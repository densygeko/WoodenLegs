import unittest
import DB_Ip

class Test_ip_FindByID(unittest.TestCase):
    def test_find_by_id(self):
        print(DB_Ip.DB_Ip.find_by_ID(11))
if __name__ == '__main__':
    unittest.main()
