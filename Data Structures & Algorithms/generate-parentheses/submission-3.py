class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []

        def backtrack(cur, open, close):
            if n == open == close:
                output.append("".join(cur.copy()))
                return
            
            if close < open:
                cur.append(")")
                backtrack(cur, open, close + 1)
                cur.pop()
            
            if open < n:
                cur.append("(")
                backtrack(cur, open+1, close)
                cur.pop()
            
            return 
        
        backtrack([], 0,0)

        return output