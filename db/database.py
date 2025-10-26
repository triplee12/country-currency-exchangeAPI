from sqlalchemy import MetaData, create_engine
from databases import Database
from sqlalchemy import engine as sqla_engine
from config import settings


metadata = MetaData()

DATABASE_URL = settings.DATABASE_URL

engine = create_engine(DATABASE_URL)

database = Database(DATABASE_URL)
