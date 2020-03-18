import sqlite3
import DB_Connection
import BlacklistKeyword

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
        BL_word = [] 
        for x in row:
            BLKW = BlacklistKeyword.BlacklistKeyword(x[0],x[1],x[2])
            BL_word.append(BLKW)
        conn.close()
        return BL_word

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
        BLKW = BlacklistKeyword.BlacklistKeyword(row[0][0],row[0][1],row[0][2])
        conn.close()
        return BLKW

    def delete_from_BlacklistKeyword(id):
        conn = sqlite3.connect('dbwoddenlegs.db')
        c = conn.cursor()
        c.execute("""DELETE FROM BlacklistKeyWord WHERE id=?; """,(id))
        conn.commit()
        conn.close()