import sqlite3
class DB_Connection(object):#Creates database with tables if it don't already exist

    def db_check():
        conn = sqlite3.connect('dbwoddenlegs.db') #creates or connects to a database called dbwoddenlegs
        c = conn.cursor() #Creates a cursor to iterate trough the SQL Queries
        #Creates  a table called "RawData" if the table dosen't already exist
        c.execute("""CREATE TABLE IF NOT EXISTS "RawData" (
    "id"    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    "text"    TEXT NOT NULL,
    "path"    TEXT NOT NULL,
    "fileType"    TEXT NOT NULL,
    "pageNumber"    INTEGER NOT NULL
);""" )
        #Creates a table called "Number" if the table dosen't already exist
        c.execute("""CREATE TABLE IF NOT EXISTS "Number" (
    "id"    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    "path"    TEXT NOT NULL,
    "identifier"    TEXT NOT NULL,
    id_rawData INTEGER NOT NULL

); """)
        #Creates a table called "Ip" if the table dosen't already exist
        c.execute("""CREATE TABLE IF NOT EXISTS "Ip" (
    "id"    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    "path"    TEXT NOT NULL,
    "identifier"    TEXT NOT NULL,
    "id_rawData"    INTEGER
); """)
        #Creates a table called "Email" if the table dosen't already exist
        c.execute("""CREATE TABLE IF NOT EXISTS "Email" (
    "id"    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    "path"    TEXT NOT NULL,
    "identifier"    TEXT NOT NULL,
    "id_rawData"    INTEGER
); """)
        #Creates a table called "BlacklistType" if the table dosen't already exist
        c.execute("""CREATE TABLE IF NOT EXISTS "BlacklistType" (
    "id"    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    "number"    NUMERIC CHECK(-1<number>=1),
    "email"    NUMERIC CHECK(-1<email>=1),
    "ip"    NUMERIC CHECK(-1<ip>=1)
); """)
       
        #Creates a table called "BlacklistKeyword" if the table dosen't already exist
        c.execute ("""CREATE TABLE IF NOT EXISTS "BlacklistKeyWord" (
    "id"    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    "keyWord"    TEXT NOT NULL,
    "id_BlackListType"    INTEGER NOT NULL
);""")
      
        conn.commit() #Commits to the database
        conn.close()  #Closes the connection to the database