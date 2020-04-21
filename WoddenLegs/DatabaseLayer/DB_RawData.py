import DB_Connection
import sqlite3
import RawData 
class DB_RawData(object):

    DB_Connection.DB_Connection.db_check()
    
    def insert_querry_all(text,path,fileType,pageNumber):
        conn = sqlite3.connect('dbwoddenlegs.db')
        c = conn.cursor()
        c.execute(
          """ INSERT INTO RawData (text,path,fileType,pageNumber) VALUES (?,?,?,?);
            """, (text,path,fileType,pageNumber))
        conn.commit()
        conn.close()


    def delete_by_ID(id):
        conn = sqlite3.connect('dbwoddenlegs.db')
        c = conn.cursor()
        c.execute(
            "DELETE FROM RawData WHERE id= ?;", (id,)
            )
        conn.commit()
        conn.close()

    def find_by_ID(id):
        conn= sqlite3.connect('dbwoddenlegs.db')
        c = conn.cursor()
        c.execute(
            "SELECT * FROM RawData Where id= ?",(id,)
            )
        rows = c.fetchall()
        RD = RawData.RawData(rows[0][0], rows[0][1], rows[0][2], rows[0][3], rows[0][4])
        conn.close()
        return RD     
        
    def find_all():

        conn = sqlite3.connect('dbwoddenlegs.db')
        c = conn.cursor()
        c.execute(
            "Select * From RawData"
            )
        rows = c.fetchall()
        RD_list = []
        for x in rows:
            RD = RawData.RawData(x[0],x[1],x[2],x[3],x[4])
            RD_list.append(RD)
        conn.close()
        return RD_list
class DB_RawData(object): #Interats with the RawData table in the database, Insert all, delete by id, find by id, find all

    DB_Connection.DB_Connection.db_check() #Calls the DB check method in DB_Connection
    
    def insert_querry_all(text,path,fileType,pageNumber): #Inserts all data in to the RawData table
        conn = sqlite3.connect('dbwoddenlegs.db') #Connects to the database 
        c = conn.cursor() #Creates a cursor to iterate trough the SQL Queries
        c.execute( #Executes insert statement into RawData
          """ INSERT INTO RawData (text,path,fileType,pageNumber) VALUES (?,?,?,?);
            """, (text,path,fileType,pageNumber))
        conn.commit() #Commits to the database
        conn.close() #Closes connection to the database


    def delete_by_ID(id): #Deletes data from the RawData table in the database
        conn = sqlite3.connect('dbwoddenlegs.db') # Connects to the database
        c = conn.cursor()#Creates a cursor to iterate trough the SQL Queries
        c.execute( #Executes delete statement in the RawData table on id
            "DELETE FROM RawData WHERE id= ?;", (id,)
            )
        conn.commit() #Commits query to the database
        conn.close()  #Closes connection to the database

    def find_by_ID(id): #Finds RawData from its id
        conn= sqlite3.connect('dbwoddenlegs.db') #Connects to the database
        c = conn.cursor()#Creates a cursor to iterate trough the SQL Queries
        c.execute( #Executes a select statement in the RawData table from its id
            "SELECT * FROM RawData Where id= ?",(id,)
            )
        rows = c.fetchall() #Creates a list of tubles (tubles is a list of strings) from the querry resultset called rows, we'e only expecting one tuble
        RD = RawData.RawData(rows[0][0], rows[0][1], rows[0][2], rows[0][3], rows[0][4])#Creates a RawData object from the information in the tuble from row
        conn.close() #Closes the connection to the database
        return RD #Returns RD    
        
    def find_all(): #Finds all data in the RawData table
        conn = sqlite3.connect('dbwoddenlegs.db') #Connects to the database
        c = conn.cursor()#Creates a cursor to iterate trough the SQL Quer
        c.execute(#Exectues a Select from query from the RawData table
            "Select * From RawData"
            )
        rows = c.fetchall()#Creates a list of tubles (tubles is a list of strings) from the querry resultset called rows
        RD_list = [] #Creates an empty list called RD_list
        for x in rows: # iterates trough the RD_list
            RD = RawData.RawData(x[0],x[1],x[2],x[3],x[4])#Goes trough a tuble in the list and creates a RawData Class with the infromation from the tuble
            RD_list.append(RD) #Adds the RawData to the RD_List
        conn.close() #closes the connection to the database
        return RD_list #Returns RD_list
