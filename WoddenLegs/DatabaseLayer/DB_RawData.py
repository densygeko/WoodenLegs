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


    def delete_by_ID(id):
        conn = sqlite3.connect('dbwoddenlegs.db')
        c = conn.cursor()
        c.execute(
            "DELETE FROM RawData WHERE id= ?;", (id,)
            )
        conn.commit()
        conn.close()

    def find_by_ID(id):
        conn= sqlite3.connect('dbwoddenlegs.db')
        c = conn.cursor()
        c.execute(
            "SELECT * FROM RawData Where id= ?",(id,)
            )
        rows = c.fetchall()
        
        conn.close()
        return rows     
    
    def find_all():
        conn = sqlite3.connect('dbwoddenlegs.db')
        c = conn.cursor()
        c.execute(
            "Select * From RawData"
            )
        rows = c.fetchall()
        conn.close()
        return rows