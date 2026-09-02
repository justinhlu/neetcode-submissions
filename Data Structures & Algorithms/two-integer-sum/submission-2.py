class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in num_dict:
                return [num_dict[difference], i]
            else:
                num_dict[nums[i]] = i
        
        return [-1,-1]
        

