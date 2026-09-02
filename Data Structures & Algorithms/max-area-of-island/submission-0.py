class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            visited.add((r,c))
            directions = [[0,1],[0,-1],[1,0],[-1,0]]
            area = 1
            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    r = dr + row
                    c = dc + col

                    if r in range(rows) and c in range(cols) and grid[r][c] == 1 and (r,c) not in visited:
                        visited.add((r,c))
                        q.append((r,c))
                        area += 1

            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    area = bfs(r,c)
                    res = max(res, area)
                
        return res