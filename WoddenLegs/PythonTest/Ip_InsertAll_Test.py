import unittest
import DB_Ip

class Ip_Insert_All_Test(unittest.TestCase):
    def test_Insert_All_DB_Ip(self):
        DB_Ip.DB_Ip.insert_querry_all("12","33333","77")

if __name__ == '__main__':
    unittest.main()

    

