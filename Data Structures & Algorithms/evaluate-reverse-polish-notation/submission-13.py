class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            token = tokens[i][1:] if tokens[i][0] == "-" and len(tokens[i]) > 1 else tokens[i]
            if token.isdigit():
                stack.append(tokens[i])
            else:
                digit2, digit1 = stack.pop(), stack.pop()
                stack.append(int(eval(f"{digit1}{tokens[i]}{digit2}")))

        return int(stack.pop())
