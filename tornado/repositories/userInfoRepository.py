from models.userInfo import UserInfo, UserInfoSchema
from models.userInfoSelectedSectorsPivot import UserInfoSelectedSectorsPivot, UserInfoSelectedSectorsPivotSchema

class UserInfoRepository(object):
    def __init__(self, db):
        self.db = db
        self.userInfoSchema = UserInfoSchema()

    def getUserInfo(self, userInfoId):
        return self.db.query(UserInfo).filter(UserInfo.id == userInfoId).first()

    def getUserInfoJson(self, userInfoId):
        return self.userInfoSchema.dump(self.getUserInfo(userInfoId))

    def createUserInfo(self, userData):
        newUserInfoEntry = UserInfo(name=userData['name'], terms_agreed=userData['terms_agreed'])
        self.db.add(newUserInfoEntry)
        self.db.commit()

        self.syncUserInfoSectors(userData['selected_sectors'], newUserInfoEntry.id);
        return newUserInfoEntry.id

    def updateUserInfo(self, userData, userInfoId):
        self.db.query(UserInfo).filter(UserInfo.id == userInfoId).update({"name": userData['name'], "terms_agreed": userData['terms_agreed']})
        self.db.commit()

        self.syncUserInfoSectors(userData['selected_sectors'], userInfoId)

    def syncUserInfoSectors(self, sectors, userInfoEntryId):
        self.db.query(UserInfoSelectedSectorsPivot).filter(UserInfoSelectedSectorsPivot.user_info_entry == userInfoEntryId).delete(synchronize_session='fetch')
        self.db.commit()

        for sector in sectors:
            user_sector=UserInfoSelectedSectorsPivot(user_info_entry=userInfoEntryId,sector_entry=sector['id'])
            self.db.add(user_sector)

        self.db.commit()