class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = set()

        ROWS = len(grid)
        COLS = len(grid[0])
        
        def bfs(r, c):
            q = collections.deque()
            q.append((r,c))
            directions = [[1,0], [0,1], [-1,0],[0,-1]]

            while q:
                row, col = q.pop()
                visited.add((row,col))

                for dr, dc in directions:
                    nr = dr + row
                    nc = dc + col

                    if nr >= 0 and nr < ROWS and nc >= 0 and nc < COLS and (nr,nc) not in visited and grid[nr][nc] == "1":
                        q.append((nr,nc))
            return

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    islands += 1

        return islands