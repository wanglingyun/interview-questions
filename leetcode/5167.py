import unittest
import math
from typing import List

class Node:
    def __init__(self, x):
        strs_x = x.split(",")
        self.name = strs_x[0]
        self.time = int(strs_x[1])
        self.amount = int(strs_x[2])
        self.city = strs_x[3]
        self.str = x

class Solution(unittest.TestCase):
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        if(len(transactions)==0):
            return []
        result = set()
        temp_map = {}
        for x in transactions:
            node = Node(x)
            #金额大于1000
            if(node.amount>=1000):
                result.add(x)
            #和另一个城市的同名交易 且交易不超过60分钟
            if node.name in temp_map:
                for temp_node in temp_map[node.name]:
                    # if(node.name == "iris" and node.city == "toronto"):
                    #     print( math.fabs(temp_node.time - node.time)<60,temp_node.time,node.time)
                    #     print(not temp_node.city == node.city,temp_node.city,node.city)
                    
                    if (math.fabs(temp_node.time - node.time)<60 and not temp_node.city == node.city):
                        result.add(node.str)
                        result.add(temp_node.str)
                temp_map[node.name].append(node)
            else:
                temp_map[node.name] = [node]
        
        return list(result)


    def setUp(self):
        self.run = self.invalidTransactions

    def test_shuffle1(self):
        transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
        type = self.run(transactions)
        print(type)
        test_result = ["alice,20,800,mtv","alice,50,100,beijing"]
        self.assertCountEqual(test_result, type)

    def test_shuffle2(self):
        transactions = ["alice,20,800,mtv","alice2,50,10000,beijing","alice,50,100,beijing"]
        type = self.run(transactions)
        test_result = ["alice,20,800,mtv","alice2,50,10000,beijing","alice,50,100,beijing"]
        self.assertCountEqual(test_result, type)

    def test_shuffle3(self):
        transactions = ["alice,20,800,mtv","alice2,5000,800,beijing","alice,50,100,beijing","alice2,50,50,beijing"]
        type = self.run(transactions)
        test_result = ["alice,20,800,mtv","alice,50,100,beijing"]
        self.assertCountEqual(test_result, type)

    def test_shuffle4(self):
        transactions = ["bob,55,173,barcelona","lee,113,952,zurich","maybe,115,1973,madrid","chalicefy,229,283,istanbul","bob,24,874,shanghai","alex,568,412,tokyo","alex,242,1710,milan","iris,722,879,shenzhen","chalicefy,281,1586,warsaw","maybe,246,778,bangkok","xnova,605,166,newdelhi","iris,631,991,hongkong","chalicefy,500,620,tokyo","chalicefy,380,428,istanbul","iris,905,180,barcelona","alex,810,732,shenzhen","iris,689,389,paris","xnova,475,298,singapore","lee,58,709,amsterdam","xnova,717,546,guangzhou","maybe,78,435,shenzhen","maybe,333,145,hongkong","lee,405,1230,hongkong","lee,456,1440,tokyo","chalicefy,286,1071,amsterdam","alex,55,271,shanghai","bob,91,273,warsaw","iris,195,1825,tokyo","maybe,639,417,madrid","maybe,305,882,chicago","lee,443,47,chicago","chalicefy,958,840,budapest","lee,162,1239,budapest","bob,701,505,montreal","alex,52,1575,munich","bob,533,1407,amsterdam","lee,621,491,tokyo","chalicefy,866,622,rome","alex,925,455,hongkong","lee,968,164,moscow","chalicefy,31,1119,newdelhi","iris,527,700,warsaw","bob,286,1694,dubai","maybe,903,29,barcelona","maybe,474,1606,prague","maybe,851,648,beijing","lee,48,655,chicago","maybe,378,25,toronto","lee,922,691,munich","maybe,411,903,taipei","lee,651,112,guangzhou","lee,664,506,dubai","chalicefy,704,924,milan","maybe,333,1264,budapest","chalicefy,587,1112,singapore","maybe,428,437,moscow","lee,721,366,newdelhi","iris,824,1962,beijing","chalicefy,834,489,istanbul","alex,639,1473,zurich","xnova,898,738,tokyo","chalicefy,585,1313,frankfurt","xnova,730,759,beijing","alex,69,892,montreal","lee,77,91,barcelona","lee,722,611,taipei","chalicefy,706,1982,jakarta","chalicefy,743,584,luxembourg","xnova,683,322,istanbul","chalicefy,60,861,prague","alex,366,871,shenzhen","chalicefy,77,870,shenzhen","iris,913,1501,warsaw","iris,846,1176,warsaw","bob,873,69,zurich","alex,601,181,chicago","chalicefy,118,145,hongkong","bob,879,982,montreal","lee,994,950,chicago","maybe,885,1900,shanghai","lee,717,1447,shanghai","chalicefy,71,434,istanbul","bob,870,968,toronto","maybe,718,51,beijing","alex,669,896,istanbul","chalicefy,639,506,rome","alex,594,934,frankfurt","maybe,3,89,jakarta","xnova,328,1710,rome","alex,611,571,chicago","chalicefy,31,458,montreal","iris,973,696,toronto","iris,863,148,rome","chalicefy,926,511,warsaw","alex,218,1411,zurich","chalicefy,544,1296,shenzhen","iris,27,23,montreal","chalicefy,295,263,prague","maybe,575,31,munich","alex,215,174,prague"]
        type = self.run(transactions)
        
        test_1= ["alex,55,271,shanghai","alex,69,892,montreal","iris,195,1825,tokyo","maybe,428,437,moscow","bob,873,69,zurich","alex,639,1473,zurich","lee,77,91,barcelona","xnova,730,759,beijing","lee,968,164,moscow","lee,621,491,tokyo","chalicefy,639,506,rome","lee,722,611,taipei","alex,611,571,chicago","lee,58,709,amsterdam","chalicefy,743,584,luxembourg","chalicefy,118,145,hongkong","lee,664,506,dubai","lee,162,1239,budapest","alex,601,181,chicago","maybe,474,1606,prague","chalicefy,587,1112,singapore","chalicefy,706,1982,jakarta","maybe,851,648,beijing","lee,922,691,munich","chalicefy,31,1119,newdelhi","bob,870,968,toronto","alex,594,934,frankfurt","chalicefy,544,1296,shenzhen","chalicefy,31,458,montreal","maybe,246,778,bangkok","maybe,885,1900,shanghai","iris,863,148,rome","chalicefy,71,434,istanbul","chalicefy,286,1071,amsterdam","maybe,903,29,barcelona","iris,722,879,shenzhen","alex,568,412,tokyo","maybe,305,882,chicago","chalicefy,295,263,prague","bob,879,982,montreal","lee,994,950,chicago","lee,456,1440,tokyo","lee,113,952,zurich","bob,24,874,shanghai","iris,689,389,paris","xnova,328,1710,rome","chalicefy,704,924,milan","lee,651,112,guangzhou","chalicefy,926,511,warsaw","lee,717,1447,shanghai","bob,55,173,barcelona","maybe,78,435,shenzhen","lee,48,655,chicago","chalicefy,585,1313,frankfurt","chalicefy,77,870,shenzhen","chalicefy,229,283,istanbul","alex,215,174,prague","alex,52,1575,munich","iris,846,1176,warsaw","bob,533,1407,amsterdam","maybe,333,145,hongkong","xnova,717,546,guangzhou","iris,824,1962,beijing","chalicefy,281,1586,warsaw","alex,218,1411,zurich","chalicefy,834,489,istanbul","alex,669,896,istanbul","iris,631,991,hongkong","iris,905,180,barcelona","chalicefy,866,622,rome","alex,242,1710,milan","xnova,683,322,istanbul","maybe,411,903,taipei","maybe,333,1264,budapest","maybe,378,25,toronto","lee,721,366,newdelhi","bob,91,273,warsaw","chalicefy,60,861,prague","chalicefy,500,620,tokyo","maybe,115,1973,madrid","iris,913,1501,warsaw","bob,286,1694,dubai","lee,443,47,chicago","lee,405,1230,hongkong","chalicefy,958,840,budapest"]
        test_result = ["bob,55,173,barcelona","lee,113,952,zurich","maybe,115,1973,madrid","chalicefy,229,283,istanbul","bob,24,874,shanghai","alex,568,412,tokyo","alex,242,1710,milan","iris,722,879,shenzhen","chalicefy,281,1586,warsaw","maybe,246,778,bangkok","iris,631,991,hongkong","chalicefy,500,620,tokyo","iris,905,180,barcelona","iris,689,389,paris","lee,58,709,amsterdam","xnova,717,546,guangzhou","maybe,78,435,shenzhen","maybe,333,145,hongkong","lee,405,1230,hongkong","lee,456,1440,tokyo","chalicefy,286,1071,amsterdam","alex,55,271,shanghai","bob,91,273,warsaw","iris,195,1825,tokyo","maybe,305,882,chicago","lee,443,47,chicago","chalicefy,958,840,budapest","lee,162,1239,budapest","alex,52,1575,munich","bob,533,1407,amsterdam","lee,621,491,tokyo","chalicefy,866,622,rome","lee,968,164,moscow","chalicefy,31,1119,newdelhi","bob,286,1694,dubai","maybe,903,29,barcelona","maybe,474,1606,prague","maybe,851,648,beijing","lee,48,655,chicago","maybe,378,25,toronto","lee,922,691,munich","maybe,411,903,taipei","lee,651,112,guangzhou","lee,664,506,dubai","chalicefy,704,924,milan","maybe,333,1264,budapest","chalicefy,587,1112,singapore","maybe,428,437,moscow","lee,721,366,newdelhi","iris,824,1962,beijing","chalicefy,834,489,istanbul","alex,639,1473,zurich","chalicefy,585,1313,frankfurt","xnova,730,759,beijing","alex,69,892,montreal","lee,77,91,barcelona","lee,722,611,taipei","chalicefy,706,1982,jakarta","chalicefy,743,584,luxembourg","xnova,683,322,istanbul","chalicefy,60,861,prague","chalicefy,77,870,shenzhen","iris,913,1501,warsaw","iris,846,1176,warsaw","bob,873,69,zurich","alex,601,181,chicago","chalicefy,118,145,hongkong","bob,879,982,montreal","lee,994,950,chicago","maybe,885,1900,shanghai","lee,717,1447,shanghai","chalicefy,71,434,istanbul","bob,870,968,toronto","alex,669,896,istanbul","chalicefy,639,506,rome","alex,594,934,frankfurt","xnova,328,1710,rome","alex,611,571,chicago","chalicefy,31,458,montreal","iris,973,696,toronto","iris,863,148,rome","chalicefy,926,511,warsaw","alex,218,1411,zurich","chalicefy,544,1296,shenzhen","chalicefy,295,263,prague","alex,215,174,prague"]
        # print(sorted(type))
        # print(sorted(test_result))
        self.assertEqual(test_result, type)
        # print(self.maxDiff(test_result, type))

if __name__ == '__main__':
    unittest.main()