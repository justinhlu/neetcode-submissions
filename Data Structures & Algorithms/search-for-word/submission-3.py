class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        directions = [[0,1],[1,0], [-1,0], [0,-1]]

        visit = set()

        def backtrack(r,c, index):
            if board[r][c] != word[index]:
                return False
            if index == len(word)-1:
                return True
            
            visit.add((r,c))
            for dr, dc in directions:
                nr = dr + r
                nc = dc + c

                if nr < ROWS and nr >= 0 and nc < COLS and nc >= 0 and (nr, nc) not in visit:
                    if backtrack(nr, nc, index+1):
                        return True

            visit.remove((r,c))
            return False
            

        for r in range(ROWS):
            for c in range(COLS):
                if backtrack(r,c, 0):
                    return True
        
        return False