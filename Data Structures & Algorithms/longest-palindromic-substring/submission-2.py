class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = 0
        resLen = 1
        
        for i in range(len(s)):
            # Check odd length palindrome
            l = i - 1
            r = i + 1
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    currLen = r - l + 1
                    if currLen > resLen:
                        resLen = currLen
                        res = l
                else:
                    break
                l -= 1
                r += 1
            # Check even length palindrome
            l = i
            r = i+1
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    currLen = r - l + 1
                    if currLen > resLen:
                        resLen = currLen
                        res = l
                else:
                    break
                l -= 1 
                r += 1

        return s[res:res+resLen]