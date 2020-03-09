import DB_Connection
import sqlite3
class DB_RawData(object):

    DB_Connection.DB_Connection.db_check()
    
    def insert_querry_all(text,path,fileType,pageNumber):
        conn = sqlite3.connect('dbwoddenlegs.db')
        c = conn.cursor()
        c.execute(
          """ INSERT INTO RawData (text,path,fileType,pageNumber) VALUES (?,?,?,?);
            """, (text,path,fileType,pageNumber))
        conn.commit()
        conn.close()


    def insert_querry_all(text,path,fileType):
        conn = sqlite3.connect('dbwoddenlegs.db')
        c = conn.cursor()
        c.execute(
          """ INSERT INTO RawData (text,path,fileType) VALUES (?,?,?);
            """, (text,path,fileType))
        conn.commit()
        conn.close()
        


    def Delete_by_ID(id):
        conn = sqlite3.connect('dbwoddenlegs.db')
        c = conn.cursor()
        c.execute(
            """DELETE FROM RawData WHERE id=?; """(id)
            )
        DB_RawData.conn.commit()
        DB_RawData.conn.close()

