class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        for i in range(ROWS):
            for j in range(COLS):
                if i < j:
                    # Transpose
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(ROWS):
            l = 0
            r = ROWS - 1
            while l < r:
                matrix[i][l],matrix[i][r] = matrix[i][r], matrix[i][l]
                l += 1
                r -= 1
