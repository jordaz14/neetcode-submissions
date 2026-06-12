from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans = ""
        for i in range(len(s)):
            sub = [s[i]]
            for j in range(i+1, len(s)):
                sub.append(s[j])

                if Counter(t) <= Counter(sub):
                    if ans == "" or len(sub) < len(ans):
                        ans = "".join(sub)

        return ans