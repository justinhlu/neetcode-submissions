class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        preMap = {x:[] for x in range(n)}

        for n1, n2 in edges:
            preMap[n1].append(n2)
            preMap[n2].append(n1)
        
        visit, cycle = set(), set()

        def dfs(node, parent):
            if node in cycle:
                return False
            
            cycle.add(node)

            for edge in preMap[node]:
                if edge == parent:
                    continue
                
                if not dfs(edge, node):
                    return False
            
            cycle.remove(node)
            visit.add(node)

            return True
        
        return dfs(0, None) and len(visit) == n