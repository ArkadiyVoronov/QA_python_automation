from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine("postgresql://dbuser:dbpassword@localhost/db")        #todo   уточнить
Base = declarative_base()


class order(Base):
    __tablename__ = 'order' 
    id = Column(Integer, primary_key=True, autoincrement=True, comment="Идентификатор")
    address_from = Column(String(50), unique=True, comment="Откуда")
    address_to = Column(String(50), comment="Куда")
    client_id = Column(String, ForeignKey('clients.id'), comment="Клиент")
    driver_id = Column(String, ForeignKey('drivers.id'), comment="Водитель")
    date_created = Column(timestamp, comment="дата создания")
    status = Column(String(25), comment="Статус")
