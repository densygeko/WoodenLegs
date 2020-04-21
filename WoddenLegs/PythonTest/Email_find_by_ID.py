import unittest
import DB_Email

class Test_Email_FindByID(unittest.TestCase): #For manual testing only
    def test_find_by_id(self):
        email = DB_Email.DB_Email.find_by_ID(11)
        print(email.identifier)
            

if __name__ == '__main__':
    unittest.main()
