class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixArr = [0] * len(nums)
        postfixArr = [0] * len(nums)
        res = [0] * len(nums)

        prefixArr[0] = 1
        postfixArr[len(nums)-1] = 1
        for i in range(1,len(nums)):
            prefixArr[i] = nums[i-1] * prefixArr[i-1]
        
        for i in range(len(nums)-2,-1,-1):
            postfixArr[i] = nums[i+1] * postfixArr[i+1]
        
        for i in range(len(nums)):
            res[i] = prefixArr[i] * postfixArr[i]

        return res
