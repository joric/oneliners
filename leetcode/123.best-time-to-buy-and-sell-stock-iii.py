from lc import *

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b1, b2, p1, p2 = -inf, -inf, 0, 0
        for p in prices:
            b1 = max(b1, -p)
            p1 = max(p1, p + b1)
            b2 = max(b2, p1 - p)
            p2 = max(p2, b2 + p)
        return p2

class Solution: 
    def maxProfit(self, p: List[int]) -> int:
        return(f:=cache(lambda i,b,k:k<4 and i<len(p)and max(b*p[i]+f(i+1,b*-1,k+1),f(i+1,b,k))or 0))(0,-1,0)

class Solution:
    def maxProfit(self, p: List[int]) -> int:
        a=b=-inf;c=0;return max(x+(b:=max(b,(c:=max(c,x+(a:=max(a,-x))))-x))for x in p)

test('''
123. Best Time to Buy and Sell Stock III
Hard

9770

196

Add to List

Share
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete at most two transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:

Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 105
Accepted
666,373
Submissions
1,354,895
''')
