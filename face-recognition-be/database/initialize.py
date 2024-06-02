from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from database.models import base

class Initialize:
  def __init__(self, conn_str: str) -> None:
    self.engine = create_engine(conn_str)
    self.init_db()
    self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

  def init_db(self):
    if not database_exists(self.engine.url):
      create_database(self.engine.url)
    base.metadata.create_all(self.engine, checkfirst=True)

  