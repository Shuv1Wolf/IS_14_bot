import sqlite3
connection = sqlite3.connect('../Databases/users_id.db')
cur = connection.cursor()



cur.execute("""CREATE TABLE IF NOT EXISTS all_id (
    id INTEGER UNIQUE ON CONFLICT REPLACE NOT NULL,
    name TEXT
 );""")



connection.commit()
