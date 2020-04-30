import unittest
from ControlLayer.ImgReader import *


class Test_ImgReadTest(unittest.TestCase):
    def test_A(self):
        imRead = ImgReader()
        result = imRead.ReadFile('Image10.png')
        self.assertEqual(bool(result), True) #Check if result contained text

if __name__ == '__main__':
    unittest.main()
