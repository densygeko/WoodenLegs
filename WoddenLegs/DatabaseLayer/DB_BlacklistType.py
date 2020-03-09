import DB_Connection
import sqlite3
class BlacklistType(object):
    """description of class"""
    
    DB_Connection.DB_Connection.db_check()
    
    def insert_querry_all(number,email,Ip):
        conn = sqlite3.connect('dbwoddenlegs.db')
        c = conn.cursor()
        DB_Connection.DB_Connection.c.execute(
          """ INSERT INTO "main"."BlacklistType"("number","email","ip") VALUES (?,?,?);
            """, (number,email,Ip))
        conn.commit
        conn.close