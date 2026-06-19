class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum_price = float("inf")
        maximum_profit =0
        n = len(prices)
        for i in range(0,n):
            minimum_price = min(minimum_price,prices[i])
            maximum_profit = max(maximum_profit,prices[i]-minimum_price)
        return maximum_profit