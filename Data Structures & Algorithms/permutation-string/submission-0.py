from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts = Counter(s1)
        cpy = counts.copy()
        
        for c in s2:
            if c not in cpy or cpy[c] == 0:
                cpy = counts.copy()
                continue
            
            cpy[c] = cpy.get(c) - 1
            if sum(cpy.values()) == 0:
                return True
    
        return False