import unittest
import DB_Number

class Test_Email_FindByID(unittest.TestCase):
    def test_find_by_id(self):
        number = DB_Number.DB_Number.find_by_ID(11)
        print(number.identifier)
if __name__ == '__main__':
    unittest.main()
