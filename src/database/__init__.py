from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import os

loggin_needed = os.environ['PYTHONENV'] == 'test' or os.environ['PYTHONENV'] == 'dev'
engine = create_engine(os.environ['DATABASE_URI'], echo=loggin_needed)
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()
