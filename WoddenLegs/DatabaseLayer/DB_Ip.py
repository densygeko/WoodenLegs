import IpML
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
        ip_list = []
        for x in rows:
            ip = IpML.Ip(x[0],x[1],x[2],x[3])
            ip_list.append(ip)

        conn.close()
        return ip_list

        

    def find_by_ID(id):
        conn = sqlite3.connect('dbwoddenlegs.db')
        c = conn.cursor()
        c.execute(
            "SELECT * FROM Ip Where id= ?",(id,)
            )
        rows = c.fetchall()
        ip = IpML.Ip(rows[0][0], rows[0][1], rows[0][2], rows[0][3])
        conn.close()
        return ip 
    
    def update_on_id(id, path, identifier, id_rawData):
        conn = sqlite3.connect('dbwoddenlegs.db')
        c = conn.cursor()
        c.execute("""UPDATE Ip SET path= ?, identifier = ?, id_rawData= ? WHERE id= ?;""",(path, identifier, id_rawData,id,))
        conn.commit()
        conn.close()

