# Definition for singly-linked list.
import unittest
import math

class TestClass(unittest.TestCase):
    def longestCommonPrefix(self, strs) -> str:
        prefix = "" if len(strs) == 0 else strs[0]
        con = 1
        while prefix!="" and con<len(strs):
            tempB = True
            index = 0
            x = strs[con]
            # print(con,x)
            prefix = prefix[:len(x)]
            while tempB and index <len(x) and index < len(prefix):
                # print("while:",index,prefix[index])
                if prefix[index] != x[index]:
                    prefix = prefix[:index]
                    tempB = False
                index+=1
            con+=1
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