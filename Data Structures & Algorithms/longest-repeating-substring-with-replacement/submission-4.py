class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if s == "":
            return 0

        res = 0
        freqDict = {}
        maxf = 0
        
        l = 0
        for r in range(len(s)):
            c = s[r]
            freqDict[c] = 1 + freqDict.get(c, 0)
            maxf = max(maxf, freqDict[c])

            if (r-l+1) - maxf > k:
                freqDict[s[l]] -= 1
                l += 1

        return (r-l+1)