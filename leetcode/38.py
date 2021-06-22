# 外观数列
import unittest
import math

class ListNode:
    def __init__(self , num: str, count:int ):
        self.num = num
        self.count = count

class Solution(unittest.TestCase):
    def countAndSay2(self, n: int) -> str:
        startNum = "1"
        # 为1返回初始数字
        if n==1:
            return startNum
        tmp_result = startNum
        # 从2开始迭代 上一次执行的结果是下一次的入参。
        for i in range(2,n+1):
            print(i-1,tmp_result)
            # 将字符串转换为数值列表
            nodes = self.count(tmp_result)
            # 将数值列表 按语义表达出来
            tmp_result = self.say(nodes)
            
        # 返回最后一次结果
        return tmp_result


    def count(self,numCount:str)-> list:
        # 新建一个数组用于存放对象列表
        nodes = []
        for x in numCount:
            endLen = len(nodes)-1
            if len(nodes)==0 or None == nodes[endLen]:
                nodes.append(ListNode(x,1))
            elif nodes[endLen].num == x:
                nodes[endLen].count+=1
            elif nodes[endLen].num != x:
                nodes.append(ListNode(x,1))
        return nodes

    def say(self,nodes:list) -> str:
        numStr = ""
        for n in nodes:
            numStr += str(n.count)
            numStr += n.num
        return numStr

    def countAndSay(self, n: int) -> str:
        startNum = "1"
        # 为1返回初始数字
        if n==1:
            return startNum
        temp_result = self.countAndSay(n-1)
        count = 1
        c = temp_result[0]
        i = 1
        result = ""
        while i < len(temp_result):
            if temp_result[i] != c:
                result += str(count) + c
                c = temp_result[i]
                count = 1
            else:
                count += 1
            i += 1
        result += str(count) + c
        return result

    def setUp(self):
        self.run = self.countAndSay

    def test_shuffle1(self):
        type = self.run(1)
        self.assertEqual("1", type)
    def test_shuffle2(self):
        type = self.run(2)
        self.assertEqual("11", type)
    def test_shuffle3(self):
        type = self.run(3)
        self.assertEqual("21", type)
    def test_shuffle4(self):
        type = self.run(4)
        self.assertEqual("1211", type)
    def test_shuffle5(self):
        type = self.run(5)
        self.assertEqual("111221", type)
    def test_shuffle6(self):
        type = self.run(6)
        self.assertEqual("312211", type)
    def test_shuffle7(self):
        type = self.run(7)
        self.assertEqual("13112221", type)
    def test_shuffle8(self):
        type = self.run(8)
        self.assertEqual("1113213211", type)
    def test_shuffle9(self):
        type = self.run(9)
        self.assertEqual("31131211131221", type)
    def test_shuffle10(self):
        type = self.run(10)
        self.assertEqual("13211311123113112211", type)

if __name__ == '__main__':
    unittest.main()