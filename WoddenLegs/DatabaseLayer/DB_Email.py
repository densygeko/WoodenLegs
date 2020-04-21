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
class DB_Email(object): #Interacrts with the Email table in the database, Insert into, select all, find by id, update on id.
    

    DB_Connection.DB_Connection.db_check() #Calls the db_check from the DB_Connection class
    
    def insert_querry_all(path,identifier,id_rawData): #Inserts all data into the Email table in the database
        conn = sqlite3.connect('dbwoddenlegs.db') #Connects to the database
        c = conn.cursor() #Creates a cursor to iterate trough the SQL Queries
        c.execute( #Executes a query to insert data into the Email table 
          """ INSERT INTO Email (path,identifier,id_rawdata) VALUES (?,?,?);
            """, (path,identifier,id_rawData))
        conn.commit() #Commits querry to the database
        conn.close()  #Closes the connection to the database

    def find_all(): # Finds all Emails in the database
        conn = sqlite3.connect('dbwoddenlegs.db') #Connects to the database
        c = conn.cursor()#Creates a cursor to iterate trough the SQL Queries
        c.execute( #Executes a query to select all emails from the Email table
            "Select * From Email"
            )
        rows = c.fetchall() #Creates a list of tubles (tubles is a list of strings) from the querry resultset called rows
        EM_list = [] #Creates an empty list
        for x in rows: #Iterates trough the list of tubles
            EM = EmailML.Email(x[0],x[1],x[2],x[3]) #Goes trough a tuble in the list and creates an Email Class with the infromation from the tuble
            EM_list.append(EM) #Adds the email to the EM_list

        conn.close() #Closes the connection to the database
        return EM_list #Returns the EM_list

    def find_by_ID(id):
        conn = sqlite3.connect('dbwoddenlegs.db') #Connects to the database 
        c = conn.cursor()#Creates a cursor to iterate trough the SQL Queries
        c.execute( #Exectues a query to find an email with a specefik id
            "SELECT * FROM Email Where id= ?",(id,)
            )
        rows = c.fetchall() #Creates a list of tubles (tubles is a list of strings), we are only expecting one tuble 
        EM = EmailML.Email(rows[0][0], rows[0][1], rows[0][2], rows[0][3]) #Creates an email object from the information in the tuble from rows
        conn.close() #Closes the connection to the database
        return EM    #Returns EM 

    def update_on_id(id, path, identifier, id_rawData): #Updates and Email in the database
        conn = sqlite3.connect('dbwoddenlegs.db') #Connects to the database
        c = conn.cursor()#Creates a cursor to iterate trough the SQL Queries
        c.execute("""UPDATE Email SET path= ?, identifier = ?, id_rawData= ? WHERE id= ?;""",(path, identifier, id_rawData,id,)) #updates the values in Email in the database
        conn.commit() #Commits the query to the database
        conn.close()  #Closes the connection to the database
