class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(used):
            if len(used) == len(nums):
                res.append(used.copy())
                return
            
            for num in nums:
                if num in used:
                    continue
                
                used.append(num)
                dfs(used)
                used.pop()
            
            return
        
        dfs([])
        return res