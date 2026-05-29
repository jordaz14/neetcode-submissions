class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        p1 = 0

        for p2 in range(1, len(prices)):
            profit = max(profit, prices[p2] - prices[p1])

            if prices[p2] < prices[p1]:
                p1 = p2

        return profit