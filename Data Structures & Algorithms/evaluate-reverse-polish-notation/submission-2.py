class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            match(token):
                case '+':
                    if len(stack) >= 2:
                        op1 = stack.pop()
                        op2 = stack.pop()
                        sum = op1 + op2
                        stack.append(sum)
                case '-':
                    if len(stack) >= 2:
                        op1 = stack.pop()
                        op2 = stack.pop()
                        diff = op2 - op1
                        stack.append(diff)
                case '*':
                    if len(stack) >= 2:
                        op1 = stack.pop()
                        op2 = stack.pop()
                        product = op1 * op2
                        stack.append(product)
                case '/':
                    if len(stack) >= 2:
                        op1 = stack.pop()
                        op2 = stack.pop()
                        quotient = int(float(op2) / op1)
                        stack.append(quotient)
                case _:
                    stack.append(int(token))
        
        return stack[0]
