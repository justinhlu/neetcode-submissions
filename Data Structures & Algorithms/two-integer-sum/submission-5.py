class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sumMap = {}
        res = []
        for i in range(len(nums)):
            difference = target - nums[i]

            if nums[i] in sumMap:
                res = [sumMap[nums[i]], i]
            else:
                sumMap[difference] = i 
        
        return res