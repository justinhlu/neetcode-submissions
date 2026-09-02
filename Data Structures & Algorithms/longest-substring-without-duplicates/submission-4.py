class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        resLen = 0
    
        dupeCheck = set()
        l = r = 0

        while r < len(s):
            if s[r] in dupeCheck:
                dupeCheck.remove(s[l])
                l += 1
            else:
                dupeCheck.add(s[r])
                r += 1
                resLen = max(resLen, r - l)


        return resLen