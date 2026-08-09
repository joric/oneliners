from lc import *

# https://leetcode.com/problems/stone-game-iv/submissions/412896040/

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = not all(dp[i - k * k] for k in range(1, int(i**0.5) + 1))
        return dp[-1]

class Solution:
    @lru_cache(None)
    def winnerSquareGame(self, n: int) -> bool:
        if n == 0: return False
        i = isqrt(n)
        while i >= 1:
            if not self.winnerSquareGame(n - i * i): return True
            i -= 1
        return False

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        return(f:=cache(lambda x:any(1-f(x-i*i)for i in range(1,isqrt(x)+1))))(n)

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        return(f:=cache(lambda x:any(1-f(x-~i*~i)for i in range(isqrt(x)))))(n)

test('''
1510. Stone Game IV
Solved
Hard
Topics
premium lock icon
Companies
Hint
Alice and Bob take turns playing a game, with Alice starting first.

Initially, there are n stones in a pile. On each player's turn, that player makes a move consisting of removing any non-zero square number of stones in the pile.

Also, if a player cannot make a move, he/she loses the game.

Given a positive integer n, return true if and only if Alice wins the game otherwise return false, assuming both players play optimally.

 

Example 1:

Input: n = 1
Output: true
Explanation: Alice can remove 1 stone winning the game because Bob doesn't have any moves.
Example 2:

Input: n = 2
Output: false
Explanation: Alice can only remove 1 stone, after that Bob removes the last one winning the game (2 -> 1 -> 0).
Example 3:

Input: n = 4
Output: true
Explanation: n is already a perfect square, Alice can win with one move, removing 4 stones (4 -> 0).
 

Constraints:

1 <= n <= 105
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
86,277/144.7K
Acceptance Rate
59.6%
Topics
Senior Staff
Math
Dynamic Programming
Minimax
Game Theory
Nim Game
Sprague–Grundy Theorem
Zero-Sum Game
Biweekly Contest 30
icon
Companies
Hint 1
Use dynamic programming to keep track of winning and losing states. Given some number of stones, Alice can win if she can force Bob onto a losing state.
Similar Questions
Stone Game V
Hard
Stone Game VI
Medium
Stone Game VII
Medium
Stone Game VIII
Hard
Stone Game IX
Medium
Stone Removal Game
Easy
''')
