class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            l, r = i+1, len(nums)-1

            while l < r:
                num_sums = nums[i] + nums[l] + nums[r]

                if num_sums == 0: 
                    ans.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]: l += 1
                    while l < r and nums[r] == nums[r-1]: r -= 1
                    l += 1
                    r -= 1

                elif num_sums > 0:
                    r -= 1

                else:
                    l += 1

        return ans


        