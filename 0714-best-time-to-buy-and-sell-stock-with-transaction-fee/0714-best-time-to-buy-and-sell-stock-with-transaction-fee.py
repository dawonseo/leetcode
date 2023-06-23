class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        
        free = [0 for _ in range(n)]
        hold = [0 for _ in range(n)]
        
        hold[0] = -prices[0]
        
        for i in range(1, n):
            free[i] = max(free[i - 1], hold[i - 1] + prices[i] - fee)
            hold[i] = max(hold[i - 1], free[i - 1] - prices[i])
        
        return free[-1]