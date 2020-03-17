import unittest
import DB_Number

class Test_FindAll(unittest.TestCase):
    def test_FindAll(self):
       testnumber = DB_Number.DB_Number.find_all()
       for x in testnumber:
           print(x.identifier)
if __name__ == '__main__':
    unittest.main()