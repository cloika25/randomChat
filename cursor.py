from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///users_db.db', echo=False)

Session = sessionmaker(bind=engine)
session = Session()


