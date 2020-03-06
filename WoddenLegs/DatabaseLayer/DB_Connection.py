class DB_Connection(object):
    import sqlite3

    conn = sqlite3.connect('dbwoddenlegs.db')

    c = conn.cursor()
    def db_check():
        DB_Connection.c.execute("""CREATE TABLE IF NOT EXISTS "RawData" (
    "id"    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    "text"    TEXT NOT NULL,
    "path"    TEXT NOT NULL,
    "fileType"    TEXT NOT NULL
);""" )

        DB_Connection.c.execute("""CREATE TABLE IF NOT EXISTS "Number" (
    "id"    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    "path"    TEXT NOT NULL,
    "identifier"    TEXT NOT NULL,
    "id_raw"    INTEGER NOT NULL
);""")

        DB_Connection.c.execute("""CREATE TABLE IF NOT EXISTS "Ip" (
    "id"    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    "path"    TEXT NOT NULL,
    "identifier"    TEXT NOT NULL,
    "id_rawData"    INTEGER
); """)

        DB_Connection.c.execute("""CREATE TABLE IF NOT EXISTS "Email" (
    "id"    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    "path"    TEXT NOT NULL,
    "identifier"    TEXT NOT NULL,
    "id_rawData"    INTEGER
); """)

        DB_Connection.c.execute("""CREATE TABLE IF NOT EXISTS "BlacklistType" (
    "id"    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    "number"    NUMERIC CHECK(-1<number>=1),
    "email"    NUMERIC CHECK(-1<email>=1),
    "ip"    NUMERIC CHECK(-1<ip>=1)
); """)

        DB_Connection.c.execute ("""CREATE TABLE IF NOT EXISTS "BlacklistKeyWord" (
    "id"    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    "keyWord"    TEXT NOT NULL,
    "id_BlackListType"    INTEGER NOT NULL
);""")
      
        DB_Connection.conn.commit()
        DB_Connection.conn.close()