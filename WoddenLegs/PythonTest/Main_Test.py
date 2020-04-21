import unittest
from ControlLayer.Main2 import *
from ModelLayer.Identifier import *
from ModelLayer.MatchedIdentifier import *

class Test_Main_Test(unittest.TestCase):
    def test_A(self):
        listMain = ['C:\\Users\\PhilipBraarup\\Desktop\\4thSemProject\\WoddenLegs\WoddenLegs\\ControlLayer\\TempPDFHolder\\1.pdf', 
                    'C:\\Users\\PhilipBraarup\\Desktop\\4thSemProject\\WoddenLegs\\WoddenLegs\\ControlLayer\\TempPDFHolder\\2.pdf',
                    'C:\\Users\\PhilipBraarup\\Desktop\\4thSemProject\\WoddenLegs\\WoddenLegs\\ControlLayer\\TempPDFHolder\\3.pdf']
        mainClass = Main2()
        mainClass.main()
        self.assertEqual(1,1)

    #def test_B(self):
    #    identifiers = [Identifier('abc@gmail.com', 'email', '123', 5, 1), 
    #                   Identifier('abc@gmail.com', 'email', '123', 5, 2), #Test same email same file. Should not match.
    #                   Identifier('abc@gmail.com', 'email', '456', 5, 3), #Test same email different file. Should match.
    #                   Identifier('jkl@gmail.com', 'email', '123', 5, 4), #Different email, same file. Should not match.
    #                   Identifier('abc@gmail.com', 'email', '456', 5, 5), 
    #                   Identifier('abc@gmail.com', 'email', '789', 5, 6),
    #                   Identifier('rst@gmail.com', 'email', '456', 5, 7),
    #                   Identifier('uvw@gmail.com', 'email', '789', 5, 8)]
    #    mainClass = Main2()
    #    results = mainClass.MatchIdentifiers(identifiers)

    #    for result in results:
    #        print(result.name + "\nOccurences: " + str(result.occurences) + "\nID: " + str(result.id))
    #    self.assertEqual(1,1)

if __name__ == '__main__':
    unittest.main()
