class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        stack = [] #[(idx, height), ...]

        for i in range(len(heights)):
            start = i
            while stack and heights[i] < stack[-1][-1]:
                idx, height = stack.pop()
                ans = max(ans, (height * (i - idx)))
                start = idx
            stack.append((start, heights[i]))

        for start, h in stack:
            ans = max(ans, (h * (len(heights) - start)))
        
        return ans