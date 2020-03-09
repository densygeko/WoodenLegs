import unittest
import DB_RawData
import DB_BlacklistType
import sqlite3

class Test_DB_Test(unittest.TestCase):
    def test_querry_RawData(self):
        DB_RawData.DB_RawData.insert_querry_all("5","2","1")

class Test_DB_insert_Blacklist_type_test(unittest.TestCase):
    def test_querry_RawData(self):
        DB_BlacklistType.BlacklistType.insert_querry_all("0","0","0")
if __name__ == '__main__':
    unittest.main()
