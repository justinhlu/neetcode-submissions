class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [[0,1], [1,0],[-1,0], [0,-1]]
        visited = set()

        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))

            while q:
                row, col = q.popleft()
                visited.add((row, col))

                for dr, dc in directions:
                    nr = dr + row
                    nc = dc + col

                    if nr >= 0 and nr < ROWS and nc >= 0 and nc < COLS and (nr,nc) not in visited and grid[nr][nc] == "1":
                        q.append((nr,nc))
            
            return

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visited and grid[r][c] == "1":
                    bfs(r,c)
                    islands += 1
        
        return islands