class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix is None:
            return False

        ROWS = len(matrix)
        COLS = len(matrix[0])

        for row in range(ROWS):
            if target >= matrix[row][0] and target <= matrix[row][COLS-1]:
                l = 0
                r = COLS-1

                while l <= r:
                    m = (l + r) // 2
                    if matrix[row][m] > target:
                        r = m -1
                    elif matrix[row][m] < target:
                        l = m+1
                    else:
                        return True
        
        return False