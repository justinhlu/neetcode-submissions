class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            match(c):
                case '(' | '[' | '{':
                    stack.append(c)
                case '}':
                    chk = "" if not stack else stack.pop()
                    if chk != "{":
                        return False
                case ']':
                    chk = "" if not stack else stack.pop()
                    if chk != "[":
                        return False
                case ')':
                    chk = "" if not stack else stack.pop()
                    if chk != "(":
                        return False
                case _:
                    return False
        
        if stack:
            return False
        else:
            return True