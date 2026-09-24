class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        oper = "/+-*"
        stack = []
        result = 0

        for i, c in enumerate(tokens):
            if c not in oper:
                stack.append(c)
            else:
                n2 = int(stack.pop())
                n1 = int(stack.pop())
                if c == "+":
                    stack.append(n1 + n2)
                elif c == "-":
                    stack.append(n1 - n2)
                elif c == "/":
                    stack.append(int(n1 / n2))
                else:
                    stack.append(n1 * n2)
                # stack = stack[2:]
        return int(stack[-1])

