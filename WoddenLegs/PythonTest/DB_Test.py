import unittest
import DB_RawData

class Test_DB_Test(unittest.TestCase):
    def test_querry_RawData(self):
        DB_RawData.DB_RawData.insert_querry_all('values', 'path', 'fileType')

if __name__ == '__main__':
    unittest.main()
