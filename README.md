# atlas-AirBnB_clone_v2. By Suntha Lucas, kevin Cyprus Jr.

MySQL
    Group project Python OOP Back-end SQL MySQL ORM
    SQLAlchemy-The SQLAlchemy Object Relational Mapper presents a method of associating user-defined Python classes with database tables, and instances of those classes (objects) with rows in their corresponding tables.

    >>> import sqlalchemy
    >>> sqlalchemy.__version__ 
    1.3.0
This is our connection point:  
    from sqlalchemy import create_engine
    engine = create_engine('sqlite:///:memory:', echo=True)

WEB Framework
    Python Back-end Webserver Flask

To Use:
    Using DBStorage, locat the console.py file and run it using these steps:

    $ HBNB_MYSQL_USER=hbnb _dev HBNB_MYSQL_PWD=hbnb_dev_pwd
    use: FileStorage, then locate the console.py file and run using the following:
    ./console.py
    
Support classes:
    User
    State
    BaseModel
    City 
    Amenity
    Place
    Review

We used the following commands:
    Create
    Show
    Destroy
    All
    quit/EOF
    Help

Environment variables were our best friend for this project!

HBNB_ENV: running environment. It can be “dev” or “test” for the moment (“production” soon!)
HBNB_MYSQL_USER: the username of your MySQL
HBNB_MYSQL_PWD: the password of your MySQL
HBNB_MYSQL_HOST: the hostname of your MySQL
HBNB_MYSQL_DB: the database name of your MySQL
HBNB_TYPE_STORAGE: the type of storage used. It can be “file” (using FileStorage) or db (using DBStorage)

