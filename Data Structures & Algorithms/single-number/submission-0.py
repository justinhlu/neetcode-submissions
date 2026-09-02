class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor_num = 0
        for i in range(len(nums)):
            xor_num ^= nums[i]
        return xor_num
