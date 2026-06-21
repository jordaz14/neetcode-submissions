class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        for i in range(len(nums)):
            window = [nums[i]]
            for j in range(i+1, len(nums)):
                if len(window) == k:
                    ans.append(max(window))
                    break
                
                window.append(nums[j])

        ans.append(max(window))
        
        return ans
                
