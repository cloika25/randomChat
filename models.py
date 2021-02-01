from cursor import session, engine
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column('id', Integer, primary_key=True)
    username = Column('username', String)
    partnerId = Column('partnerId', Integer, ForeignKey('users.id'))

    @classmethod
    def add(cls, elem):
        session.add(elem)
        session.commit()

    @classmethod
    def get(cls, id):
        return session.query(cls).filter(cls.id == id).first()

    @classmethod
    def all(cls):
        return session.query(cls).all()


Base.metadata.create_all(engine)
