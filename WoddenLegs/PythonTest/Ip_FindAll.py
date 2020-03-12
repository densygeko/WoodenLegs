import unittest
import DB_Ip
class Test_FindAll(unittest.TestCase):
    def test_FindAll(self):
       print(DB_Ip.DB_Ip.find_all())

if __name__ == '__main__':
    unittest.main()