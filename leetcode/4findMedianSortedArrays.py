import unittest
import math
from typing import List

class TestClass(unittest.TestCase):
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        size1 = len(nums1)
        size2 = len(nums2)
        ## 边界值处理
        if size1 == 0 :
            return self.median(nums2)
        elif size2 == 0 :
            return self.median(nums1)
        if nums1[size1-1] <= nums2[0]:
            return self.median(nums1+nums2)
        elif nums2[size2-1] <= nums1[0] :
            return self.median(nums2+nums1)

        if size2<size1:
            nums1,nums2 = nums2,nums1
        
        ## 自我思路  先算出位置 单数或双数  从每个数组中的中位数开始比较   失败
        ## 学习思路1 O(（m+n）/2)计算所有中位数可能出现的位置   从二个数字第一个数字开始，向后移动位置,谁小移动谁，这样移动到一半的时候中位数就出现了。
        ## 学习思路2 O(long(m+n)) 使用二分查找计算，中位数。每次减少 被舍弃掉了部分，直到被舍弃掉m+n/2时 得到中位数
        return self.myMedian(nums1,nums2)
        ## return self.findMedianByIteration(nums1,nums2)
        ## return self.findMedianByDichotomy(nums1,nums2)

    def findMedianByIteration(self, nums1: List[int], nums2: List[int]) -> float:
        half = (len(nums1)+len(nums2)) /2
        for i in range(len(nums1)):
            j = half - i
            nums1[i],nums1[i-1],nums2[j],nums2[j-1]

    def findMedianByDichotomy(self, nums1: List[int], nums2: List[int]) -> float:
        pass

    def myMedian(self, nums1: List[int], nums2: List[int]) -> float:
        half = (len(nums1)+len(nums2)) /2
        i,j,m,n=0,0,0,0
        for x in range(math.floor(half)+1):
            m=n
            if i==len(nums1):
                ## 在中位数到来之前，就超出大小，那么中位数一定在数组2中。并且位置也确认在 len - half中，计算单双即可。
                ## 既然已一定是排在前面，那么顺序已经不重要，只需要拿到那个位置的数字即可
                print(nums2[0:j]+nums1+nums2[j:])
                return self.median(nums2[0:j]+nums1+nums2[j:])
            if nums1[i]>nums2[j] :
                j=j+1
                n=nums2[j-1]
            else :
                i=i+1
                n=nums1[i-1]
        if (len(nums1)+len(nums2)) % 2 == 1:
            return n
        else:
            return (m+n)/2

    def median(self,nums: List[int]):
        half = len(nums) // 2
        return (nums[half] + nums[~half]) / 2

    def myMedianError(self, nums1: List[int], nums2: List[int]) -> float:
        half1 = size1 // 2
        half2 = size2 // 2
        half = (size1 + size2 )//2
        temp1 = nums1[half1]
        temp2 = nums2[half2]
        if temp2>temp1:
            self.findMedianSortedArrays(nums2,nums1)
        # 二分法寻址
        while temp1<=temp2:
            half1 = half1//2
            half2 = half2//2
            temp1 = nums1[half1]
            temp2 = nums2[half2]

        return (temp1+temp2)/2

    def setUp(self):
        self.run = self.findMedianSortedArrays

    # def test_algorithm1(self):
    #     nums1 = [1, 3]
    #     nums2 = [2]
    #     result = self.run(nums1,nums2)
    #     self.assertEqual(2, result)

    # def test_algorithm2(self):
    #     nums1 = [1,2,3]
    #     nums2 = [1,2,3]
    #     result = self.run(nums1,nums2)
    #     self.assertEqual(2, result)

    # def test_algorithm3(self):
    #     nums1 = [1,2,3,4,5,6,7,8,9]
    #     nums2 = [2]
    #     result = self.run(nums1,nums2)
    #     self.assertEqual(4.5, result)
    
    # def test_algorithm4(self):
    #     nums1 = [1,2,3,4,5,6,7,8,9]
    #     nums2 = [2,3]
    #     result = self.run(nums1,nums2)
    #     self.assertEqual(4, result)

    # def test_algorithm5(self):
    #     nums1 = [1,3,5,7,9,11,13,15,17,19]
    #     nums2 = [2,4,6,8,10,12,14,16,18,20]
    #     result = self.run(nums1,nums2)
    #     self.assertEqual(10.5, result)

    # def test_algorithm6(self):
    #     nums1 = []
    #     nums2 = [1]
    #     result = self.run(nums1,nums2)
    #     self.assertEqual(1, result)

    def test_algorithm7(self):
        nums1 = [2]
        nums2 = [1,3,4]
        result = self.run(nums1,nums2)
        self.assertEqual(2.5, result)



    # def test_algorithm2(self):
    #     nums1 = [1, 2]
    #     nums2 = [3, 4]
    #     result = self.run(s)
    #     self.assertEqual(2.5, result)

if __name__ == '__main__':
    unittest.main()