class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            num_sums = numbers[l] + numbers[r]

            if num_sums == target:
                return [l+1, r+1]

            elif num_sums > target:
                r -= 1

            else:
                l += 1
        
        return []
            