from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from settings import DATABASE

username = DATABASE["username"]
password = DATABASE["password"]
host = DATABASE["host"]
port = DATABASE["port"]
database = DATABASE["database"]


# create engine
engine = create_engine(
    f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}",
    pool_size=20,
    max_overflow=0,
    pool_timeout=300,
)

# make a session
Session = sessionmaker(engine, future=True)

# set up base
Base = declarative_base()
