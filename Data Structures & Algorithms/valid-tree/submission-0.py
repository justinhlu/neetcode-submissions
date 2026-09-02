class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visit = set()
        nodeMap = {i:[] for i in range(n)}

        for n1, n2 in edges:
            nodeMap[n1].append(n2)
            nodeMap[n2].append(n1)

        def dfs(node, parent):
            if node in visit:
                return False

            visit.add(node)

            for edge in nodeMap[node]:
                if edge == parent:
                    continue
                if not dfs(edge, node):
                    return False
            
            return True

        if not dfs(0, None):
            return False
        
        if len(visit) == n:
            return True
        else:
            return False