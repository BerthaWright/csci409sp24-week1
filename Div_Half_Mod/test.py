### Program

''' Bertha Wright: Lab Modules and Testing
Date: 02-Oct-2022
Assignment: Week 06
Pseudocode: None Needed
'''

### Main Program


import unittest


def division():
    halfnum = float(input("Please type the number you want halved here: "))  # input = 4
    return halfnum // 2


def double():
    dub_num = float(input("Please type the number you want doubled here: "))  # input = 4
    return dub_num * 2


class test_div_half(unittest.TestCase):
    def test_div(self):
        self.assertEqual(division(), 2)

    def test_half(self):
        self.assertEqual(double(), 8)


if __name__ == '__main__':
    unittest.main()
