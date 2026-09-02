class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        firstMemo, secMemo = [-1] * len(nums), [-1] * len(nums)
        first = nums[:len(nums)-1]
        second = nums[1:len(nums)]

        def dfs(i, houses, memo):
            if i >= len(houses):
                return 0
            
            if memo[i] != -1:
                return memo[i]
            
            memo[i] = max(houses[i] + dfs(i+2, houses, memo), dfs(i+1, houses, memo))

            return memo[i]
        
        return max(dfs(0, first, firstMemo), dfs(0, second, secMemo))