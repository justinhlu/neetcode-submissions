class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        nodeMap = {i:[] for i in range(n)}

        for n1,n2 in edges:
            nodeMap[n1].append(n2)
            nodeMap[n2].append(n1)
        
        res = 0
        visit = set()

        def dfs(node):
            if node in visit:
                return False
            
            visit.add(node)

            for v in nodeMap[node]:
                dfs(v)
            
            return True
        
        for i in range(n):
            if dfs(i):
                res += 1
        
        return res