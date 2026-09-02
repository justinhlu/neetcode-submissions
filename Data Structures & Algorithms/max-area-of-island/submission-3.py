class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if grid is None:
            return 0
        
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        directions = [[0,1],[1,0],[-1,0],[0,-1]]

        maxArea = 0

        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            visited.add((r,c))
            area = 1
            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    nr = dr + row
                    nc = dc + col

                    if nr >= 0 and nr < ROWS and nc >=0 and nc < COLS and (nr,nc) not in visited and grid[nr][nc] == 1:
                        q.append((nr,nc))
                        visited.add((nr,nc))
                        area += 1
            
            return area


        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visited and grid[r][c] == 1:
                    area = bfs(r,c)
                    maxArea = max(maxArea, area)
        
        return maxArea
