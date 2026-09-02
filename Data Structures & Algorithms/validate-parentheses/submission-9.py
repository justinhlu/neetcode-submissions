class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            match(c):
                case '(' | '[' | '{':
                    stack.append(c)
                case ')' if stack:
                    chk = stack.pop()
                    if chk != '(':
                        return False
                case ']' if stack:
                    chk = stack.pop()
                    if chk != '[':
                        return False
                case '}' if stack:
                    chk = stack.pop()
                    if chk != '{':
                        return False
                case _:
                    return False

        if stack:
            return False
        else:
            return True 
