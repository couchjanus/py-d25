import sqlite3

db = 'product.db'

class Product:

    def __init__(self):
        with sqlite3.connect(db) as conn:
            cursor = conn.cursor()
            cursor.execute("""select * from products""")
            self.products = cursor.fetchall()

    def all(self):
        with sqlite3.connect(db) as conn:
            cursor = conn.cursor()
            cursor.execute("""select * from products""")
            return cursor.fetchall()
   
    def show(self, id):
        with sqlite3.connect(db) as conn:
            cursor = conn.cursor()
            query = "select * from products where id = :id"
            cursor.execute(query, {'id': id})
            return cursor.fetch()
