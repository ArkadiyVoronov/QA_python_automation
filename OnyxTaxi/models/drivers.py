from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine("postgresql://dbuser:dbpassword@localhost/db")
Base = declarative_base()

class Drivers(Base):
    __tablename__ = 'drivers'
    id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable=False)
    car = Column(String(25), nullable=False)
