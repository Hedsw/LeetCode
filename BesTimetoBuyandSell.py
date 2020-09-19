class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        answer = 0
        for i in range(1,length):
            answer += max(prices[i]-prices[i-1], 0)
            
        return answer
        


# New Solution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxValue = 0
        length = len(prices)
        for i in range(1, length):
            if prices[i] > prices[i-1]:
                maxValue = maxValue + prices[i] - prices[i-1]
                
        return maxValue