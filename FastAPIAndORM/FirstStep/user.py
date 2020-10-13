from sqlalchemy import engine
from session import Session
from sqlalchemy import Column, Integer, String

session = Session()
DataBase = Session.get_database(session)
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
