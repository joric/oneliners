from lc import *

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/discuss/567595/Python-DP-one-line-ish

class Solution:
    def maxProfit(self, p: List[int], f: int) -> int:
        o,d=-p[0],0
        for x in p:
            o,d=max(o,d-x),max(d,o+x-f)
        return d

class Solution:
    def maxProfit(self, p: List[int], f: int) -> int:
        o,d=-p[0],0;[(o:=max(o,d-x),d:=max(d,o+x-f))for x in p];return d

test('''
714. Best Time to Buy and Sell Stock with Transaction Fee
Medium

5418

133

Add to List

Share
You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee representing a transaction fee.

Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:

Input: prices = [1,3,2,8,4,9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
- Buying at prices[0] = 1
- Selling at prices[3] = 8
- Buying at prices[4] = 4
- Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
Example 2:

Input: prices = [1,3,7,5,10,3], fee = 3
Output: 6
 

Constraints:

1 <= prices.length <= 5 * 10^4
1 <= prices[i] < 5 * 10^4
0 <= fee < 5 * 10^4
Accepted
235,889
Submissions
359,238
Seen this question in a real interview before?

Yes

No
Consider the first K stock prices. At the end, the only legal states are that you don't own a share of stock, or that you do. Calculate the most profit you could have under each of these two cases.
''')

