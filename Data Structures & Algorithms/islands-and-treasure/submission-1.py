class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = collections.deque()
        directions = [[0,1],[-1,0],[1,0],[0,-1]]
        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
        
        while q:
            row, col = q.popleft()

            for dr, dc in directions:
                nr = dr + row
                nc = dc + col

                if nr in range(rows) and nc in range(cols) and grid[nr][nc] == 2147483647:
                    grid[nr][nc] = grid[row][col] + 1
                    q.append((nr,nc))
        return