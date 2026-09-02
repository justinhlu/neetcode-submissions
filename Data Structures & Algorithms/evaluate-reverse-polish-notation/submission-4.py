class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = 0
        stack = []

        for token in tokens:
            match(token):
                case '+':
                    b = stack.pop()
                    a = stack.pop()
                    stack.append((a + b))
                case '-':
                    b = stack.pop()
                    a = stack.pop()
                    stack.append((a - b))
                case '*':
                    b = stack.pop()
                    a = stack.pop()
                    stack.append((a * b))
                case '/':
                    b = stack.pop()
                    a = stack.pop()
                    stack.append((int(float(a / b))))
                case _:
                    stack.append(int(token))
        
        return stack[-1]