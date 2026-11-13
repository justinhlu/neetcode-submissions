class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        subset = []

        def dfs(index):
            if index >= len(nums):
                res.append(subset.copy())
                return
        
            
            subset.append(nums[index])
            dfs(index+1)
            subset.pop()
            while index + 1 < len(nums) and nums[index+1] == nums[index]:
                index += 1

            dfs(index+1)
            return
        
        dfs(0)
        return res