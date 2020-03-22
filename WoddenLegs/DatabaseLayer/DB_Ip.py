import IpML
import DB_Connection
import sqlite3
class DB_Ip(object): #Interacts withs the ip table in the database, insert all, select all, find by id, update on id

    DB_Connection.DB_Connection.db_check() #Calls the DB check method in DB_Connection
    
    def insert_querry_all(path,identifier,id_rawData): #Inserts all data into the Ip table in the database
        conn = sqlite3.connect('dbwoddenlegs.db') #Connects to the database
        c = conn.cursor()#Creates a cursor to iterate trough the SQL Queries
        c.execute( #Executes an insert querry into the Ip table in the database
          """ INSERT INTO Ip (path,identifier,id_rawdata) VALUES (?,?,?);
            """, (path,identifier,id_rawData))
        conn.commit() #Commits the querry to the database
        conn.close() #Closes the connection to the database

    def find_all(): #Creates a list of all Ips from in the database
        conn = sqlite3.connect('dbwoddenlegs.db') #Connects to the database
        c = conn.cursor()#Creates a cursor to iterate trough the SQL Queries
        c.execute( #Executes a select all data in the ip table query
            "Select * From Ip"
            )
        rows = c.fetchall() #Creates a list of tubles (tubles is a list of strings) from the querry resultset called rows
        ip_list = [] #Creates an empty list called ip_list
        for x in rows: #Iterates trough the list of tubles
            ip = IpML.Ip(x[0],x[1],x[2],x[3])#Goes trough a tuble in the list and creates an Ip Class with the infromation from the tuble
            ip_list.append(ip) #Adds the ip to the ip_list

        conn.close() #Closes the connection to the database
        return ip_list #Returns the Ip_list

        

    def find_by_ID(id):# Finds an ip from its id 
        conn = sqlite3.connect('dbwoddenlegs.db') #Connects to the database
        c = conn.cursor()#Creates a cursor to iterate trough the SQL Queries
        c.execute( #Executes a select statement to find and ip using its id
            "SELECT * FROM Ip Where id= ?",(id,)
            )
        rows = c.fetchall()#Creates a list of tubles (tubles is a list of strings) from the querry resultset called rows, We are only expecting one tuble
        ip = IpML.Ip(rows[0][0], rows[0][1], rows[0][2], rows[0][3]) #Creates an ip object from the information in the tuble from rows
        conn.close() #Closes the connection to the database 
        return ip #Returns the ip
    
    def update_on_id(id, path, identifier, id_rawData): #Updates an ip in the database on its id
        conn = sqlite3.connect('dbwoddenlegs.db')#Connects to the database
        c = conn.cursor() #Creates a cursor to iterate trough the SQL Queries
        c.execute("""UPDATE Ip SET path= ?, identifier = ?, id_rawData= ? WHERE id= ?;""",(path, identifier, id_rawData,id,))#Executes an update querry in Ip from its id
        conn.commit() #Commits querry to the database
        conn.close() #Closes connection to the database 

