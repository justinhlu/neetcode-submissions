class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if grid is None:
            return
        
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        q = collections.deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
        
        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if nr in range(ROWS) and nc in range(COLS) and grid[nr][nc] == 2147483647:
                    grid[nr][nc] = 1 + grid[r][c]
                    q.append((nr, nc))
        
        return