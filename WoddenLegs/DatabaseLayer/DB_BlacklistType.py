import DB_Connection
import sqlite3
import BlacklistType
class DB_BlacklistType(object):
    """interact with the BlacklistType table in the database"""
    
    DB_Connection.DB_Connection.db_check() # makes a database if there are none
    
    def UPdate_number_true():
        conn = sqlite3.connect('dbwoddenlegs.db') #connet with the database
        c = conn.cursor() #Creates a cursoer to iterate trough the SQL queries
        c.execute( #Executes a queries that set the number table to 1 /true
          """UPDATE "main"."BlacklistType" SET "number"=1 WHERE "id"='1';
            """)
        conn.commit() #commit the querie
        conn.close() #close the datadase connetion 

    def UPdate_number_false():
        conn = sqlite3.connect('dbwoddenlegs.db') #connet with the database
        c = conn.cursor()#Creates a cursoer to iterate trough the SQL queries
        c.execute("""UPDATE "main"."BlacklistType" SET "number"=0 WHERE "id"='1';""") #Executes a queries that set the number table to 0 /false
        conn.commit() #commits the query
        conn.close() #close the connetion to the Database

    def update_email_ture():

        conn = sqlite3.connect('dbwoddenlegs.db')#connet with the database
        c = conn.cursor()#Creates a cursoer to iterate trough the SQL queries
        c.execute( #Executes a queries that set the emil table to 1 /true
          """UPDATE "main"."BlacklistType" SET "email"=1 WHERE "id"='1'; 
            """) 
        conn.commit() #commits the query
        conn.close() #close the connetion to the Database

    def update_email_false():
        conn = sqlite3.connect('dbwoddenlegs.db') #connet with the database
        c = conn.cursor()#Creates a cursoer to iterate trough the SQL queries
        c.execute( #Executes a queries that set the email table to 0 /false
          """UPDATE "main"."BlacklistType" SET "email"=0 WHERE "id"='1';
            """)
        conn.commit() #commits the query
        conn.close() #close the connetion to the Database

    def update_ip_true():
        conn = sqlite3.connect('dbwoddenlegs.db') #connet with the database
        c = conn.cursor()#Creates a cursoer to iterate trough the SQL queries
        c.execute( #Executes a queries that set the ip table to 1 /true
          """UPDATE "main"."BlacklistType" SET "true"=1 WHERE "id"='1';
            """)
        conn.commit() #commits the query
        conn.close()#close the connetion to the Database

    def update_ip_false():
        conn = sqlite3.connect('dbwoddenlegs.db')
        c = conn.cursor()#Creates a cursoer to iterate trough the SQL queries
        c.execute( #Executes a queries that set the ip table to 0 /false
         """UPDATE "main"."BlacklistType" SET "number"= 0 WHERE id ='1';
            """)
        conn.commit()  #cp,,otes the query
        conn.close() #close the connettion to the Database

    def get_BleckliostType():
        conn = sqlite3.connect('dbwoddenlegs.db') #connet with the database
        c = conn.cursor()#Creates a cursoer to iterate trough the SQL queries
        c.execute("Select * From BlacklistType") #there is only tuple in the table or there is only supose to one
        row = c.fetchall() #Creates a list of tubles (tubles is a list of strings) from the querry resultset called rows
        blt = BlacklistType.BlacklistType(row[0][0],row[0][1],row[0][2],row[0][3])
        conn.close() #close the connettion to the Database
        return blt #return  BlacklistType