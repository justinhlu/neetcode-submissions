class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}
        path = set()

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        def dfs(crs):
            if crs in path:
                return False
            if preMap[crs] == []:
                return True
            
            path.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            
            preMap[crs] = []
            path.remove(crs)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False

        return True