import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DB_URL = os.environ.get("DB_URL")

# create a connection to DB
db_engine = create_engine(url=DB_URL)

# create DB Session Class using the DB engine
SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=db_engine)

# create an SQLAlchemy base class to map Python classes to DB tables
Base = declarative_base()


def get_db():
    """
    creates and returns a DB session for all db related transactions
    """
    # create a new DB session
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
