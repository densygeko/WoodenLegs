import unittest
import DB_Email
class Test_FindAll(unittest.TestCase):
    def test_FindAll(self):
       print(DB_Email.DB_Email.find_all())

if __name__ == '__main__':
    unittest.main()