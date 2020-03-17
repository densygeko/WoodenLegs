import EmailML
import DB_Connection
import sqlite3
class DB_Email(object):

    DB_Connection.DB_Connection.db_check()
    
    def insert_querry_all(path,identifier,id_rawData):
        conn = sqlite3.connect('dbwoddenlegs.db')
        c = conn.cursor()
        c.execute(
          """ INSERT INTO Email (path,identifier,id_rawdata) VALUES (?,?,?);
            """, (path,identifier,id_rawData))
        conn.commit()
        conn.close()

    def find_all():
        conn = sqlite3.connect('dbwoddenlegs.db')
        c = conn.cursor()
        c.execute(
            "Select * From Email"
            )
        rows = c.fetchall()
        EM_list = []
        for x in rows:
            EM = EmailML.Email(x[0],x[1],x[2],x[3])
            EM_list.append(EM)

        conn.close()
        return EM_list

    def find_by_ID(id):
        conn = sqlite3.connect('dbwoddenlegs.db')
        c = conn.cursor()
        c.execute(
            "SELECT * FROM Email Where id= ?",(id,)
            )
        rows = c.fetchall()
        EM = EmailML.Email(rows[0][0], rows[0][1], rows[0][2], rows[0][3])
        conn.close()
        return EM     

    def update_on_id(id, path, identifier, id_rawData):
        conn = sqlite3.connect('dbwoddenlegs.db')
        c = conn.cursor()
        c.execute("""UPDATE Email SET path= ?, identifier = ?, id_rawData= ? WHERE id= ?;""",(path, identifier, id_rawData,id,))
        conn.commit()
        conn.close()