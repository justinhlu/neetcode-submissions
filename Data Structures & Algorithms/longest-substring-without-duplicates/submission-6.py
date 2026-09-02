class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charDict = set()
        res = 0
        l = 0

        for r in range(len(s)):

            while l < len(s) and s[r] in charDict:
                charDict.remove(s[l])
                l += 1

            charDict.add(s[r])

            
            res = max(res, (r-l+1))
            
        
        return res