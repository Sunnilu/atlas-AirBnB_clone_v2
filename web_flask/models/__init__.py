#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from models.state import Base

# Configure the database connection
engine = create_engine('sqlite:///your_database.db')
Base.metadata.create_all(engine)

# Create a scoped session
Session = scoped_session(sessionmaker(bind=engine, expire_on_commit=False))
