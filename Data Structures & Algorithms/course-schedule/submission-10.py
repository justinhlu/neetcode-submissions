class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
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
        
        for crs in range(numCourses):
            if not dfs(crs, path):
                return False
        
        return True
            

            
