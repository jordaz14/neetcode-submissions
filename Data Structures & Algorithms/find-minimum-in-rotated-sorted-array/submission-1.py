class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        ans = float("inf")

        while l <= r:
            m = (l + r) // 2

            ans = min(ans, nums[m])

            if nums[m] >= nums[l]: # left sorted
                ans = min(ans, nums[l])
                l = m + 1
        
            else: # right sorted
                r = m - 1

        return ans

