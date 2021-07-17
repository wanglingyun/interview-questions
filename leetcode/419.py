"""
419. 甲板上的战舰
给定一个二维的甲板， 请计算其中有多少艘战舰。 战舰用 'X'表示，空位用 '.'表示。 你需要遵守以下规则：

给你一个有效的甲板，仅由战舰或者空位组成。
战舰只能水平或者垂直放置。换句话说,战舰只能由 1xN (1 行, N 列)组成，或者 Nx1 (N 行, 1 列)组成，其中N可以是任意大小。
两艘战舰之间至少有一个水平或垂直的空位分隔 - 即没有相邻的战舰。
示例 :

X..X
...X
...X
"""
import unittest
from typing import List

class Solution(unittest.TestCase):
    def countBattleships(self, board: List[List[str]]) -> int:
        

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