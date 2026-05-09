class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0

        counter = [0] * (max(nums) + 1)
        
        for num in nums:
            counter[num] = 1
        
        max_range = 0
        l, r = 0, 0

        while r < len(counter):
            if counter[r] == 0:
                max_range = max((r-l), max_range)
                l = r + 1

            r += 1

        max_range = max((r-l), max_range)
        return max_range



