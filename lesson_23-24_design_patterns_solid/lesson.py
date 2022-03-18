from sqlalchemy import Table, String, Boolean, Column, Integer, ForeignKey, create_engine, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from contextlib import contextmanager
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine(u'sqlite:///some.db', echo=True)
session = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()

# Session = scoped_session(sessionmaker(autoflush=True, autocommit=False, bind=engine))
#
# @contextmanager
# def session_scope():
#         session = Session()
#         try:
#             yield session
#             session.commit()
#         except:
#             print("OTRABOTAL ROLLBACK")
#             session.rollback()
#             raise
#         finally:
#             session.close()


class Items (Base):
    __tablename__ = 'items'
    identifier = Column(Integer, primary_key=True, comment="Идентификатор предмета")
    name = Column(String(25), unique=True, comment="Название предмета")
    type = Column(String(25), comment="возможные значения weapon/armor/potion/quest_item")
    attack = Column(Float, comment="атака предмета")
    defense = Column(Float, comment="деф предмета")
    special_ability = Column(String(25), comment="абилка предмета")
    backpacks = relationship('Backpacks')


class Players(Base):
    __tablename__ = 'players'
    identifier = Column(Integer, primary_key=True, comment='Уникальный идентификатор товара')
    nickname = Column(String(25), unique=True, comment='Nickname')
    character_class = Column(String, comment='Класс')
    character_passive_ability = Column(String, comment='Пассивная способность')
    backpacks = relationship('Backpacks')


class Backpacks(Base):
    __tablename__ = 'backpacks'
    id = Column(Integer, primary_key=True, comment="Идентификатор рюкзака")
    player_identifier = Column(Integer, ForeignKey("players.identifier"), comment="Отношение к игроку")
    item_identifier = Column(Integer, ForeignKey("items.identifier"), comment="Отношение к предмету")
    amount = Column(Integer, comment="Количество предметов")
    equipped = Column(Boolean, comment="Признак одет или нет предмет")


Base.metadata.create_all(engine)


# session = Sesion()

# duck = Players( nickname = "best_duck",
# character_class = "busy",
# character_passive_ability =
# )
# first_items

# with session_scope() as session:
# sword =

# with session_scope() as session:
#     new_player = Player(nickname="Player4",
#                         character_race="ogre",
#                         character_class="warrior",
#                         character_passive_ability="fire resist")
