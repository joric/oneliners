from lc import *

# https://leetcode.com/problems/coin-change-ii/discuss/2049788/Python-Easy-5-line-DP-Solution-Beats-90

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [1]+[0]*amount
        for i in range(len(coins)):
            for j in range(coins[i],len(dp)):
                dp[j]+=dp[j-coins[i]]
        return dp[amount]

class Solution:
    def change(self, a: int, c: List[int]) -> int:
        d=[1]+[0]*a;[setitem(d,j,d[j]+d[j-c[i]])for i in range(len(c))for j in range(c[i],len(d))];return d[a]

# https://leetcode.com/problems/coin-change-ii/discuss/99209/Python-Recursive-Solution-(Slow)

# TLE
class Solution:
    def change(self, a: int, c: List[int]) -> int:
        if a == 0: 
            return 1 
        if a<0 or len(c)==0:
            return 0
        return self.change(a-c[-1],c)+self.change(a,c[:-1])

class Solution:
    def change(self, a: int, c: List[int]) -> int:
        return(f:=cache(lambda a,i:not a or 0 if a<0 or i<0 else f(a-c[i],i)+f(a,i-1)))(a,len(c)-1)

test('''
518. Coin Change II
Medium

7740

137

Add to List

Share
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.

 

Example 1:

Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
Example 3:

Input: amount = 10, coins = [10]
Output: 1

Example 4:
Input: amount = 0, coins = [7]
Output: 1


Constraints:

1 <= coins.length <= 300
1 <= coins[i] <= 5000
All the values of coins are unique.
0 <= amount <= 5000
''')

