import shutil

from peewee import *
from playhouse.migrate import *

# Connect to the database
# Other modules in project should use 'from db.db import db' to access it
shutil.copy("default_db.sqlite", "db.sqlite")
db = SqliteDatabase('db.sqlite')
migrator = SqliteMigrator(db)
db.connect()