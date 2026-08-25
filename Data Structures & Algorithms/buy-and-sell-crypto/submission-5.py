class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0

        minprice = prices[0]

        for sell in prices:
            maxP = max(maxP, sell - minprice)
            minprice = min(minprice,sell)
        
        return maxP