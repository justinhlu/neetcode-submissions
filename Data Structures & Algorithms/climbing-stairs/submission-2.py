class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [-1] * (n + 1)
        res = 0

        def dfs(i):
            if i == n:
                return 1
            if i > n:
                return 0
                
            if memo[i] != -1:
                return memo[i]
            
            memo[i] = dfs(i+1) + dfs(i+2)

            return memo[i]
        
        res = dfs(0)

        return res