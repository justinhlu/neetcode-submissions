class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid is None:
            return 0
        
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        islands = 0
        visit = set()

        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            visit.add((r,c))

            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc

                    if nr in range(ROWS) and nc in range(COLS) and (nr,nc) not in visit and grid[nr][nc] == "1":
                        visit.add((nr,nc))
                        q.append((nr,nc))
            
            return

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c)
                    islands += 1
        
        return islands