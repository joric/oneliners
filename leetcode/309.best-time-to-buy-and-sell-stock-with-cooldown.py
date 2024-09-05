from lc import *

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/discuss/75964/1-line-python-dp-solution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return max(reduce(lambda x,y:(lambda r,b,s,v:(max(r,s),max(r-v,b),b+v))(*(*x,y)),prices,(0,-inf,-inf)))

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return max(reduce(lambda x,y:(max(x[0],x[2]),max(x[0]-y,x[1]),x[1]+y),prices,(0,-inf,-inf)))

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/discuss/75940/5-lines-Python-O(n)-time-O(1)-space
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        free = 0
        have = cool = -inf
        for price in prices:
            free, have, cool = max(free, cool), max(have, free - price), have + price
        return max(free, cool)

class Solution:
    def maxProfit(self, s: List[int]) -> int:
        f=0;h=c=-inf;[(h:=max(h,f-p),f:=max(f,c),c:=h+p)for p in s];return max(f,c)

test('''

309. Best Time to Buy and Sell Stock with Cooldown
Medium

7120

238

Add to List

Share
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:

Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]
Example 2:

Input: prices = [1]
Output: 0
 

Constraints:

1 <= prices.length <= 5000
0 <= prices[i] <= 1000

''')
