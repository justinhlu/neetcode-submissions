class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        nodeMap = {i:[] for i in range(n)}
        for n1,v in edges:
            nodeMap[n1].append(v)
            nodeMap[v].append(n1)

        visit = set()
        components = 0
        def dfs(node):
            
            if node in visit:
                return False
            
            visit.add(node)

            for nei in nodeMap[node]:
                dfs(nei)
                    
            return True
        
        for i in range(n):
            if dfs(i):
                components += 1

        return components

        