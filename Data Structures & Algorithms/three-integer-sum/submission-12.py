class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums.sort()

        for i in range(len(nums)-2):
            l, r = i+1, len(nums)-1

            while l < r:
                num_sums = nums[i] + nums[l] + nums[r]

                if num_sums == 0: 
                    ans.add(tuple(sorted([nums[i], nums[l], nums[r]])))
                    l += 1
                    r -= 1

                elif num_sums > 0:
                    r -= 1

                else:
                    l += 1

        return list(ans)


        