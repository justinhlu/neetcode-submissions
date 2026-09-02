class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s))
            res += '#'
            res += s
        return res
    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            lenStr = ""

            while s[i] != "#":
                lenStr += s[i]
                i += 1
                
            length = int(lenStr)
            i += 1
            currStr = ""
            for j in range(length):
                currStr += s[i+j]
            res.append(currStr)
            i+=length
        return res            


