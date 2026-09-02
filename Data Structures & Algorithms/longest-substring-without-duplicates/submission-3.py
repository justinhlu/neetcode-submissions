class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charMap = set()
        l = 0
        r = 0
        res = 0
        if len(s) == 0:
            return res
        
        while l <= r and r < len(s):
            if s[r] in charMap:
                while s[r] in charMap:
                    charMap.remove(s[l])
                    l += 1
            
            charMap.add(s[r])
            res = max(res, r-l+1)
            
            r += 1
        
        return res

