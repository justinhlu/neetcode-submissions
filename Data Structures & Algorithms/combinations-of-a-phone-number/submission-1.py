class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return [] 
            
        res = []

        digitMap = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

        def backtrack(i, cur):
            if i == len(digits):
                res.append("".join(cur))
                return
            if i > len(digits):
                return
            
            for char in digitMap[digits[i]]:
                cur.append(char)
                backtrack(i+1, cur)
                cur.pop()
            
            return
        
        backtrack(0, [])

        return res