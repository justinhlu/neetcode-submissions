class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            match(c):
                case ')':
                    if stack:
                        if stack.pop() != '(':
                            return False
                    else:
                        return False
                case ']':
                    if stack:
                        if stack.pop() != '[':
                            return False
                    else:
                        return False
                case '}':
                    if stack:
                        if stack.pop() != '{':
                            return False
                    else:
                        return False
                case _:
                    stack.append(c)
        if stack:
            return False
        else:
            return True
