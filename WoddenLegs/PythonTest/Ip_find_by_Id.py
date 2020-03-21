import unittest
import DB_Ip

class Test_ip_FindByID(unittest.TestCase):#for manual testing only
    def test_find_by_id(self):
        ip = DB_Ip.DB_Ip.find_by_ID(11)
        print(ip.identifier)
if __name__ == '__main__':
    unittest.main()
