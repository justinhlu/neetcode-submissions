class Solution:
    def climbStairs(self, n: int) -> int:
        def climb(i, memo):
            if i == n:
                return 1
            if i > n:
                return 0
            if i in memo:
                return memo[i]
            
            memo[i] = climb(i+1, memo) + climb(i+2,memo)

            return memo[i]
        
        return climb(0, {})