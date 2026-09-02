class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        charDict = set()
        for r in range(len(s)):
            c = s[r]
            
            while l < len(s) and c in charDict:
                charDict.remove(s[l])
                l += 1

            charDict.add(c)

            res = max(res, (r-l+1))

        return res