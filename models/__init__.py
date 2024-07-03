#!/usr/bin/python3
""" Models package, defines storage type """

from os import getenv

storage_t = getenv("HBNB_TYPE_STOARGE")

if storage_t == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()