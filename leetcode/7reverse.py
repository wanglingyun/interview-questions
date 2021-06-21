# Definition for singly-linked list.
import unittest
import math

class TestClass(unittest.TestCase):
    def reverse(self, x: int) -> int:
        if not -2**31<x<2**31-1:
            return 0
        flag = 1
        if x < 0:
            flag = -1
            x = 0-x
        rx = self.reverseNum(x)
        if not -2**31<rx<2**31-1:
            return 0
        if flag == -1:
            return -rx
        return rx
    
    def reverseNum(self,x: int):
        rx = 0
        print("======1",x)
        while x>=1:
            pop = x % 10
            print("======2",pop)
            x/=10
            rx = rx*10 + int(pop)
        print("======3",rx)
        return rx

                

    def setUp(self):
        self.run = self.reverse

    def test_shuffle1(self):
        s = 123
        type = self.run(s)
        self.assertEqual(321, type)

    def test_shuffle2(self):
        s = -123
        type = self.run(s)
        self.assertEqual(-321, type)

    def test_shuffle3(self):
        s = 120
        type = self.run(s)
        self.assertEqual(21, type)

    def test_shuffle4(self):
        s = 2147483647
        type = self.run(s)
        self.assertEqual(0, type)

    def test_shuffle5(self):
        s = -2147483648
        type = self.run(s)
        self.assertEqual(0, type)
    
    def test_shuffle6(self):
        s =  2063847412
        type = self.run(s)
        self.assertEqual(2147483602, type)

    def test_shuffle7(self):
        s =  1
        type = self.run(s)
        self.assertEqual(1, type)

if __name__ == '__main__':
    unittest.main()