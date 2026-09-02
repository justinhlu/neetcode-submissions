class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charDict = {}
        maxf = 0

        l, r = 0, 0

        for r in range(len(s)):
            c = s[r]
            charDict[s[r]] = 1 + charDict.get(s[r], 0)
            maxf = max(maxf, charDict.get(s[r], 0))

            if (r-l+1) - maxf > k:
                charDict[s[l]] -= 1
                l += 1

        return (r-l+1)
