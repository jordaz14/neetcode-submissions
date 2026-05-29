class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length, l = 0, 0
        sub_str = []

        for r in range(len(s)):
            sub_str.append(s[r])

            if len(sub_str) == len(set(sub_str)):
                max_length = max(max_length, len(sub_str))
            else:
                l = r
                sub_str = [s[l]]

        return max_length

