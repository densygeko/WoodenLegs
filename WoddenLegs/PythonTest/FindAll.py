import unittest
import DB_RawData
class Test_FindAll(unittest.TestCase):
    def test_FindAll(self):
       print(DB_RawData.DB_RawData.Find_all())

if __name__ == '__main__':
    unittest.main()
