class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        answer = 0
        for i in range(1,length):
            answer += max(prices[i]-prices[i-1], 0)
            
        return answer
        
        