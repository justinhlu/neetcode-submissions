class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        rows = len(grid)
        cols = len(grid[0])
        res = 0
        directions = [[0,1], [1,0], [-1,0],[0,-1]]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))

        while q:
            qLen = len(q)
            progress = False
            for _ in range(qLen):
                row, col = q.popleft()

                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc

                    if nr in range(rows) and nc in range(cols) and grid[nr][nc] == 1:
                        q.append((nr,nc))
                        grid[nr][nc] = 2
                        progress = True
            
            if progress:
                res += 1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
        
        return res