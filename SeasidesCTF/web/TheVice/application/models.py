import uuid
from database import Base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Boolean, DateTime, Column, Integer, \
                       String, ForeignKey

def DefaultUUID():
    return str(uuid.uuid4())

class Device(Base):
    __tablename__ = 'devices'
    id = Column(Integer, primary_key=True)
    uuid = Column(String(54), unique=True, default=DefaultUUID)
    status = Column(String(50), default='offline')
    admin = Column(Boolean, default=False)
    last_tick = Column(DateTime())