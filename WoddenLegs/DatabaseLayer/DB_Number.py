import Number
import DB_Connection
import sqlite3
class DB_Number(object): # Interacts with the Number table in the database, Insert all, select all, find by id, update by id

    DB_Connection.DB_Connection.db_check() #Calls the DB check method in DB_Connection
    
    def insert_querry_all(path,identifier,id_rawData): # Insersts all data into the Number table in the database
        conn = sqlite3.connect('dbwoddenlegs.db') #Connects to the database
        c = conn.cursor()#Creates a cursor to iterate trough the SQL Queries
        c.execute(#Executes an insert querry to Number table in the database
          """ INSERT INTO Number (path,identifier,id_rawdata) VALUES (?,?,?);
            """, (path,identifier,id_rawData))
        conn.commit()#Commits querry to the database
        conn.close() #Closes the connection to the database

    def find_all(): #Finds all data from the number table in the database
        conn = sqlite3.connect('dbwoddenlegs.db') #Connects to the database
        c = conn.cursor()#Creates a cursor to iterate trough the SQL Queries
        c.execute( #Exectues a select statement for all data in the Number table
            "Select * From Number"
            )
        NM_list = [] #Creates an empty list
        rows = c.fetchall() #Creates a list of tubles (tubles is a list of strings) from the querry resultset called rows
        for x in rows: #Iterates trough the list of tubles
            NM = Number.Number(x[0],x[1],x[2],x[3])#Goes trough a tuble in the list and creates an Ip Class with the infromation from the tuble
            NM_list.append(NM)#Adds the numbers to the NM_list

        conn.close() #Closes the connection to the database
        return NM_list #Returns the NM_list

    def find_by_ID(id): #finds a number from its id
        conn = sqlite3.connect('dbwoddenlegs.db') #Connects to the database
        c = conn.cursor()#Creates a cursor to iterate trough the SQL Queries
        c.execute( #executes a select on Number from a numbers id
            "SELECT * FROM Number Where id= ?",(id,)
            )
        rows = c.fetchall()#Creates a list of tubles (tubles is a list of strings) from the querry resultset called rows, we only expect one tuble here
        NM = Number.Number(rows[0][0], rows[0][1], rows[0][2], rows[0][3]) #Creates a Number object from the information in the tuble from rows
        conn.close() #Closes the connection to the database
        return NM  #Returns NM

    def update_on_id(id, path, identifier, id_rawData): #Update values in the Number table
        conn = sqlite3.connect('dbwoddenlegs.db') #Connects to the database 
        c = conn.cursor() #Creates a cursor to iterate trough the SQL Queries
        c.execute("""UPDATE Number SET path= ?, identifier = ?, id_rawData= ? WHERE id= ?;""",(path, identifier, id_rawData,id,)) #Executes an update statment in the Number table
        conn.commit() #Commits the querry to the database
        conn.close() #Closes the connection to the database
