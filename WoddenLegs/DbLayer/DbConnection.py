class DbConnection(object):
    """description of class"""
    import sqlite3
    from sqlite3 import Error
 
    conn = sqlite3.connect('dbwoddenlegs.db')
    def __init__(self,):
        return self;

    def getconnection():
    
     c = conn.cursor()
    
     c.execute("""SELECT * FROM RawData where id='5' """)

     print(c.fetchall())

     conn.commit()

     conn.close()







