from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import os


class Singleton(type):
    def __call__(cls, *args, **kwargs):
        try:
            return cls.instance
        except AttributeError:
            cls.instance = super(Singleton, cls).__call__(*args, **kwargs)
            return cls.instance


class Session(object, metaclass=Singleton):
    Base = None

    def __init__(self) -> None:
        self.database = self._get_database(self)
        self.Base = declarative_base()

    @staticmethod
    def _get_database(self):
        link = self._get_links(
            host=os.environ.get("MARIA_HOST", "localhost"),
            port=int(os.environ.get("MARIA_PORT", 13306)),
            db='maru',
            user_name='root',
            user_password='42maru')
        return create_engine(link, echo=True)
        

    @staticmethod
    def _get_links(host, port, db, user_name, user_password):
        return 'mysql://{0}:{1}@{2}:{3}/{4}'.format(user_name, user_password, host, port, db)

    def get_base(self):
        return self.Base

    def get_engine(self):
        return self.database


if __name__ == "__main__":
    Session()
    print("Init Session")