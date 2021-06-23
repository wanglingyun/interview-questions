# 递减元素使数组呈锯齿状
import unittest
import math
from typing import List
    #5 1 6 6 7 8 1 7 8
    #5 + 6 + 2 + 0 + 2 = 15
    #+ 0 + 1 + 8 + 7 + = 16

class Solution(unittest.TestCase):
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        # n 表示奇数位累加值 m 表示偶数位累加值
        n,m = 0,0
        #处理第一位
        n = self.append(-1,nums[0] - nums[1],n)
        print(0,-1,nums[0] - nums[1],n,m)
        for i in range(1,len(nums)-1) :
            if i%2 == 0:
                #处理奇数位
                n = self.append(nums[i] - nums[i-1],nums[i] - nums[i+1],n)
            else:
                #处理偶数位
                m = self.append(nums[i] - nums[i-1],nums[i] - nums[i+1],m)
            print(i,nums[i] - nums[i-1],nums[i] - nums[i+1],n,m)

        #最后一位
        if len(nums)%2 == 0:
            # 若为0 累加到偶数位
            m = self.append(nums[len(nums)-1] - nums[len(nums)-2],-1,m)
        else:
            # 累加到奇数位
            n = self.append(nums[len(nums)-1] - nums[len(nums)-2],-1,n)

        print(len(nums)-1,nums[len(nums)-1] - nums[len(nums)-2],-1,n,m)
        if n > m :
            return m
        return n

    def append(self,t1,t2,x) -> int:
        if t1 >= 0 and t2 >= 0:
            x+=1
            if t1 - t2 > 0:
                x+=t1
            else:
                x+=t2
        elif t1 >= 0:
            x+=1
            x+=t1
        elif t2 >= 0 :
            x+=1
            x+=t2

        return x
        

    def setUp(self):
        self.run = self.movesToMakeZigzag

    def test_shuffle1(self):
        type = self.run([1,2,3])
        self.assertEqual(2, type)
    def test_shuffle2(self):
        type = self.run([9,6,1,6,2])
        self.assertEqual(4, type)
    def test_shuffle3(self):
        type = self.run([5, 1, 6, 6, 7, 8, 1, 7, 8])
        self.assertEqual(15, type)
    def test_shuffle4(self):
        type = self.run([1])
        self.assertEqual(0, type)

if __name__ == '__main__':
    unittest.main()