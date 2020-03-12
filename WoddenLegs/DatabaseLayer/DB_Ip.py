
import DB_Connection
import sqlite3
class DB_Ip(object):

    DB_Connection.DB_Connection.db_check()
    
    def insert_querry_all(path,identifier,id_rawData):
        conn = sqlite3.connect('dbwoddenlegs.db')
        c = conn.cursor()
        c.execute(
          """ INSERT INTO Ip (path,identifier,id_rawdata) VALUES (?,?,?);
            """, (path,identifier,id_rawData))
        conn.commit()
        conn.close()

    def find_all():
        conn = sqlite3.connect('dbwoddenlegs.db')
        c = conn.cursor()
        c.execute(
            "Select * From Ip"
            )
        rows = c.fetchall()
        conn.close()
        return rows

    def find_by_ID(id):
        conn = sqlite3.connect('dbwoddenlegs.db')
        c = conn.cursor()
        c.execute(
            "SELECT * FROM Ip Where id= ?",(id,)
            )
        rows = c.fetchall()
        
        conn.close()
        return rows   
    
    def update_on_id(id, path, identifier, id_rawData):
        conn = sqlite3.connect('dbwoddenlegs.db')
        c = conn.cursor()
        c.execute("""UPDATE Ip SET path= ?, identifier = ?, id_rawData= ? WHERE id= ?;""",(path, identifier, id_rawData,id,))
        conn.commit()
        conn.close()

