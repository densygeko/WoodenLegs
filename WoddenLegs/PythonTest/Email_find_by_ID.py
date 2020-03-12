import unittest
import DB_Email

class Test_Email_FindByID(unittest.TestCase):
    def test_find_by_id(self):
        print(DB_Email.DB_Email.find_by_ID(11))
if __name__ == '__main__':
    unittest.main()
