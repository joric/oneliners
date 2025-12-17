from lc import *

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-v/solutions/6820567/javacpython-dp-ok-space-by-lee215-zolx/?envType=daily-question&envId=2025-12-17

class Solution:
    def maximumProfit(self, p: List[int], k: int) -> int:
        bought = [-inf] * k
        res = [0] * (k + 1)
        sold = [0] * k
        for x in p:
            for j in range(k, 0, -1):
                res[j] = max(res[j], bought[j - 1] + x, sold[j - 1] - x)
                bought[j - 1] = max(bought[j - 1], res[j - 1] - x)
                sold[j - 1] = max(sold[j - 1], res[j - 1] + x)
        return max(res)

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-v/solutions/7079325/python-recursive-dfs-with-cache-dp-with-6w8oh/?envType=daily-question&envId=2025-12-17

class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        f = [[-inf] * 3 for _ in range(k + 2)]
        for j in range(1, k + 2):
            f[j][0] = 0
        for p in prices:
            for j in range(k + 1, 0, -1): # loop j backwards guarantees f[j][1], f[j-1][0] to be yesterday's value
                f[j][0] = max(f[j][0], f[j][1] + p, f[j][2] - p)
                f[j][1] = max(f[j][1], f[j-1][0] - p)
                f[j][2] = max(f[j][2], f[j-1][0] + p)
        return f[-1][0]

class Solution:
    def maximumProfit(self, p: List[int], k: int) -> int:
        @cache
        def f(i, j, e):
            if j < 0:
                return -inf
            if i < 0:
                return -inf if e else 0
            if e == 0:
                return max(f(i-1,j,0),f(i-1,j,1)+p[i],f(i-1,j,2)-p[i])
            if e == 1:
                return max(f(i-1,j,1),f(i-1,j-1,0)-p[i])
            else:
                return max(f(i-1,j,2),f(i-1,j-1,0)+p[i])
        r = f(len(p)-1, k, 0)
        f.cache_clear()
        return r

class Solution:
    def maximumProfit(self, p: List[int], k: int) -> int:
        @cache
        def f(i,j,e):
            if j < 0:
                return -inf
            if i < 0:
                return -inf if e else 0
            return max(f(i-1,j,e),f(i-1,j-1,0)+p[i]*(1,-1)[e<2])if e else max(f(i-1,j,0),f(i-1,j,1)+p[i],f(i-1,j,2)-p[i])
        return(f(len(p)-1,k,0),f.cache_clear())[0]

class Solution:
    def maximumProfit(self, p: List[int], k: int) -> int:
        f=cache(lambda i,j,e:(max(f(i-1,j,e),f(i-1,j-1,0)+p[i]*(1,-1)[e<2])if e else max(f(i-1,j,0),f(i-1,j,1)+p[i],f(i-1,j,2)-p[i]))if i>-1<j else(-inf,0)[e<=0<=j]);return(f(len(p)-1,k,0),f.cache_clear())[0]

test('''
3573. Best Time to Buy and Sell Stock V
Medium
Topics
premium lock icon
Companies
Hint
You are given an integer array prices where prices[i] is the price of a stock in dollars on the ith day, and an integer k.

You are allowed to make at most k transactions, where each transaction can be either of the following:

Normal transaction: Buy on day i, then sell on a later day j where i < j. You profit prices[j] - prices[i].

Short selling transaction: Sell on day i, then buy back on a later day j where i < j. You profit prices[i] - prices[j].

Note that you must complete each transaction before starting another. Additionally, you can't buy or sell on the same day you are selling or buying back as part of a previous transaction.

Return the maximum total profit you can earn by making at most k transactions.

 

Example 1:

Input: prices = [1,7,9,8,2], k = 2

Output: 14

Explanation:

We can make $14 of profit through 2 transactions:
A normal transaction: buy the stock on day 0 for $1 then sell it on day 2 for $9.
A short selling transaction: sell the stock on day 3 for $8 then buy back on day 4 for $2.
Example 2:

Input: prices = [12,16,19,19,8,1,19,13,9], k = 3

Output: 36

Explanation:

We can make $36 of profit through 3 transactions:
A normal transaction: buy the stock on day 0 for $12 then sell it on day 2 for $19.
A short selling transaction: sell the stock on day 3 for $19 then buy back on day 4 for $8.
A normal transaction: buy the stock on day 5 for $1 then sell it on day 6 for $19.


Other examples:

Input: prices = [20,19,12,10,5,10,9], k = 1
Output: 15

Input: prices = [8,1,7,4,6,16,6,1,13,18], k = 3
Output: 36

Input: prices = [14,16,5,11,20], k = 2
Output: 20

Constraints:

2 <= prices.length <= 103
1 <= prices[i] <= 109
1 <= k <= prices.length / 2
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
24,855/52.9K
Acceptance Rate
47.0%
Topics
Array
Dynamic Programming
Biweekly Contest 158
icon
Companies
Hint 1
Use dynamic programming.
Hint 2
Keep the following states: idx, transactionsDone, transactionType, isTransactionRunning.
Hint 3
Transactions transition from completed -> running and from running -> completed.
Similar Questions
Best Time to Buy and Sell Stock
Easy
''')
