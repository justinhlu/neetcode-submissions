class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges)+1)]
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(n1, n2):
            root_a = find(n1)
            root_b = find(n2)

            if root_a == root_b:
                return False
            
            parent[root_a] = root_b
            return True
        
        for a, b in edges:
            if not union(a,b):
                return [a,b]
        
        return []