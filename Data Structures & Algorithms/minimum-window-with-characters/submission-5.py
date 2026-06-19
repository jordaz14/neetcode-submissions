from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCount = Counter(t)

        min_s = ""
        for i in range(len(s)):
            sCount, sStr = Counter(s[i]), [s[i]]
            for j in range(i+1, len(s)):
                sStr.append(s[j])
                sCount[s[j]] += 1
                if tCount <= sCount:
                    if not min_s or len(sStr) < len(min_s):
                        min_s = "".join(sStr)

        return min_s