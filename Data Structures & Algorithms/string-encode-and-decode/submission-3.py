class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s
        return res
    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            lenStr = ""
            while s[i] != '#':
                lenStr += s[i]
                i += 1
            lenStr = int(lenStr)

            i += 1
            newStr = ""
            for j in range(lenStr):
                newStr += s[i+j]
            
            res.append(newStr)
            i += lenStr

        return res
