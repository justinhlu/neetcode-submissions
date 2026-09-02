class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = 0
        resLen = 1

        for i in range(len(s)):
            # Check odd length palindrome
            l = i-1
            r = i+1

            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    paliLength = r-l+1
                    if paliLength > resLen:
                        resLen = paliLength
                        res = l
                    r += 1
                    l -= 1

                else:
                    break
            
            # Check even length palindrome
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and l < r:
                if s[l] == s[r]:
                    
                    paliLength = r-l+1
                    if paliLength > resLen:
                        resLen = paliLength
                        res = l
                    r += 1
                    l -= 1
                else:
                    break

        return s[res:res+resLen]