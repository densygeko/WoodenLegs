import unittest
import DB_RawData

class Test_FindByID(unittest.TestCase): #for manual testing only
    def test_find_by_id(self):
        rawData = DB_RawData.DB_RawData.find_by_ID(11)
        print(rawData.pageNumber)        
if __name__ == '__main__':
    unittest.main()
