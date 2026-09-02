class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid is None:
            return 0
        
        islands = 0
        visited = set()
        rows = len(grid)
        cols = len(grid[0])

        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            visited.add((r,c))
            directions = [[0,1],[1,0],[-1,0],[0,-1]]
            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r,c) not in visited:
                        q.append((r,c))
                        visited.add((r,c))
            return

        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    islands += 1
        
        return islands