class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        rows = len(grid)
        cols = len(grid[0])
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        res = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
        while q:
            qLen = len(q)
            progressed = False

            for _ in range(qLen):
                row, col = q.popleft()

                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc

                    if nr in range(rows) and nc in range(cols) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr,nc))
                        progressed = True
            if progressed:
                res += 1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    res = -1

        return res
                    



