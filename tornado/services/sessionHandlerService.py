import uuid

class SessionHandlerService(object):
    def __init__(self, redisDb, sessionId, sessionTime):
        self.redisDb = redisDb
        self.sessionId = sessionId
        self.sessionTime = sessionTime
        self.refreshSession()

    def generateSessionId(self, userInfoId):
        self.sessionId = str(uuid.uuid4())
        self.redisDb.set(self.sessionId, userInfoId)
        self.setSessionExpirationTime(self.sessionTime)

    def getSessionId(self):
        return self.sessionId

    def setSessionExpirationTime(self, expirationTime):
        self.redisDb.expire(self.sessionId, expirationTime)

    def refreshSession(self):
        if self.sessionId is not None:
            self.setSessionExpirationTime(self.sessionTime)

    def getUserInfoId(self):
        if self.sessionId is not None:
            return self.redisDb.get(self.sessionId)
        else:
            return None