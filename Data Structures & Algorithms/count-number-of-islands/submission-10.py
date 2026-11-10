class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid is None:
            return 0

        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        visit = set()
        islands = 0

        def bfs(r,c):
            q = deque()
            q.append((r,c))
            visit.add((r,c))

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr = dr + row
                    nc = dc + col

                    if nr in range(ROWS) and nc in range(COLS) and (nr,nc) not in visit and grid[nr][nc] == "1":
                        q.append((nr,nc))
                        visit.add((nr,nc))
            
            return

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visit and grid[r][c] == "1":
                    islands += 1
                    bfs(r,c)
        
        return islands
