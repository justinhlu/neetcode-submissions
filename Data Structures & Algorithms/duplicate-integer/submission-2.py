class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numMap = {}

        for i in range(len(nums)):
            if nums[i] in numMap:
                return True
            else:
                numMap[nums[i]] = 1
        
        return False