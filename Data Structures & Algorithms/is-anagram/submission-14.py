
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        freqMap = {}
        for c in s:
            freqMap[c] = freqMap.get(c, 0) + 1
    
        for c in t:
            freqMap[c] = freqMap.get(c, 0) - 1
        
        for val in freqMap.values():
            if val != 0: return False

        return True