import unittest
import DB_Email

class Email_Insert_All_Test(unittest.TestCase):
    def test_Insert_All_DB_Email(self):
        DB_Email.DB_Email.insert_querry_all("1","33","7")

if __name__ == '__main__':
    unittest.main()

    

