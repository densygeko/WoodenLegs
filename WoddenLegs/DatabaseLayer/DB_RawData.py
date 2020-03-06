import DB_Connection
import sqlite3
class DB_RawData(object):

    DB_Connection.DB_Connection.db_check()

    def insert_querry_all(text,path,fileType):
        DB_Connection.DB_Connection.c.execute(
          """ INSERT INTO RawData (text,path,fileType) VALUES (?,?,?);
            """, (text,path,fileType))
        DB_Connection.DB_Connection.conn.commit()