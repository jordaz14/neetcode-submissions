class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {} # num, idx

        for i in range(len(numbers)):
            compl = target - numbers[i]

            if compl in seen:
                return [seen[compl]+1, i+1]
            else:
                seen[numbers[i]] = i

        return []