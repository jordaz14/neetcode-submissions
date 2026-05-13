class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0

        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                sum_of_area = (j - i) * min(heights[i], heights[j])
                max_area = max(max_area, sum_of_area)

        return max_area