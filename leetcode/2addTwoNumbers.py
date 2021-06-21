# Definition for singly-linked list.
import unittest
import math
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class TestClass(unittest.TestCase):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = ListNode(0)
        nowL3 = l3
        t = 0
        while l1 != None or l2 != None:
            l1 = l1 if l1 != None else ListNode(0)
            l2 = l2 if l2 != None else ListNode(0)
            i = l1.val+l2.val+t
            if i>=10:
                i=i-10
                t=1
            else:
                t=0
            nowL3.next = ListNode(i)
            l1 = l1.next
            l2 = l2.next
            nowL3 = nowL3.next
            print(x,y,nowL3.val)
        if t==1:
            nowL3.next = ListNode(1)
        print(nowL1,nowL2)
        return l3.next
                

    def setUp(self):
        self.run = self.addTwoNumbers

    def test_shuffle1(self):
        l1 = ListNode(3)
        l1.next = ListNode(0)
        l1.next.next = ListNode(7)
        l2 = ListNode(1)
        l2.next = ListNode(2)
        l2.next.next = ListNode(3)
        l3 = ListNode(4)
        l3.next = ListNode(2)
        l3.next.next = ListNode(0)
        l3.next.next.next = ListNode(1)
        type = self.run(l1,l2)
        self.assertEqual(l3.val, type.val)
        self.assertEqual(l3.next.val, type.next.val)
        self.assertEqual(l3.next.next.val, type.next.next.val)
        self.assertEqual(l3.next.next.next.val, type.next.next.next.val)

    def test_shuffle2(self):
        l1 = ListNode(2)
        l1.next = ListNode(4)
        l1.next.next = ListNode(3)
        l2 = ListNode(5)
        l2.next = ListNode(6)
        l2.next.next = ListNode(4)
        l3 = ListNode(7)
        l3.next = ListNode(0)
        l3.next.next = ListNode(8)
        type = self.run(l1,l2)
        self.assertEqual(l3.val, type.val)
        self.assertEqual(l3.next.val, type.next.val)
        self.assertEqual(l3.next.next.val, type.next.next.val)

if __name__ == '__main__':
    unittest.main()