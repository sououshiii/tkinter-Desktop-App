import sqlite3


class DB():
    def __init__(self):
        self.connection = sqlite3.connect("bookstore.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS books(id INTEGER PRIMARY KEY, title TEXT,author TEXT,publish_year TEXT,isbn TEXT)""")

    def fetch(self):
        self.cursor.execute("Select * FROM books")
        all_rows =self.cursor.fetchall()
        return all_rows

    def insert(self, title, author, publish_year, isbn):
        self.cursor.execute("INSERT INTO books VALUES (NULL, ?, ?, ?, ?)", (title, author, publish_year, isbn))
        self.connection.commit()

    def delete(self, id):
        self.cursor.execute("DELETE FROM books WHERE id=?", (id,))
        self.connection.commit()

    def update(self, id, title, author, publish_year, isbn):
        self.cursor.execute("UPDATE books WHERE id =? SET title=?, author=?, publish_year=?, isbn=?", (id, title, author, publish_year, isbn))
        self.connection.commit()

    def search(self, title, author, publish_year, isbn):
        self.cursor.execute("Select * FROM books WHERE title=? AND author=? AND publish_year=? AND isbn=?", (title, author, publish_year, isbn))
        search_result = self.cursor.fetchall()
        return search_result

