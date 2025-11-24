from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DateTime, Text
from sqlalchemy.sql import func
from sqlalchemy.orm import registry
from config import DATABASE_URL

engine = create_engine(DATABASE_URL, connect_args={'check_same_thread': False})
mapper_registry = registry()
metadata = mapper_registry.metadata

fancy_table = Table(
    'fancy_names', metadata,
    Column('user_id', Integer, primary_key=True),
    Column('username', String(128)),
    Column('prefix', String(16)),
    Column('suffix', String(16)),
    Column('fancy_name', String(256)),
    Column('created_at', DateTime, server_default=func.now())
)

# simple init helper
def init_db():
    metadata.create_all(engine)

