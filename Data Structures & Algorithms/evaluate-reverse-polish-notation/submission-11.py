class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i].isdigit():
                stack.append(tokens[i])
            else:
                digit2, digit1 = stack.pop(), stack.pop()
                stack.append(int(eval(f"{digit1}{tokens[i]}{digit2}")))

        return stack.pop()
