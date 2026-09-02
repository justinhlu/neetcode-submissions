class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_dict = {}
        for i in range(len(nums)):
            if nums[i] in num_dict:
                return True
            else:
                num_dict[nums[i]] = i
        
        return False