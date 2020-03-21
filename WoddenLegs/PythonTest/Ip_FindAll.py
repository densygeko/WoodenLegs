import unittest
import DB_Ip
class Test_FindAll(unittest.TestCase): #for manual testing only
    def test_FindAll(self):
       testIp = DB_Ip.DB_Ip.find_all()
       for x in testIp:
           print(x.identifier)

if __name__ == '__main__':
    unittest.main()