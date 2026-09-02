class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        directions = [[0,1], [-1, 0], [1, 0], [0, -1]]
        visited = set()

        def backtrack(r, c, index):
            if board[r][c] != word[index]:
                return False
   
            if index == len(word)-1:
                return True

            visited.add((r,c))
            for dr, dc in directions:
                row = r + dr
                col = c + dc 

                if row < ROWS and row >= 0 and col < COLS and col >= 0 and (row, col) not in visited:
                    if backtrack(row, col, index + 1):
                        return True
                   
            visited.remove((r,c))
            return False

        for r in range(ROWS):
            for c in range(COLS):
                if backtrack(r, c, 0):
                    return True

        return False    