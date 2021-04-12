from parse import get_default_table, create_table, get_table_info


class Table:
    instance = None
    default_db = {}
    db = {}
    info = {}

    def __init__(self):
        if Table.instance is None:
            Table.instance = self
        else:
            self = Table.instance

    def __getitem__(self, key):
        return self.db[key]

    def create(self):
        self.default_db = get_default_table()
        self.db = create_table(self.default_db)
        self.info = get_table_info()

    def items(self):
        return self.db.items()
