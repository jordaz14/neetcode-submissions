from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t: return ""

        countT = Counter(t)
        window = defaultdict(int)
        have, need = 0, len(countT)
        res, resLen = (0,0), float("inf")
        l = 0

        for r, c in enumerate(s):
            window[c] += 1
            if c in countT and window[c] == countT[c]:
                have += 1
            
            while have == need:
                if r - l + 1 < resLen:
                    res, resLen = (l, r), r - l + 1
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        
        return s[res[0]:res[1] + 1] if resLen != float('inf') else ""