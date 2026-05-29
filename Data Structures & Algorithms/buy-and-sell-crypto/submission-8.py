class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, stack = 0, []

        for i in range(len(prices)):
            if not stack or prices[i] < stack[-1]:
                stack.append(prices[i])

            profit = max(profit, prices[i] - stack[-1])

        return profit