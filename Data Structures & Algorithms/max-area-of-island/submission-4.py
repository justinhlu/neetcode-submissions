class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if grid is None:
            return 0
        
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        visited = set()
        maxArea = 0

        def bfs(r,c):
            res = 1
            q = collections.deque()
            q.append((r,c))
            visited.add((r,c))
            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    nr = dr + row
                    nc = dc + col

                    if nr in range(ROWS) and nc in range(COLS) and (nr,nc) not in visited and grid[nr][nc] == 1:
                        q.append((nr,nc))
                        visited.add((nr,nc))
                        res += 1
            
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visited:
                    area = bfs(r,c)
                    maxArea = max(area, maxArea)
        
        return maxArea