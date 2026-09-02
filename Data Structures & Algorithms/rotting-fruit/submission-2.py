class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if grid is None:
            return -1
        
        ROWS = len(grid)
        COLS = len(grid[0])
        q = collections.deque()
        fresh = 0
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        res = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))

        while fresh > 0 and q:
            qLen = len(q)

            for i in range(qLen):
                row, col = q.popleft()
                for dr, dc in directions:
                    nr = dr + row
                    nc = dc + col

                    if nr in range(ROWS) and nc in range(COLS) and grid[nr][nc] == 1:
                        q.append((nr,nc))
                        grid[nr][nc] = 2
                        fresh -= 1
            res += 1
        
        
        return res if fresh == 0 else -1