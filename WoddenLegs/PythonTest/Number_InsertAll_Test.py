import unittest
import DB_Number

class Email_Insert_All_Test(unittest.TestCase):#for manual testing only
    def test_Insert_All_DB_Email(self):
        DB_Number.DB_Number.insert_querry_all("1","33","7")

if __name__ == '__main__':
    unittest.main()

    

