class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Run binary search on the first column 
        # to determine which row the target is in

        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1
        potentialRow = 0
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]: # -1 in array retrieves last value
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break
        if not (top <= bot):
            return False 

        l, r = 0, len(matrix[potentialRow]) - 1
        potentialRow = (top + bot) // 2
        while l <= r:
            mid = (l +r) // 2
            if target == matrix[potentialRow][mid]:
                return True
            elif target < matrix[potentialRow][mid]:
                r = mid - 1
            else:
                l = mid + 1

        return False

            