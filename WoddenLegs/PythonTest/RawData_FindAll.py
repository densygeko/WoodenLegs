import unittest
import DB_RawData
class Test_FindAll(unittest.TestCase):#for manual testing only
    def test_FindAll(self):
        tabber = DB_RawData.DB_RawData.find_all()
        for x in tabber:
            print(x.filePath)
       

if __name__ == '__main__':
    unittest.main()
