# Definition for singly-linked list.
import unittest
import math

class TestClass(unittest.TestCase):
    def romanToInt(self, s: str) -> int:
        s+="I"
        mapping = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        count = 0
        temp = mapping[s[0]]
        for x in s[1:]:
            if(temp<mapping[x]):
                count-=temp
            else:
                count+=temp
            # print(temp,mapping[x],count)
            temp = mapping[x]
        return count

                

    def setUp(self):
        self.run = self.romanToInt

    def test_shuffle1(self):
        s = "III"
        type = self.run(s)
        self.assertEqual(3, type)

    def test_shuffle2(self):
        s = "IV"
        type = self.run(s)
        self.assertEqual(4, type)

    def test_shuffle3(self):
        s = "IX"
        type = self.run(s)
        self.assertEqual(9, type)

    def test_shuffle4(self):
        s = "LVIII"
        type = self.run(s)
        self.assertEqual(58, type)

    def test_shuffle5(self):
        s = "MCMXCIV"
        type = self.run(s)
        self.assertEqual(1994, type)

if __name__ == '__main__':
    unittest.main()