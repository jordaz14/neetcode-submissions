class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0

        for i in range(len(heights)):
            h, w = heights[i], 1
            ans = max((h*w), ans)

            for r in range(i+1, len(heights), 1):
                h = min(h, heights[r])
                w += 1
                ans = max((h*w), ans)

        return ans