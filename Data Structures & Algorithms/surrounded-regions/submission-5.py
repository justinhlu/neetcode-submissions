class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if board is None:
            return None
        
        ROWS = len(board)
        COLS = len(board[0])
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        q = collections.deque()

        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 or r == ROWS-1 or c == 0 or c == COLS - 1:
                    if board[r][c] == "O":
                        q.append((r,c))
        
        while q:
            row, col = q.popleft()
            if board[row][col] == "O":
                board[row][col] = "T"

                for dr, dc in directions:
                    nr = dr + row
                    nc = dc + col

                    if nr in range(ROWS) and nc in range(COLS) and board[nr][nc] == "O":
                        q.append((nr,nc))
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"
            