class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)

        max_range = 0
        for num in num_set:
            sub_range = 1
            if num - 1 not in num_set:
                while num + 1 in num_set:
                    sub_range += 1
                    num += 1

            max_range = max(max_range, sub_range)

        return max_range
                                
                    


