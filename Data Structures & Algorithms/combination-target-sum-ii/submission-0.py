class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        res = []
        def dfs(index, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            
            if total > target or index >= len(candidates):
                return

            
            cur.append(candidates[index])
            dfs(index + 1, cur, total + candidates[index])
            cur.pop()
            while index + 1 < len(candidates) and candidates[index] == candidates[index+1]:
                index += 1 
            dfs(index + 1, cur, total)

            return
        
        dfs(0, [], 0)
        return res
