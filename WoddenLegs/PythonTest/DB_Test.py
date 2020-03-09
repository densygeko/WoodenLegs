import unittest
import DB_RawData
import DB_BlacklistType
import sqlite3

class IDB_Test(unittest.TestCase):

    def Insert_All_DB_RawData_test(self):
        DB_RawData.DB_RawData.insert_querry_all("5","2","1","8")
        

    def Delete_By_ID_RawData_test(self):
        DB_RawData.DB_RawData.Delete_by_ID("10")
        

class Test_DB_insert_Blacklist_type_test(unittest.TestCase):
    def test_querry_RawData(self):
        DB_BlacklistType.BlacklistType.update_ip_false()
        print("true")

class Test_test_1(unittest.TestCase):
    def test_A(self):
        print(DB_BlacklistType.BlacklistType.get_BleckliostType())



if __name__ == '__main__':
    unittest.main()

    

