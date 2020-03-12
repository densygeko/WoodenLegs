import unittest
import DB_Email

class Test_Email_Update_on_id(unittest.TestCase):
    def test_A(self):
        DB_Email.DB_Email.update_on_id("1","1","1","1")

if __name__ == '__main__':
    unittest.main()
