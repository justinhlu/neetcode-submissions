class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        currDict = {0:1}
        curSum = 0
        for i in range(len(nums)):
            curSum += nums[i]
            diff = curSum - k
            res += currDict.get(diff, 0)
            currDict[curSum] = 1 + currDict.get(curSum, 0)
        
        return res
