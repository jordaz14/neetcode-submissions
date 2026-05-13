class Solution:
    def isValid(self, s: str) -> bool:
        if not s: return True

        compl = {
            "}" : "{",
            ")" : "(",
            "]" : "["
        }

        stack = []
        for c in s:
            if c in compl:
                if not stack or stack[-1] != compl[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)

        return not stack