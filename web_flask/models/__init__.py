#!/bin/python3

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base_model import Base

# Define database connection URL
db_url = 'mysql+mysqlconnector://{}:{}@{}/{}'.format(
    os.getenv('HBNB_MYSQL_USER'),
    os.getenv('HBNB_MYSQL_PWD'),
    os.getenv('HBNB_MYSQL_HOST'),
    os.getenv('HBNB_MYSQL_DB')
)

# Create SQLAlchemy engine
engine = create_engine(db_url, pool_pre_ping=True)

# Create session maker
Session = sessionmaker(bind=engine)

# Create all tables in the database if they don't exist
Base.metadata.create_all(engine)
