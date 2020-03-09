import unittest
import DB_RawData

class IDB_Test(unittest.TestCase):

    def Insert_All_DB_RawData_test(self):
        DB_RawData.DB_RawData.insert_querry_all("5","2","1","8")
        

    def Delete_By_ID_RawData_test(self):
        DB_RawData.DB_RawData.Delete_by_ID("10")
        

if __name__ == '__main__':
    unittest.main()

    

