import unittest
from RegexChecker import *

class Test_RegexTest(unittest.TestCase):
    
    def test_A(self):
        input = "This is an email ole.wedel@gmail.com k abc123@hotmail.co.uk"
        self.assertEqual(RegexChecker.checkMail(input), ['ole.wedel@gmail.com', 'abc123@hotmail.co.uk'])

    def test_B(self):
        tests = """
        207.142.131.235
        192.168.1.1
        1::
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
        '207.142.131.235',
        '192.168.1.1',
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
        self.assertEqual(RegexChecker.findIP(tests), expectedOutput)

    def test_C(self):
        input = " this is a hpone number +45 25 31 47 89 here is one more +4523456789 here is another 4553853848 the fourth one is this 91 55 98 89 and tis be the last one 23456789"
        expectedOutput = [
            '+45 25 31 47 89',
            '+4523456789',
            '4553853848',
            '91 55 98 85',
            '23456789',
]
        self.assertEqual(RegexChecker.checkPhone(input), expectedOutput)

    

if __name__ == '__main__':
    unittest.main()
