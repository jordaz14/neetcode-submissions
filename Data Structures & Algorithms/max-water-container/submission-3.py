class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1

        max_sum = 0
        while l < r:
            sum_of_area = (r - l) * min(heights[l], heights[r])
            max_sum = max(max_sum, sum_of_area)

            if heights[l] < heights[r]:
                l += 1
    
            elif heights[l] > heights[r]:
                r -= 1
            
            else:
                l += 1
                r -= 1
            
        
        return max_sum