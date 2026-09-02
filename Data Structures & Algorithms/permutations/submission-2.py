class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(cur, used):
            if len(cur) == len(nums):
                res.append(cur.copy())
                return
            
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    cur.append(nums[i])
                    dfs(cur, used)
                    cur.pop()
                    dfs(cur, used)
                    used[i] = False
            return
        
        dfs([], [False] * len(nums))

        return res