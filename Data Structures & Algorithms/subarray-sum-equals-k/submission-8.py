class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if len(nums) == 0:
            return 0
        
        curSum = 0
        res = 0
        sumDict = {0:1}

        for i in range(len(nums)):
            curSum += nums[i]
            diff = curSum - k

            res += sumDict.get(diff, 0)
            sumDict[curSum] = 1 + sumDict.get(curSum, 0)
        
        return res