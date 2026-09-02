class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        res = 0
        
        for num in nums:
            idx = abs(num) - 1
            if nums[idx] >= 0:
                nums[idx] *= -1
            else:
                res = abs(num)

        return res 