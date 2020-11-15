from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import TINYINT
from marshmallow_sqlalchemy import ModelSchema, fields

from config.config import Base
from models.userInfoSelectedSectorsPivot import UserInfoSelectedSectorsPivot, UserInfoSelectedSectorsPivotSchema

class UserInfo(Base):
    __tablename__ = 'users-info'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(125))
    terms_agreed = Column(TINYINT(unsigned=True))
    selected_sectors = relationship("UserInfoSelectedSectorsPivot")

class UserInfoSchema(ModelSchema):
    class Meta:
        model = UserInfo
        exclude = ["id"]
        include_relationships = True
        include_fk = True
        load_instance = True

    selected_sectors = fields.Nested('UserInfoSelectedSectorsPivotSchema', many=True)