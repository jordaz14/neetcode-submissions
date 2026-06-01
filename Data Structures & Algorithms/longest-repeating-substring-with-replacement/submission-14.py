from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        sub = []

        for r in range(len(s)):
            sub.append(s[r])
            freqMap = Counter(sub)
            if len(sub) - freqMap.most_common(1)[0][1] <= k:
                ans = max(ans, len(sub))
            else:
                sub.pop(0)
            
        return ans