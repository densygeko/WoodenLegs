import unittest
from ControlLayer.Main2 import *
class Test_Main_Test(unittest.TestCase):
    def test_A(self):
        listMain = ["C:\\Users\Scyras\Documents\GitHub\WoddenLegs\WoddenLegs\ControlLayer\TempPDFHolder\report.pdf", "C:\\Users\Scyras\Documents\GitHub\WoddenLegs\WoddenLegs\ControlLayer\TempPDFHolder\OCRTestPDF.pdf"]
        Main2.main()
        self.assertEqual(1,1)

if __name__ == '__main__':
    unittest.main()
