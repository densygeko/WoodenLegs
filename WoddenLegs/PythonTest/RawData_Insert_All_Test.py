import unittest
import DB_RawData

class RawData_Insert_All_Test(unittest.TestCase):
    def test_Insert_All_DB_RawData(self):
        DB_RawData.DB_RawData.insert_querry_all("5","2","1","8")

if __name__ == '__main__':
    unittest.main()

    

