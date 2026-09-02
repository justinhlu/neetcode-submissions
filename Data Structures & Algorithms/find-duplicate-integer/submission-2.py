class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        res = 0

        for i in range(len(nums)):
            index = abs(nums[i]) -1

            if nums[index] >= 0:
                nums[index] *= -1
            else:
                res = abs(nums[i])
            
        return res
                