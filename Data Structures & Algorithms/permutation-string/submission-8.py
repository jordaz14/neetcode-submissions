class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        if len(s1) == 1 and s1 in s2: return True

        for i in range(len(s2)):
            sub = [s2[i]]
            for j in range(i+1, len(s2)):      
                sub.append(s2[j])

                if len(sub) == len(s1):
                    if "".join(sorted(sub)) == "".join(sorted(s1)):
                        return True

        return False
                

            
            