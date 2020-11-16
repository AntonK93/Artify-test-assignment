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
        self.set_header('Content-type', 'application/json')

    def options(self):
        self.set_status(204)
        self.finish()

    def finishWithErrors(self, errors):
        self.set_status(422)
        self.finish(json.dumps({'errors': errors}))


class userInfoHandler(BaseHandler):
    def initialize(self):
        super().initialize()
        self.userInfoRepository = UserInfoRepository(self.settings['db'])
        self.userExist = self.userInfoRepository.getUserInfo(self.userInfoId) is not None

    def get(self):
        if self.userExist is not False:
            response = json.dumps({'data': self.userInfoRepository.getUserInfoJson(self.userInfoId)})
        else:
            response = json.dumps({'message': 'Not Authorized'})

        self.write(response)

    def post(self):
        try:
            userValidatedData = UserInfoValidationSchema().load(self.args)
        except ValidationError as err:
            return self.finishWithErrors(err.messages)

        if self.userExist is not False:
            self.userInfoRepository.updateUserInfo(userValidatedData, self.userInfoId)

            response = json.dumps({'message': 'User info was updated successfully!'})
        else:
            userInfoId = self.userInfoRepository.createUserInfo(userValidatedData)

            self.sessionHandler.generateSessionId(userInfoId)
            response = json.dumps({'message': 'User info was created successfully!'})

        self.set_cookie("session_id", self.sessionHandler.getSessionId())

        self.write(response)

class sectorsHandler(BaseHandler):
    def initialize(self):
        super().initialize()
        self.sectorRepository = SectorRepository(self.settings['db'])

    def get(self):
        response = json.dumps({'data': self.sectorRepository.getSectorsJson()})
        self.write(response)

class routes():
    def get_routes():
        return [
            (r"/api/user_info", userInfoHandler),
            (r"/api/sectors", sectorsHandler),
        ]
