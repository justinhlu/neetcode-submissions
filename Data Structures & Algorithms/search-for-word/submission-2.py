class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        visited = set()
        directions = [[0,1],[1,0],[-1, 0], [0,-1]]

        def backtrack(r,c,index):
            if board[r][c] != word[index]:
                return False
            
            if len(word)-1 == index:
                return True
            visited.add((r,c))
            for dr, dc in directions:
                nr = dr + r
                nc = dc + c

                if nc >= 0 and nc < COLS and nr >= 0 and nr < ROWS and (nr, nc) not in visited:
                    if backtrack(nr, nc, index + 1):
                        return True    

            visited.remove((r,c))
            return False

        for r in range(ROWS):
            for c in range(COLS):
                if backtrack(r,c,0):
                    return True
        
        return False