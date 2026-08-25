class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l = 0
        r = 1

        while r < len(prices):
            buy = prices[l]
            sell = prices[r]
            if buy < sell:
                pt = sell - buy
                profit = max(pt,profit)
                
            else:
                l = r
            r = r+1
        return profit
                
        