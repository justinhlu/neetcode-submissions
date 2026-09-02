class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixArr = [0] * len(nums)
        postfixArr = [0] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            prefixArr[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            postfixArr[i] = postfix
            postfix *= nums[i]
        
        res = []
        for i in range(len(nums)):
            res.append(prefixArr[i] * postfixArr[i])

        return res