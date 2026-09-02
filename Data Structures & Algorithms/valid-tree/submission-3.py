class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        preMap = {x:[] for x in range(n)}

        for n1,n2 in edges:
            preMap[n1].append(n2)
            preMap[n2].append(n1)
        
        cycle, visit = set(), set()

        def dfs(i, parent):
            if i in cycle:
                return False
            
            cycle.add(i)

            for edge in preMap[i]:
                if edge == parent:
                    continue
                if not dfs(edge, i):
                    return False
            
            visit.add(i)
            cycle.remove(i)
            return True
        
        return dfs(0,None) and len(visit) == n