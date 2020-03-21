import unittest
import DB_RawData
import DB_BlacklistKeyword

class Test_test_1(unittest.TestCase):

    #test for manual testing of the database

    def test_A(self):
        DB_BlacklistKeyword.DB_BlacklistKeyword.insert_into_blacklist("2","1")

    def test_b(self):
        DB_BlacklistKeyword.DB_BlacklistKeyword.update_on_id("1","30","2")
    
    def test_c(slef):
        print(DB_BlacklistKeyword.DB_BlacklistKeyword.select_on_id("1"))

    def test_c(slef):
        DB_BlacklistKeyword.DB_BlacklistKeyword.insert_into_blacklist("2","2")
        DB_BlacklistKeyword.DB_BlacklistKeyword.delete_from_BlacklistKeyword("2")
    def test_d(slef):
        print(DB_BlacklistKeyword.DB_BlacklistKeyword.select_all_Blacklist_keyword())

if __name__ == '__main__':
    unittest.main()
