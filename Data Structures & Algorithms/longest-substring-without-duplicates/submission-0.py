class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        charMap = {}
        l, r = 0, 0

        while r < len(s):
            while s[r] in charMap:
                del charMap[s[l]]
                l+=1
            charMap[s[r]] = r
            res = max(res, (r-l + 1))
            r += 1
        
        return res
