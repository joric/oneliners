from Leetcode import *

class Solution1:
    def coinChange(self, coins, amount):
        dp = [inf] * (amount+1)
        dp[0] = 0;
        for coin in coins:
            for i in range(coin, amount+1):
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount]<=amount else -1

class Solution2:
    def coinChange(self, coins, amount):
        return (lambda x:x[-1] if x[-1]<=amount else -1)((lambda a:[a,[a.__setitem__(i,min(a[i],a[i-c]+1)) for c in coins for i in range(c, amount+1)]][0])([0]+[amount+1]*amount))

class Solution3:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def f(n):
            return min([1 + f(n-c) for c in coins]) if n>0 else 0 if n==0 else inf
        x = f(amount)
        return x if x!=inf else -1

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        return (lambda x:x if x!=inf else -1)((f:=cache(lambda n: min(1 + f(n-c) for c in coins) if n>0 else 0 if n==0 else inf))(amount))

test(Solution,'''
322. Coin Change

Medium

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:

Input: coins = [2], amount = 3
Output: -1

Example 3:

Input: coins = [1], amount = 0
Output: 0

Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 10**4
''')
