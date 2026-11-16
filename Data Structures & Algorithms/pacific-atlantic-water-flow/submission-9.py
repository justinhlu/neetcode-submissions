class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        pac, atl = set(), set()
        directions = [[0,1], [1,0],[-1,0],[0,-1]]
        ROWS = len(heights)
        COLS = len(heights[0])

        def dfs(r,c, visited, prevHeight):
            if r not in range(ROWS) or c not in range(COLS) or (r,c) in visited or heights[r][c] < prevHeight:
                return
            visited.add((r,c))
            for dr, dc in directions:
                nr = dr + r
                nc = dc + c
                if nr in range(ROWS) and nc in range(COLS) and (nr,nc) not in visited and heights[nr][nc] >= prevHeight:
                    dfs(nr,nc, visited, heights[r][c])
                
            return
        
        for r in range(ROWS):
            dfs(r,0, pac, 0)
            dfs(r, COLS-1, atl, 0)
        
        for c in range(COLS):
            dfs(0,c, pac, 0)
            dfs(ROWS-1, c, atl, 0)
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        
        return res
        
