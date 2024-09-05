from lc import *

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, min_price = 0, inf
        for x in prices:
            min_price = min(min_price, x)
            profit = x - min_price
            max_profit = max(max_profit, profit)
        return max_profit


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m,r = inf, 0
        for x in prices:
            m = min(m,x)
            r = max(r,x-m)
        return r

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return reduce(lambda p,x:(max(p[0],x-(m:=min(p[1],x))),m),prices,[0,inf])[0]

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return (m:=inf,r:=0,[r:=max(r,x-(m:=min(m,x))) for x in prices],r)[3]

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return max(x-y for x,y in zip(prices,list(accumulate(prices,min))))

class Solution:
    def maxProfit(self, p: List[int]) -> int:
        return max(map(sub,p,accumulate(p,min)))

test('''
121. Best Time to Buy and Sell Stock
Easy

23303

740

Add to List

Share
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 10^5
0 <= prices[i] <= 10^4
''')