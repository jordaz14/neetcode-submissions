class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        freqMap1 = {}
        freqMap2 = {}

        for c in s:
            freqMap1[c] = freqMap1.get(c, 0) + 1

        for c in t:
            freqMap2[c] = freqMap2.get(c, 0) + 1 

        for c in s:
            if freqMap1.get(c) != freqMap2.get(c): return False

        return True