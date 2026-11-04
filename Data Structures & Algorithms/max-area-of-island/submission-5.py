class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if grid is None:
            return 0
        
        res = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [[0,1], [1,0], [-1,0], [0,-1]]
        visit = set()

        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            area = 1
            visit.add((r,c))

            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    nr = dr + row
                    nc = dc + col

                    if nr in range(ROWS) and nc in range(COLS) and (nr,nc) not in visit and grid[nr][nc] == 1:
                        area += 1
                        visit.add((nr,nc))
                        q.append((nr,nc))
            
            return area

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visit and grid[r][c] == 1:
                    area = bfs(r,c)
                    res = max(area, res)
        
        return res
            