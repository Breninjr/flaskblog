import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Primeiro Post', 'Conteúdo do primeiro post')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Segundo Post', 'Conteúdo do segundo post')
            )

connection.commit()
connection.close()