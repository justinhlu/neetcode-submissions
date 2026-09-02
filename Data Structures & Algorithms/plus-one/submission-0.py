class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = "".join(str(digit) for digit in digits)
        integerNum = int(num) + 1
        res = [digit for digit in str(integerNum)]

        return res