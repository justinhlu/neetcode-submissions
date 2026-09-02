class Solution:
    def isPalindrome(self, s: str) -> bool:
        parsedStr = ''.join([char for char in s if char.isalnum()]).lower()
        l = 0
        r = len(parsedStr)-1

        while l <= r:
            if parsedStr[l] != parsedStr[r]:
                return False

            l += 1
            r -= 1
        
        return True
