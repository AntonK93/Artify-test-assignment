import tornado.web
import json

from routes.validators import UserInfoValidationSchema
from marshmallow import ValidationError

from services.sessionHandlerService import SessionHandlerService

from repositories.userInfoRepository import UserInfoRepository
from repositories.sectorRepository import SectorRepository

class BaseHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.sessionHandler = SessionHandlerService(self.settings['redisDb'], self.get_cookie('session_id'), self.settings['config'].SESSION_TIME)
        self.userInfoId = self.sessionHandler.getUserInfoId()

    def prepare(self):
        self.args = {}
        if 'Content-Type' in self.request.headers:
            if 'application/json' in self.request.headers['Content-Type']:
                jsonBody = json.loads(self.request.body)
                if 'data' in jsonBody:
                    self.args = jsonBody['data']

    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', self.settings['config'].CLIENT_APP)
        self.set_header('Access-Control-Allow-Headers', 'Content-Type')
        self.set_header('Access-Control-Allow-Credentials', 'true')
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, PATCH, DELETE, OPTIONS')
        self.set_header('Content-type', 'application/json')

    def options(self):
        self.set_status(204)
        self.finish()

    def finishWithValidationError(self, errors):
        self.set_status(422)
        self.finish(json.dumps({'message': 'Validation error', 'errors': errors}))

    def finishWithCustomError(self, error):
        self.set_status(423)
        self.finish(json.dumps({'message': error}))

    def finishWithMessage(self, message):
        self.finish(json.dumps({'message': message}))

    def finishWithMessageAndData(self, message, data):
        self.finish(json.dumps({'message': message, 'data': data}))


class userInfoHandler(BaseHandler):
    def initialize(self):
        super().initialize()
        self.userInfoRepository = UserInfoRepository(self.settings['db'])
        self.userExist = self.userInfoRepository.getUserInfo(self.userInfoId) is not None

    def get(self):
        if self.userExist is not False:
            self.finishWithMessageAndData('Successfully!',  self.userInfoRepository.getUserInfoJson(self.userInfoId))
        else:
            # Custom approach to clear cookies, set_cookie method does not have param to set expiration time
            self.set_header('Set-Cookie', 'session_id='+self.sessionHandler.getSessionId()+';expires=Thu, 01 Jan 1970 00:00:00 GMT;path=/')
            self.finishWithMessage('Not Authorized')

    def post(self):
        try:
            userValidatedData = UserInfoValidationSchema().load(self.args)
        except ValidationError as err:
            self.finishWithValidationError(err.messages)

        userInfoId = self.userInfoRepository.createUserInfo(userValidatedData)

        self.sessionHandler.generateSessionId(userInfoId)

        self.set_cookie("session_id", self.sessionHandler.getSessionId())

        self.finishWithMessage('User info was created successfully!')

    def patch(self):
        try:
            userValidatedData = UserInfoValidationSchema().load(self.args)
        except ValidationError as err:
            self.finishWithValidationError(err.messages)

        if self.userExist is not False:
            self.userInfoRepository.updateUserInfo(userValidatedData, self.userInfoId)

            self.finishWithMessage('User info was updated successfully!')
        else:
            self.finishWithCustomError('Cannot update data, user not found')


class sectorsHandler(BaseHandler):
    def initialize(self):
        super().initialize()
        self.sectorRepository = SectorRepository(self.settings['db'])

    def get(self):
        self.finishWithMessageAndData('Successfully!', self.sectorRepository.getSectorsJson())

class routes():
    def get_routes():
        return [
            (r"/api/user_info", userInfoHandler),
            (r"/api/sectors", sectorsHandler),
        ]
