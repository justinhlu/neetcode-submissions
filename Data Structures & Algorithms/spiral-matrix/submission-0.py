class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        LEFT = 0
        RIGHT = len(matrix[0])
        TOP = 0
        BOT = len(matrix)

        while LEFT < RIGHT and TOP < BOT:
            for i in range(LEFT, RIGHT):
                res.append(matrix[TOP][i])
            
            TOP += 1

            for i in range(TOP, BOT):
                res.append(matrix[i][RIGHT-1])
            
            RIGHT -= 1

            if not (LEFT < RIGHT and TOP < BOT):
                break
            
            for i in range(RIGHT - 1, LEFT - 1, -1):
                res.append(matrix[BOT-1][i])
            
            BOT -= 1

            for i in range(BOT-1, TOP-1, -1):
                res.append(matrix[i][LEFT])
            
            LEFT += 1
        
        return res