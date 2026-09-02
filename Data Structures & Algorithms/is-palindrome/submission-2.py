class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        parsedStr = "".join(c for c in s.lower() if c.isalnum())
        l = 0
        r = len(parsedStr) - 1
        while l <= r:
            if parsedStr[l] != parsedStr[r]:
                return False
            l += 1
            r -= 1
        return True
