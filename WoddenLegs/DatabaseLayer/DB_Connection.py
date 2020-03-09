import sqlite3
class DB_Connection(object):



    def db_check():
        conn = sqlite3.connect('dbwoddenlegs.db')
        c = conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS "RawData" (
    "id"    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    "text"    TEXT NOT NULL,
    "path"    TEXT NOT NULL,
    "fileType"    TEXT NOT NULL,
    "pageNumber"    INTEGER NOT NULL
);""" )

        c.execute("""CREATE TABLE IF NOT EXISTS "Number" (
    "id"    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    "path"    TEXT NOT NULL,
    "identifier"    TEXT NOT NULL,
    "id_raw"    INTEGER NOT NULL
);""")

        c.execute("""CREATE TABLE IF NOT EXISTS "Ip" (
    "id"    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    "path"    TEXT NOT NULL,
    "identifier"    TEXT NOT NULL,
    "id_rawData"    INTEGER
); """)

        c.execute("""CREATE TABLE IF NOT EXISTS "Email" (
    "id"    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    "path"    TEXT NOT NULL,
    "identifier"    TEXT NOT NULL,
    "id_rawData"    INTEGER
); """)

        c.execute("""CREATE TABLE IF NOT EXISTS "BlacklistType" (
    "id"    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    "number"    NUMERIC CHECK(-1<number>=1),
    "email"    NUMERIC CHECK(-1<email>=1),
    "ip"    NUMERIC CHECK(-1<ip>=1)
); """)

        c.execute ("""CREATE TABLE IF NOT EXISTS "BlacklistKeyWord" (
    "id"    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    "keyWord"    TEXT NOT NULL,
    "id_BlackListType"    INTEGER NOT NULL
);""")
      
        conn.commit()
        conn.close()