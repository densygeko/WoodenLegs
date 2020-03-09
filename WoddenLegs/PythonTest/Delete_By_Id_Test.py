import unittest
import DB_RawData

class Test_Delete_By_Id_Test(unittest.TestCase):
    def test_Delete_ById(self):
        DB_RawData.DB_RawData.Delete_by_ID(10)
if __name__ == '__main__':
    unittest.main()
