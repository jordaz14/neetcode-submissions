class Solution:
    def isValid(self, s: str) -> bool:
        if not s: return False

        compl = {
            "}" : "{",
            ")" : "(",
            "]" : "["
        }

        stack = []
        for c in s:
            if not stack:
                stack.append(c)
                continue
            
            if stack and stack[-1] == compl.get(c):
                stack.pop()

            elif stack:
                stack.append(c)

        return not stack