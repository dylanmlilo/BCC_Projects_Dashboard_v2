from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

db_connection_string = os.getenv('db_connection_string')

engine = create_engine(db_connection_string)

Session = sessionmaker(bind=engine)

session = Session()