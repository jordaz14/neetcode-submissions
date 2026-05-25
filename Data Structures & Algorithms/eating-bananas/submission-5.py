class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        ans = float("inf")

        while l <= r:
            k = (l + r) // 2

            time_needed = 0
            for i in range(len(piles)):
                time_needed += math.ceil(piles[i] / k)

            if time_needed <= h:
                ans = min(ans, k)
                r = k - 1
            else:
                l = k + 1

        return ans
