import os
import shutil

from peewee import *
from playhouse.migrate import *

# Connect to the database
# Other modules in project should use 'from db.db import db' to access it
shutil.copy(os.path.abspath(__file__ + "/../../default_db.sqlite"), os.path.abspath(__file__ + "/../../db.sqlite"))
db = SqliteDatabase(os.path.abspath(__file__ + "/../../db.sqlite"))
migrator = SqliteMigrator(db)
db.connect()