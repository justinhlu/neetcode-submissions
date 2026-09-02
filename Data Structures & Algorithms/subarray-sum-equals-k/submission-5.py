class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        sumMap = {0:1}
        curSum = 0

        for i in range(len(nums)):
            curSum += nums[i] 
            diff = curSum - k
            res += sumMap.get(diff,0)
            sumMap[curSum] = 1 + sumMap.get(curSum, 0)
            

        return res