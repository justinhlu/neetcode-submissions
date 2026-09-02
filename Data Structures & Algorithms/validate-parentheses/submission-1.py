class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            elif char == ')' or char == '}' or char == ']':
                
                if not stack:
                    return False
                else:
                    openerCheck = stack.pop()
                    match(char):
                        case ')':
                            if openerCheck != '(':
                                return False
                        case '}':
                            if openerCheck != '{':
                                return False
                        case ']':
                            if openerCheck != '[':
                                return False
        if len(stack) > 0:
            return False
        else:
            return True