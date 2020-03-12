import sqlite3
import DB_Connection

class DB_BlacklistKeyword(object):
    """description of class"""
    DB_Connection.DB_Connection.db_check()

    def insert_into_blacklist(keyword, id_blacklistType):
        conn = sqlite3.connect('dbwoddenlegs.db')
        c = conn.cursor()
        c.execute(""" INSERT INTO BlacklistKeyWord (keyword,id_blacklistType) VALUES (?,?);
            """,(keyword, id_blacklistType))
        conn.commit()
        conn.close()

    def select_all_Blacklist_keyword():
        conn = sqlite3.connect('dbwoddenlegs.db')
        c = conn.cursor()
        c.execute(""" Select * From BlacklistKeyWord""")
        row = c.fetchall()
        conn.close()
        return row

    def update_on_id(id, keyword, ID_blacklistType):
        conn = sqlite3.connect('dbwoddenlegs.db')
        c = conn.cursor()
        c.execute("""UPDATE BlacklistKeyWord SET keyWord= ?, id_BlackListType = ? WHERE id= ?;""",(keyword, ID_blacklistType, id,))
        conn.commit()
        conn.close()

    def select_on_id(id):
        conn = sqlite3.connect('dbwoddenlegs.db')
        c = conn.cursor()
        c.execute(""" select * from BlacklistKeyWord where id = ? """,(id,))
        row = c.fetchall()
        conn.close()
        return row

    def delete_from_BlacklistKeyword(id):
        conn = sqlite3.connect('dbwoddenlegs.db')
        c = conn.cursor()
        c.execute("""DELETE FROM BlacklistKeyWord WHERE id=?; """,(id))
        conn.commit()
        conn.close()