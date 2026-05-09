class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        max_range, sub_range = 0, 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            elif nums[i] - nums[i-1] == 1:
                sub_range += 1
            else:
                sub_range = 1

            max_range = max(max_range, sub_range)

        return max_range


