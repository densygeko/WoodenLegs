import unittest
import DB_Email
class Test_FindAll(unittest.TestCase):
    def test_FindAll(self):
        testEmail = DB_Email.DB_Email.find_all()
        for x in testEmail:
            print(x.identifier)
if __name__ == '__main__':
    unittest.main()