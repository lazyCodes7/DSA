class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        low = prices[0]
        
        profit = 0
        
        for i in range(1, len(prices)):
            
            if(low>prices[i]):
                low = prices[i]
            
            if(prices[i] - low > profit):
                profit = prices[i] - low
        return profit
