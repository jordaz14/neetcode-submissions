class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0

        for i in range(len(s)):
            sub_str = [s[i]]
            for j in range(i+1, len(s)):
                if s[j] in sub_str:
                    break
                sub_str.append(s[j])
            max_length = max(max_length, len(sub_str))

        return max_length