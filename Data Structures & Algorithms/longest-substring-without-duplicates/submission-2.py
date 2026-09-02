class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charMap = {}

        l = r = 0
        res = 0
        while r < len(s):
            if s[r] in charMap:
                # increment the left counter until no more dupes in map
                while s[r] in charMap:
                    del charMap[s[l]]
                    l += 1

            charMap[s[r]] = s[r]
           
            res = max(res, (r-l) + 1)
            r += 1

        return res