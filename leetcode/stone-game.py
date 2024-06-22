from lc import *

# https://leetcode.com/problems/stone-game/discuss/154610/DP-or-Just-return-true

class Solution:
    def stoneGame(self, p: List[int]) -> bool:
        n = len(p)
        dp = [[0] * n for i in range(n)]
        for i in range(n): dp[i][i] = p[i]
        for d in range(1, n):
            for i in range(n - d):
                dp[i][i + d] = max(p[i] - dp[i + 1][i + d], p[i + d] - dp[i][i + d - 1])
        return dp[0][-1] > 0

# simplify to 1D dp

class Solution:
    def stoneGame(self, p: List[int]) -> bool:
        n = len(p)
        dp = p[:]
        for d in range(1, n):
            for i in range(n - d):
                dp[i] = max(p[i] - dp[i + 1], p[i + d] - dp[i])
        return dp[0] > 0

# recursive

class Solution:
    def stoneGame(self, p: List[int]) -> bool:
        return(k:=sum(p))<2*(f:=cache(lambda i,j,k:i<j and max(k-f(i+1,j,k-p[i]),k-f(i,j-1,k-p[j]))or p[i]))(0,len(p)-1,k)

# https://leetcode.com/problems/stone-game
# shortest solution, except strictly-palindromic-number

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return 1

test('''
877. Stone Game
Medium

3132

2843

Add to List

Share
Alice and Bob play a game with piles of stones. There are an even number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].

The objective of the game is to end with the most stones. The total number of stones across all the piles is odd, so there are no ties.

Alice and Bob take turns, with Alice starting first. Each turn, a player takes the entire pile of stones either from the beginning or from the end of the row. This continues until there are no more piles left, at which point the person with the most stones wins.

Assuming Alice and Bob play optimally, return true if Alice wins the game, or false if Bob wins.

 

Example 1:

Input: piles = [5,3,4,5]
Output: true
Explanation: 
Alice starts first, and can only take the first 5 or the last 5.
Say she takes the first 5, so that the row becomes [3, 4, 5].
If Bob takes 3, then the board is [4, 5], and Alice takes 5 to win with 10 points.
If Bob takes the last 5, then the board is [3, 4], and Alice takes 4 to win with 9 points.
This demonstrated that taking the first 5 was a winning move for Alice, so we return true.
Example 2:

Input: piles = [3,7,2,3]
Output: true
 

Constraints:

2 <= piles.length <= 500
piles.length is even.
1 <= piles[i] <= 500
sum(piles[i]) is odd.
Accepted
221,796
Submissions
314,997
''')
