from sqlalchemy import Column, Integer, String, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.dialects.mysql import TINYINT
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields

from config.config import Base

class UserInfoSelectedSectorsPivot(Base):
    __tablename__ = 'user-info-selected-sectors-pivot'
    __table_args__ = (PrimaryKeyConstraint('user_info_entry','sector_entry'),)
    
    user_info_entry = Column(Integer, ForeignKey('users-info.id'))
    sector_entry = Column(Integer, ForeignKey('sectors.id'))

class UserInfoSelectedSectorsPivotSchema(ModelSchema):
    id = fields.Integer(attribute="sector_entry")
    class Meta:
        model = UserInfoSelectedSectorsPivot
        exclude = ["user_info_entry", "sector_entry"]
        include_relationships = True
        include_fk = True
        load_instance = True
