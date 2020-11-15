from sqlalchemy import Column, Integer, String, ForeignKey, ForeignKeyConstraint
from sqlalchemy.orm import relationship
from marshmallow_sqlalchemy import ModelSchema, fields

from config.config import Base

class Sector(Base):
    __tablename__ = 'sectors'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    parent_sector = Column(Integer, ForeignKey('sectors.id', ondelete='SET NULL'))
    children = relationship("Sector")

class SectorSchema(ModelSchema):
    class Meta:
        model = Sector
        include_relationships = True
        include_fk = True
        load_instance = True

    children = fields.Nested('self', many=True)
