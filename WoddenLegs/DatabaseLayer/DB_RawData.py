import DB_Connection
import sqlite3
import RawData 
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
        RD = RawData.RawData(rows[0][0], rows[0][1], rows[0][2], rows[0][3], rows[0][4])
        conn.close()
        return RD     
        
    def find_all():

        conn = sqlite3.connect('dbwoddenlegs.db')
        c = conn.cursor()
        c.execute(
            "Select * From RawData"
            )
        rows = c.fetchall()
        RD_list = []
        for x in rows:
            RD = RawData.RawData(x[0],x[1],x[2],x[3],x[4])
            RD_list.append(RD)
        conn.close()
        return RD_list