class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStr = []
        for string in strs: 
            numChars = len(string)
            encodedStr.append(str(numChars))
            encodedStr.append("#")
            encodedStr.append(string)
        
        print(''.join(encodedStr))

        return ''.join(encodedStr)


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            numCharsBuilder = []
            while s[i] != '#':
                numCharsBuilder.append(s[i])
                i += 1
            numChars = int(''.join(numCharsBuilder)) + 1
            resString = s[i+1:i+numChars]
            res.append(resString)
            i += numChars

        return res

        