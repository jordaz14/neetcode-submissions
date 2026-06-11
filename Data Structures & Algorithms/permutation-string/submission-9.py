from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        need = Counter(s1)
        window = Counter(s2[:len(s1)])

        if need == window: return True

        for r in range(len(s1), len(s2)):
            window[s2[r]] += 1
            left = s2[r - len(s1)]
            window[left] -= 1
            if window[left] == 0:
                del window[left]
            if need == window: return True

        return False
            