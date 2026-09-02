class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = 0
        stack = []
        for token in tokens:
            match(token):
                case '+':
                    b = stack.pop()
                    a = stack.pop()
                    chk = a + b
                    stack.append(chk)
                case '-':
                    b = stack.pop()
                    a = stack.pop()
                    chk = a - b
                    stack.append(chk)
                case '*':
                    b = stack.pop()
                    a = stack.pop()
                    chk = a * b
                    stack.append(chk)
                case '/':
                    b = stack.pop()
                    a = stack.pop()
                    chk = int(float(a / b))
                    stack.append(chk)

                case _:
                    stack.append(int(token))
        
        return stack[-1]
