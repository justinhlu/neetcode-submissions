class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        res = []
        for i in range(len(nums)):
            difference = target - nums[i]
        
            if nums[i] in map:
                res = [map[nums[i]], i]
            else:
                map[difference] = i
        
        return res
