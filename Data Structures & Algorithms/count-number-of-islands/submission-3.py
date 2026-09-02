class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid is None:
            return 0
        
        ROWS = len(grid)
        COLS = len(grid[0])
        islands = 0
        visited = set()
        directions = [[0,1],[1,0],[-1,0],[0,-1]]

        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            visited.add((r,c))

            while q:
                row, col = q.pop()
                for dr,dc in directions:
                    nr = row + dr
                    nc = col + dc

                    if (nr < ROWS and nr >= 0 and nc < COLS and nc >= 0) and (nr,nc) not in visited and grid[nr][nc] == "1":
                        q.append((nr,nc))
                        visited.add((nr,nc))

            return 
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    islands += 1
        
        return islands