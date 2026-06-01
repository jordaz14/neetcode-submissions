class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        for i in range(len(s)):
            sub = []
            for j in range(i, len(s)):
                sub.append(s[j])
                max_freq = max(sub, key=sub.count)
                if (len(sub) - sub.count(max_freq)) <= k:
                    ans = max(ans, len(sub))
                else:
                    break
        return ans
    