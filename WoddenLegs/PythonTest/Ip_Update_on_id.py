import unittest
import DB_Ip

class Test_Ip_Update_on_id(unittest.TestCase): #for manual testing only
    def test_A(self):
        DB_Ip.DB_Ip.update_on_id("1","1","1","1")

if __name__ == '__main__':
    unittest.main()
