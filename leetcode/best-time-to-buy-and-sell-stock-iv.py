from Leetcode import *

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/discuss/2555929/python-oneliner-dfs-with-a-cache-decorator


class Solution1:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        @cache
        def dfs(i, k, sell):
            return 0 if k==0 or i==len(prices) else max(dfs(i+1, k-1, 0) + prices[i], dfs(i+1, k, 1)) if sell else max(dfs(i+1, k, 1)-prices[i], dfs(i+1, k, sell))
        return dfs(0, k, 0)

class Solution2:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        @cache
        def dfs(i, k, sell):
            return 0 if k==0 or i==len(prices) else max(dfs(i+1, k-sell, 1-sell) + prices[i] * (2*sell-1), dfs(i+1, k, sell))
        return dfs(0, k, 0)

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        return (f:=cache(lambda i,k,s:0 if k==0 or i==len(prices) else max(f(i+1,k-s,1-s)+prices[i]*(2*s-1),f(i+1,k,s))))(0,k,0)

test(Solution,'''
188. Best Time to Buy and Sell Stock IV
Hard

5771

190

Add to List

Share
You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.

Find the maximum profit you can achieve. You may complete at most k transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:

Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
Example 2:

Input: k = 2, prices = [3,2,6,5,0,3]
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
 

Constraints:

1 <= k <= 100
1 <= prices.length <= 1000
0 <= prices[i] <= 1000
''')