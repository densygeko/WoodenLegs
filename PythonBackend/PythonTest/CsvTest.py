import unittest
from CsvReader import *

class Test_CsvTest(unittest.TestCase):
    def test_A(self):
        csvRead = CsvReader()
        csvrows = csvRead.ReadFile('C:\\Users\\PhilipBraarup\\temp\\2800-41492-04159-20\\ullam illum\\nesciunt pariatur\\mollitia atque\\id.csv')
        for row in csvrows:
            print(row)
        self.assertEqual(1,1)

if __name__ == '__main__':
    unittest.main()
