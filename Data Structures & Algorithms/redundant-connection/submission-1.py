class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        nodeMap = {i:[] for i in range(len(edges) + 1)}
        res = []
        def dfs(node, parent):
            if node in visit:
                return True
            
            visit.add(node)

            for edge in nodeMap[node]:
                if edge == parent:
                    continue
                
                if dfs(edge, node):
                    return True
            
            return False
        
        for n1, n2 in edges:
            nodeMap[n1].append(n2)
            nodeMap[n2].append(n1)
            visit = set()

            if dfs(n1, None):
                return [n1, n2]
            
        
        return res
        