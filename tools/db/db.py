import os
import shutil

from peewee import *
from playhouse.migrate import *

# Connect to the database
# Other modules in project should use 'from db.db import db' to access it
db = SqliteDatabase(os.path.abspath(__file__ + "/../../default_db.sqlite"))
migrator = SqliteMigrator(db)
db.connect()