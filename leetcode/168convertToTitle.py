# Definition for singly-linked list.
import unittest
import math

class TestClass(unittest.TestCase):
    def convertToTitle(self, n: int) -> str:
        if(n<=0):
            return ""
        st = ""
        while n!=0:
            n-=1
            st += chr((n)%26+65)
            n = n//26
            print("test:",n,st)
        print(n,st)
        return st[::-1]


                

    def setUp(self):
        self.run = self.convertToTitle

    def test_shuffle1(self):
        s = 1
        type = self.run(s)
        self.assertEqual("A", type)

    def test_shuffle2(self):
        s = -123
        type = self.run(s)
        self.assertEqual("", type)

    def test_shuffle3(self):
        s = 701
        type = self.run(s)
        self.assertEqual("ZY", type)

    # def test_shuffle4(self):
    #     s = 121
    #     type = self.run(s)
    #     self.assertEqual(True, type)

    # def test_shuffle5(self):
    #     s = 1221
    #     type = self.run(s)
    #     self.assertEqual(True, type)

if __name__ == '__main__':
    unittest.main()