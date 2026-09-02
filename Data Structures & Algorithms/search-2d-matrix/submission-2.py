class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        for r in range(ROWS):
            if target >= matrix[r][0] and target <= matrix[r][COLS-1]:
                left = 0
                right = COLS-1
                while left <= right:
                    m = (left+right) // 2

                    if matrix[r][m] < target:
                        left = m + 1
                    elif matrix[r][m] > target:
                        right = m - 1
                    else:
                        return True
        
        return False