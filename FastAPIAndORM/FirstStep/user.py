from sqlalchemy import engine
from sqlalchemy.orm import sessionmaker
from session import Session
from sqlalchemy import Column, Integer, String
from pprint import pprint


session = Session()
DataBase = Session.get_engine(session)
Base = Session.get_base(session)

class User(Base):
    __tablename__ = "user"

    user_id: int = Column(Integer, nullable=False, primary_key=True)
    user_name:str = Column(String(32), nullable=False)

    def __init__(self, user_name: str) -> None:
        self.user_name = user_name

    def __repr__(self) -> str:
        return "{0} is {1}".format(self.user_id, self.user_name)


Base.metadata.create_all(DataBase)

ed_user = User('Bao')
orm_session = sessionmaker(bind=DataBase)
db_session = orm_session()
db_session.add(ed_user)
db_session.commit()
our_users = db_session.query(User).all()
pprint(our_users)