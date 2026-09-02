class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses == 1:
            return True
        
        preMap = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        path = set()

        def dfs(crs, path):
            if crs in path:
                return False
            if preMap[crs] == []:
                return True
            
            path.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre, path):
                    return False
            
            path.remove(crs)
            preMap[crs] = []

            return True
        
        for i in range(numCourses):
            if not dfs(i, path):
                return False
        
        return True