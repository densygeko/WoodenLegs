import DB_Connection
import sqlite3
class BlacklistType(object):
    """description of class"""
    
    DB_Connection.DB_Connection.db_check()
    
    def UPdate_number_true():
        conn = sqlite3.connect('dbwoddenlegs.db')
        c = conn.cursor()
        c.execute(
          """UPDATE "main"."BlacklistType" SET "number"=1 WHERE "id"='1';
            """)
        conn.commit()
        conn.close()
    def UPdate_number_false():
        conn = sqlite3.connect('dbwoddenlegs.db')
        c = conn.cursor()
        c.execute("""UPDATE "main"."BlacklistType" SET "number"=0 WHERE "id"='1';""")
        conn.commit()
        conn.close()
    def update_email_ture():

        conn = sqlite3.connect('dbwoddenlegs.db')
        c = conn.cursor()
        c.execute(
          """UPDATE "main"."BlacklistType" SET "email"=1 WHERE "id"='1';
            """)
        conn.commit()
        conn.close()
    def update_email_false():
        conn = sqlite3.connect('dbwoddenlegs.db')
        c = conn.cursor()
        c.execute(
          """UPDATE "main"."BlacklistType" SET "email"=0 WHERE "id"='1';
            """)
        conn.commit()
        conn.close()
    def update_ip_true():
        conn = sqlite3.connect('dbwoddenlegs.db')
        c = conn.cursor()
        c.execute(
          """UPDATE "main"."BlacklistType" SET "true"=1 WHERE "id"='1';
            """)
        conn.commit()
        conn.close()
    def update_ip_false():
        conn = sqlite3.connect('dbwoddenlegs.db')
        c = conn.cursor()
        c.execute(
         """UPDATE "main"."BlacklistType" SET "number"= 0 WHERE id ='1';
            """)
        conn.commit()
        conn.close()
    def get_BleckliostType():
        conn = sqlite3.connect('dbwoddenlegs.db')
        c = conn.cursor()
        c.execute("Select * From BlacklistType")
        row = c.fetchall()
        conn.close()
        return row