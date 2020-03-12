import unittest
import DB_Number

class Test_Ip_Update_on_id(unittest.TestCase):
    def test_A(self):
        DB_Number.DB_Number.update_on_id("1","1","1","1")

if __name__ == '__main__':
    unittest.main()
