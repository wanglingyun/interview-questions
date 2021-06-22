# 分式化简
import unittest
import math
from typing import List

class Solution(unittest.TestCase):
    def fraction(self, cont: List[int]) -> List[int]:
        # 第一位为分子  第二位为分母
        result = [1,0]
        for n in cont[::-1] :
            # 若还存在下一个 先执行1 除以 result
            # print(n,result)
            result.reverse()
            result[0] += n*result[1]

        return result
            
    def setUp(self):
        self.run = self.fraction

    def test_shuffle1(self):
        type = self.run([3, 2, 0, 2])
        self.assertEqual([13, 4], type)
    def test_shuffle2(self):
        type = self.run([2])
        self.assertEqual([2,1], type)

if __name__ == '__main__':
    unittest.main()