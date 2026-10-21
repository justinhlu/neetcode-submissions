class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges)+1)]
        res = []
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            
            return parent[x]

        def union(a,b):
            root_a = find(a)
            root_b = find(b)

            if root_a == root_b:
                return False
            
            parent[root_a] = root_b
            return True
        
        for n1,n2 in edges:
            if not union(n1,n2):
                return [n1,n2]
        
        return []