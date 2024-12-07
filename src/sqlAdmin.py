import sqlite3

class SqlManager:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None
        self.cursor = None

    def connect(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

    def create_table(self, create_table_sql):
        try:
            self.cursor.execute(create_table_sql)
        except sqlite3.Error as e:
            print(e)

    def insert_data(self, insert_sql, data):
        try:
            self.cursor.execute(insert_sql, data)
            self.conn.commit()
        except sqlite3.Error as e:
            print(e)

    def query_data(self, query_sql, params = ()):
        try:
            self.cursor.execute(query_sql, params)
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(e)
            return []

    def close(self):
        if self.conn:
            self.conn.close()