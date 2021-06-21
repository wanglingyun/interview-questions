# Definition for singly-linked list.
import unittest
import math

class TestClass(unittest.TestCase):
    def longestPalindrome(self, s: str) -> str:
        
        return prefix

                

    def setUp(self):
        self.run = self.longestCommonPrefix

    def test_shuffle1(self):
        s = ["flower","flow","flight"]
        type = self.run(s)
        self.assertEqual("fl", type)

    def test_shuffle2(self):
        s = ["dog","racecar","car"]
        type = self.run(s)
        self.assertEqual("", type)

    def test_shuffle3(self):
        s = []
        type = self.run(s)
        self.assertEqual("", type)

    def test_shuffle4(self):
        s = ["flower","flow","flight","ftrea"]
        type = self.run(s)
        self.assertEqual("f", type)

    def test_shuffle5(self):
        s = ["a","ac"]
        type = self.run(s)
        self.assertEqual("a", type)

    def test_shuffle5(self):
        s = ["aa","a"]
        type = self.run(s)
        self.assertEqual("a", type)


if __name__ == '__main__':
    unittest.main()