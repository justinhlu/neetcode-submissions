class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1
        res = []

        while l < r and l >= 0 and r < len(numbers):
            check = numbers[l] + numbers[r]
            
            if check < target:
                l += 1
            elif check > target:
                r -= 1
            else:
                res = [l+1,r+1]
                break

        return res