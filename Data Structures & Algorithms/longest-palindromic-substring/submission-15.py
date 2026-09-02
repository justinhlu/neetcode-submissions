class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = 0
        resLen = 0

        if len(s) == 1:
            return s

        for i in range(len(s)):
            # Check odd length palindrome
            l = i 
            r = i 

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if resLen < (r-l)+1:
                    resLen = (r-l)+1
                    res = l
                l -= 1
                r += 1

            # Check even length palindrome
            l = i
            r = i+1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if resLen < (r-l)+1:
                    resLen = (r-l)+1
                    res = l
                l -= 1
                r += 1

        return s[res:res+resLen]