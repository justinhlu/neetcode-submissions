class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        nodeMap = {i:[] for i in range(n)}
        for n1, n2 in edges:
            nodeMap[n1].append(n2)
            nodeMap[n2].append(n1)
        
        visit = set()
        components = 0

        def dfs(node, parent):

            visit.add(node)

            for edge in nodeMap[node]:
                if edge == parent:
                    continue
                elif edge not in visit:
                    dfs(edge, node)

        
        for node in range(n):
            if node not in visit:
                dfs(node, None)
                components += 1
        
        return components
            
