class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #nums = [0]*len(prices)
        # Pick minimum number -> and add as much as possible by end of length if found high number than before one, switch 
        maxProfit, minprice = 0, float('inf')
        maxNumber = 0
        
        for price in prices:
            minprice = min(minprice, price)
            maxNumber = price - minprice
            maxProfit = max(maxProfit, maxNumber)
        return maxProfit