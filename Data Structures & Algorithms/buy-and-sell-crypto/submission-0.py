
# buy pointer, sell pointer (initialize 0, 1)
# look at price diff, if not zero and better than max_so_far, we update 

# Then, shift the sell pointer up -> its lower than the buy pointer -> shift the buy pointer up 

# [10, 1, 5, 6, 7, 1]
# buy -> 10, sell -> 1  


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_so_far = 0 

        # Different days 
        buy = 0 
        sell = 1 

        while buy < n and sell < n: 
            buy_price = prices[buy]
            sell_price = prices[sell]

            # Found our new low 
            if sell_price < buy_price: 
                buy = sell
                sell += 1
                
            else: 
                profit = sell_price - buy_price 
                max_so_far = max(profit, max_so_far)
                sell += 1

        return max_so_far 

        