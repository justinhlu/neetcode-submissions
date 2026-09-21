class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0

        if grid is None:
            return 0

        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()

        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            visited.add((r,c))
            while q:
                row, col = q.popleft()

                for dr,dc in directions:
                    nr = row + dr
                    nc = col + dc

                    if nr in range(ROWS) and nc in range(COLS) and (nr,nc) not in visited and grid[nr][nc] == "1":
                        q.append((nr,nc))
                        visited.add((nr,nc))
                        
            return

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    islands += 1
        
        return islands