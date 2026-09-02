class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subsets = []
        nums.sort()

        def dfs(index):
            if index >= len(nums):
                res.append(subsets.copy())
                return
            
            subsets.append(nums[index])
            dfs(index+1)
            subsets.pop()
            while index + 1 < len(nums) and nums[index+1] == nums[index]:
                index += 1

            dfs(index+1)
            return
        
        dfs(0)
        return res