# atlas-AirBnB_clone_v2. By Suntha Lucas, Kevin Cyrus Jr.

MySQL
    Group project Python OOP Back-end SQL MySQL ORM
    SQLAlchemy-The SQLAlchemy Object Relational Mapper presents a method of associating user- 
    defined Python classes with database tables, and instances of those classes (objects) with 
    rows in their corresponding tables.

    >>> import sqlalchemy
    >>> sqlalchemy.__version__ 
    1.3.0
This is our connection point:  
    from sqlalchemy import create_engine
    engine = create_engine('sqlite:///:memory:', echo=True)

WEB Framework
    Python Back-end Webserver Flask

To Use:
    Using DBStorage, locate the console.py file and run it using these steps:

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

The unittest:
It supports test automation, sharing of setup and shutdown code for tests, aggregation of tests into collections, and independence of the tests from the reporting framework. unittest supports some important concepts in an object-oriented way:

test fixture
A test fixture represents the preparation needed to perform one or more tests, and any associated cleanup actions. This may involve, for example, creating temporary or proxy databases, directories, or starting a server process.

test case
A test case is the individual unit of testing. It checks for a specific response to a particular set of inputs. unittest provides a base class, TestCase, which may be used to create new test cases.

test suite
A test suite is a collection of test cases, test suites, or both. It is used to aggregate tests that should be executed together.

test runner
A test runner is a component which orchestrates the execution of tests and provides the outcome to the user. The runner may use a graphical interface, a textual interface, or return a special value to indicate the results of executing the tests.

Example test:
import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()

Command-Line Interface:
The unittest module can be used from the command line to run tests from modules, classes or even individual test methods:

python -m unittest test_module1 test_module2
python -m unittest test_module.TestClass
python -m unittest test_module.TestClass.test_method
You can pass in a list with any combination of module names, and fully qualified class or method names.

Test modules can be specified by file path as well:
