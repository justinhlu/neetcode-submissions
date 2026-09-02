class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        nodeMap = {i:[] for i in range(n)}
        components = 0

        for n1, n2 in edges:
            nodeMap[n1].append(n2)
            nodeMap[n2].append(n1)
        
        visit = set()

        def dfs(node, parent):
            if node in visit:
                return
            
            visit.add(node)

            for edge in nodeMap[node]:
                if edge == parent:
                    continue

                dfs(edge, node)

            return 
        
        for i in range(n):
            if i not in visit:
                dfs(i, None)
                components += 1
        
        return components
            