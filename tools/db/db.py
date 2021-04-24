from peewee import *
from playhouse.migrate import *

# Connect to the database
# Other modules in project should use 'from db.db import db' to access it
db = SqliteDatabase('db.sqlite')
migrator = SqliteMigrator(db)
db.connect()


# Add a new column:
# migrate(migrator.add_column("entrance", "test", CharField(null=True)))
# migrate(migrator.add_column("item", "key_name", CharField(null=True)))
# migrate(migrator.add_column("item", "value", IntegerField(null=True)))