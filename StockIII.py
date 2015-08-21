class Solution:
  # @param prices, a list of integer
  # @return an integer
  def maxProfit(self, prices):
    # Solve problem going backwards.
    if not prices:
      return 0
    tail_max_profit = [0 for _ in range(len(prices))]
    max_from_tail = prices[-1]
    max_profit_from_tail = 0
    for i in range(len(prices) - 2, -1, -1):
      cost = prices[i]
      max_from_tail = max(max_from_tail, cost)
      max_profit_from_tail = max(max_profit_from_tail, max_from_tail - cost)
      tail_max_profit[i] = max_profit_from_tail
      print 'cost %d, max from tail %d, max profit from tail %d' %(cost,max_from_tail,max_profit_from_tail)

      print tail_max_profit
    # print tail_max_profit
    
    # Solve problem going forward.
    min_from_head = prices[0]
    max_profit_from_head = 0
    
    # Max profit from two transactions.
    max_profit_2 = max_profit_from_head + tail_max_profit[0]
    for i in range(1, len(prices) - 1):
      cost = prices[i]
      min_from_head = min(min_from_head, cost)
      max_profit_from_head = max(max_profit_from_head, cost - min_from_head)

      max_profit_2 = max(
          max_profit_2, max_profit_from_head + tail_max_profit[i]) 

    return max_profit_2
      

# print Solution().maxProfit([])      
print Solution().maxProfit([2,1,2,0,1])