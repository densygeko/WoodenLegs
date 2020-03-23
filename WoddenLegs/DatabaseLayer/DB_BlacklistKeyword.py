import sqlite3
import DB_Connection
import BlacklistKeyword

class DB_BlacklistKeyword(object):
    """Interacts withs the BlacklistKeyword  tabe in the database, isert into, select all, update on id, select on id, delete on id"""
    DB_Connection.DB_Connection.db_check()

    def insert_into_blacklist(keyword, id_blacklistType):
        conn = sqlite3.connect('dbwoddenlegs.db') #Connet with the database
        c = conn.cursor() #Creates a cursoer to iterate trough the SQL queries
        c.execute( #Execute a qurie that insert a Keyword into the table
            """ INSERT INTO BlacklistKeyWord (keyword,id_blacklistType) VALUES (?,?);
            """,(keyword, id_blacklistType)) #Query that execute insert stament into BlacklistKeyword table
        conn.commit() #commit the query
        conn.close() #close the connettion to the Database

    def select_all_Blacklist_keyword():
        conn = sqlite3.connect('dbwoddenlegs.db') #connet with the database
        c = conn.cursor() #Creates a cursoer to iterate trough the SQL queries
        c.execute(""" Select * From BlacklistKeyWord""") #Query that selct all the Blacklistkeywords from the blacklistkeyword table
        row = c.fetchall() #Creates a list of tubles (tubles is a list of strings) from the querry resultset called rows
        BL_word = [] # makes a list
        for x in row: #Interates tho the list of tubles
            BLKW = BlacklistKeyword.BlacklistKeyword(x[0],x[1],x[2]) #creats a BlacklistKeyword with the information from the tupales
            BL_word.append(BLKW) #add the created BlacklistKeyword to the list BL_word
        conn.close() #close the connettion to the Database
        return BL_word # retrnun a list of BlacklistKeywords

    def update_on_id(id, keyword, ID_blacklistType):
        conn = sqlite3.connect('dbwoddenlegs.db') #connet with the database
        c = conn.cursor() #Creates a cursoer to iterate trough the SQL queries
        c.execute("""UPDATE BlacklistKeyWord SET keyWord= ?, id_BlackListType = ? WHERE id= ?;""",(keyword, ID_blacklistType, id,)) #query that update the a blacklistkeyword on id
        conn.commit() #Commit the query
        conn.close()#Close the connettion to the Database

    def select_on_id(id):
        conn = sqlite3.connect('dbwoddenlegs.db') #Connet with the database
        c = conn.cursor() #Creates a cursoer to iterate trough the SQL queries
        c.execute(""" select * from BlacklistKeyWord where id = ? """,(id,))
        row = c.fetchall() #Creates a list of tubles (tubles is a list of strings) from the querry resultset called rows
        BLKW = BlacklistKeyword.BlacklistKeyword(row[0][0],row[0][1],row[0][2]) #makes a blacklistkeyword with the data form the Row tuple
        conn.close() #Close the connettion to the Database
        return BLKW #return the blacklistkeyword

    def delete_from_BlacklistKeyword(id):
        conn = sqlite3.connect('dbwoddenlegs.db') #connet with the database
        c = conn.cursor() #Creates a cursoer to iterate trough the SQL queries
        c.execute("""DELETE FROM BlacklistKeyWord WHERE id=?; """,(id)) #Execute the a query Delete a blacklistKeyword with an id som arg
        conn.commit() #commit the query
        conn.close() #close the connettion to the Database