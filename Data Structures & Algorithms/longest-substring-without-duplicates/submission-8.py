class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length, l = 0, 0
        sub_str = []

        for r in range(len(s)):
            sub_str.append(s[r])

            while len(sub_str) != len(set(sub_str)):
                sub_str.pop(0)
                l += 1

            max_length = max(max_length, len(sub_str))

        return max_length

