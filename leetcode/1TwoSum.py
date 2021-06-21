class Solution:
    def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(1,len(nums)-i,1):
                if(nums[i]+nums[i+j]==target):
                    return [i,i+j]
            
        return [0,0]
    def twoSum(nums,target):
        dictNum = {}
        for i in range(len(nums)):
            x = target-nums[i]
            if(x in dictNum):
                return [dictNum[x],i]
            dictNum[nums[i]]=i
            print(nums[i],i)


    def test1():
        nums = [1,3,4,5,6,2]
        target = 3
        rtype = twoSum()
        print(rtype)

    def test2():
        nums = [3,2,4]
        target = 6
        rtype = twoSum()
        print(rtype)
    def __init__(self):
        print "调用父类构造函数"
        test1()
        test2()

t = new Solution()