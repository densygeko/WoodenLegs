import unittest
from ControlLayer.MailChecker import *
from ControlLayer.IPChecker import *

class Test_RegexTest(unittest.TestCase):
    
    def test_A(self):
        
        input = "This is an email ole.wedel@gmail.com k abc123@hotmail.co.uk"
        self.assertEqual(MailChecker.checkMail(input), ['ole.wedel@gmail.com', 'abc123@hotmail.co.uk'])

    def test_B(self):
        tests = """1::
        1:2:3:4:5:6:7::
        1::8
        1:2:3:4:5:6::8
        1:2:3:4:5:6::8
        1::7:8
        1:2:3:4:5::7:8
        1:2:3:4:5::8
        1::6:7:8
        1:2:3:4::6:7:8
        1:2:3:4::8
        1::5:6:7:8
        1:2:3::5:6:7:8
        1:2:3::8
        1::4:5:6:7:8
        1:2::4:5:6:7:8
        1:2::8
        1::3:4:5:6:7:8
        1::3:4:5:6:7:8
        1::8
        ::2:3:4:5:6:7:8
        ::2:3:4:5:6:7:8
        ::8
        ::
        fe80::7:8%eth0
        fe80::7:8%1
        ::255.255.255.255
        ::ffff:255.255.255.255
        ::ffff:0:255.255.255.255
        2001:db8:3:4::192.0.2.33
        64:ff9b::192.0.2.33
        hej"""

        expectedOutput = [
        '1::',
        '1:2:3:4:5:6:7::',
        '1::8',
        '1:2:3:4:5:6::8',
        '1:2:3:4:5:6::8',
        '1::7:8',
        '1:2:3:4:5::7:8',
        '1:2:3:4:5::8',
        '1::6:7:8',
        '1:2:3:4::6:7:8',
        '1:2:3:4::8',
        '1::5:6:7:8',
        '1:2:3::5:6:7:8',
        '1:2:3::8',
        '1::4:5:6:7:8',
        '1:2::4:5:6:7:8',
        '1:2::8',
        '1::3:4:5:6:7:8',
        '1::3:4:5:6:7:8',
        '1::8',
        '::2:3:4:5:6:7:8',
        '::2:3:4:5:6:7:8',
        '::8',
        '::',
        'fe80::7:8%eth0',
        'fe80::7:8%1',
        '::255.255.255.255',
        '::ffff:255.255.255.255',
        '::ffff:0:255.255.255.255',
        '2001:db8:3:4::192.0.2.33',
        '64:ff9b::192.0.2.33',
]
        self.assertEqual(IPChecker.findIP(tests), expectedOutput)

if __name__ == '__main__':
    unittest.main()
