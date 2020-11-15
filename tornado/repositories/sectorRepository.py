from models.sector import Sector, SectorSchema
from sqlalchemy import orm
from models.userInfoSelectedSectorsPivot import UserInfoSelectedSectorsPivot, UserInfoSelectedSectorsPivotSchema

class SectorRepository(object):
    def __init__(self, db):
        self.db = db
        self.sectorSchema = SectorSchema(many=True)

    def getSectors(self):
        return self.db.query(Sector).options(orm.joinedload('children')).filter(Sector.parent_sector == None).all()

    def getSectorsJson(self):
        return self.sectorInfoToJson(self.getSectors())

    def sectorInfoToJson(self, sectorsData):
        return self.sectorSchema.dump(sectorsData)