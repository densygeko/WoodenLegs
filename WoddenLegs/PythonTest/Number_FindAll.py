import unittest
import DB_Number

class Test_FindAll(unittest.TestCase):
    def test_FindAll(self):
       print(DB_Number.DB_Number.find_all())

if __name__ == '__main__':
    unittest.main()