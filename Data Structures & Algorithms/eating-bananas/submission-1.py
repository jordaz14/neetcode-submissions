class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        for k in range(1, 10000000):
            time_needed = 0
            for i in range(len(piles)):
                time_needed += math.ceil(piles[i] / k)
            
            if time_needed <= h:
                return k
        
        return -1
