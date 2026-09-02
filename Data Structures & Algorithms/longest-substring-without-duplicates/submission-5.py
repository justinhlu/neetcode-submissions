class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        r = l = 0
        dupeCheck = set()
        while r < len(s):
            if s[r] in dupeCheck:
                dupeCheck.remove(s[l])
                l += 1
            else:
                dupeCheck.add(s[r])
                r += 1
                res = max(res, r-l)
        
        return res