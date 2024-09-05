from lc import *

class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        @cache
        def f(i,k):
            if k==0 or i==0:
                return 0
            r,c,s = f(i-1,k),piles[i-1],0
            for j in range(min(len(c),k)):
                s += c[j]
                r = max(r,s+f(i-1,k-j-1))
            return r
        return f(len(piles),k)

class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        return (f:=cache(lambda i,k:(r:=f(i-1,k),c:=piles[i-1],s:=0,[(s:=s+c[j],r:=max(r,s+f(i-1,k-j-1))) for j in range(min(len(c),k))],r)[-1] if k and i else 0))(len(piles),k)

class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        return (f:=cache(lambda i,k:max(f(i+1,k),max(x+f(i+1,k-j-1) for x,j in zip(accumulate(piles[i]),range(min(len(piles[i]),k))))) if k*(i-len(piles)) else 0))(0,k)

class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        return (f:=cache(lambda i,k:max(f(i+1,k),max(x+f(i+1,k-j-1) for x,j in zip(accumulate(t[i]),range(min(len(t[i]),k))))) if k*(i-len(t:=piles)) else 0))(0,k)

class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        return (f:=cache(lambda i,k:max(f(i+1,k),max(x+f(i+1,k-j-1) for x,j in zip(accumulate(t[i]),range(k)))) if k*(i-len(t:=piles)) else 0))(0,k)

test('''
2218. Maximum Value of K Coins From Piles
Hard

762

13

Add to List

Share
There are n piles of coins on a table. Each pile consists of a positive number of coins of assorted denominations.

In one move, you can choose any coin on top of any pile, remove it, and add it to your wallet.

Given a list piles, where piles[i] is a list of integers denoting the composition of the ith pile from top to bottom, and a positive integer k, return the maximum total value of coins you can have in your wallet if you choose exactly k coins optimally.

 

Example 1:


Input: piles = [[1,100,3],[7,8,9]], k = 2
Output: 101
Explanation:
The above diagram shows the different ways we can choose k coins.
The maximum total we can obtain is 101.
Example 2:

Input: piles = [[100],[100],[100],[100],[100],[100],[1,1,1,1,1,1,700]], k = 7
Output: 706
Explanation:
The maximum total can be obtained if we choose all coins from the last pile.
 

Constraints:

n == piles.length
1 <= n <= 1000
1 <= piles[i][j] <= 105
1 <= k <= sum(piles[i].length) <= 2000
Accepted
14,180
Submissions
29,416
Seen this question in a real interview before?

Yes

No
Coin Change
Medium
Coin Change II
Medium
For each pile i, what will be the total value of coins we can collect if we choose the first j coins?
How can we use dynamic programming to combine the results from different piles to find the most optimal answer?
''')