class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        nodeMap = {i:[] for i in range(n)}

        for n1, n2 in edges:
            nodeMap[n1].append(n2)
            nodeMap[n2].append(n1)
        
        cycle, visit = set(), set()

        def dfs(node, parent):
            if node in cycle:
                return False
            if node is None or node in visit:
                return True
            
            cycle.add(node)

            for edge in nodeMap[node]:
                if edge == parent:
                    continue

                if not dfs(edge, node):
                    return False

            cycle.remove(node)
            visit.add(node)

            return True
        
        return dfs(0,None) and len(visit) == n