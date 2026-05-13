class Solution:
    def trap(self, height: List[int]) -> int:
        max_water = 0
        for i in range(len(height)):
            max_l, max_r = 0, 0
            for j in range(len(height)):
                if i == j: continue

                elif j < i: 
                    max_l = max(max_l, height[j])

                else:
                    max_r = max(max_r, height[j])
            
            max_water += max(min(max_l, max_r) - height[i],0)
            
        return max_water
        



                

                
