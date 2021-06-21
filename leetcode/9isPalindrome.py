# Definition for singly-linked list.
import unittest
import math

class TestClass(unittest.TestCase):
    def isPalindrome(self, x: int) -> bool:
        if(x<0):
            return False
        rx = self.reverseNum(x)
        return rx == x
    def reverseNum(self,x: int):
        rx = 0
        while x>=1:
            pop = x % 10
            x/=10
            rx = rx*10 + int(pop)
        return rx
    def isPalindrome1(self, x: int) -> bool:
        if(x<0):
            return False
        return str(x)[::-1] == str(x)

                

    def setUp(self):
        self.run = self.isPalindrome1

    def test_shuffle1(self):
        s = 123
        type = self.run(s)
        self.assertEqual(False, type)

    def test_shuffle2(self):
        s = -123
        type = self.run(s)
        self.assertEqual(False, type)

    def test_shuffle3(self):
        s = 120
        type = self.run(s)
        self.assertEqual(False, type)

    def test_shuffle4(self):
        s = 121
        type = self.run(s)
        self.assertEqual(True, type)

    def test_shuffle5(self):
        s = 1221
        type = self.run(s)
        self.assertEqual(True, type)

if __name__ == '__main__':
    unittest.main()