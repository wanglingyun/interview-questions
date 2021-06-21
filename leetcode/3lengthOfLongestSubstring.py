# Definition for singly-linked list.
import unittest
import math
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class TestClass(unittest.TestCase):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # l = 0
        # for x in range(len(s)):
        #     temp = ""
        #     for t in s[x:]:
        #         print(t,temp)
        #         if t in temp:
        #             l = l if l>=len(temp) else len(temp)
        #             print(l,len(temp),temp)
        #             temp = ""
        #         else:
        #             temp = temp+t
        #     l = l if l>=len(temp) else len(temp)
        # return l  
        l = 0
        temp = ""
        for t in s:
            print(t,temp)
            if t in temp:
                l = l if l>=len(temp) else len(temp)
                print("print temp:",l,len(temp),temp)
                index=temp.index(t)
                temp=temp[index+1:]
            temp = temp+t
            # print("temp:",temp)
        l = l if l>=len(temp) else len(temp)
        return l
        

                

    def setUp(self):
        self.run = self.lengthOfLongestSubstring

    def test_shuffle1(self):
        s = "abcabcbb"
        type = self.run(s)
        self.assertEqual(3, type)

    def test_shuffle2(self):
        s = "bbbbb"
        type = self.run(s)
        self.assertEqual(1, type)

    def test_shuffle3(self):
        s = "pwwkew"
        type = self.run(s)
        self.assertEqual(3, type)

    def test_shuffle4(self):
        s = "aab"
        type = self.run(s)
        self.assertEqual(2, type)

    def test_shuffle5(self):
        s = ""
        type = self.run(s)
        self.assertEqual(0, type)
    
    def test_shuffle6(self):
        s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"*10 +"ABCD"
        type = self.run(s)
        self.assertEqual(len("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"), type)

if __name__ == '__main__':
    unittest.main()