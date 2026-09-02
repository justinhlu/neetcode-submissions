class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        nodeMap = {i:[] for i in range(n)}
        visitSet = set()
        res = 0

        for n1,n2 in edges:
            nodeMap[n1].append(n2)
            nodeMap[n2].append(n1)

        def dfs(i):
            if i == n or i in visitSet or i < 0:
                return False

            visitSet.add(i)

            for neighbor in nodeMap[i]:
                dfs(neighbor)

            return True

        for i in range(n):
            if dfs(i):
                res += 1

        
        return res
