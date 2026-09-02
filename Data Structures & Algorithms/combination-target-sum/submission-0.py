class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(index, currList, currSum):
            if currSum == target:
                res.append(currList.copy())
                return
            if index >= len(nums) or currSum > target:
                return

            currList.append(nums[index])
            dfs(index, currList, currSum + nums[index])
            currList.pop()
            dfs(index+1, currList, currSum)
            return
        
        dfs(0,[],0)

        return res