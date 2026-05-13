class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, 1

        max_sum = 0
        while r < len(heights):
            sum_of_area = (r - l) * min(heights[l], heights[r])
            max_sum = max(max_sum, sum_of_area)

            if heights[r] > heights[l]:
                l = r
            
            r += 1
        
        return max_sum