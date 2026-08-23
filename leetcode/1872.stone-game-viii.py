from lc import *

# https://leetcode.com/problems/stone-game-viii/solutions/6222754/explained-line-by-line-by-bepriyansh-1qbo/?envType=daily-question&envId=2026-08-24

class Solution:
    def stoneGameVIII(self, p: List[int]) -> int:
        n = len(p)
        for i in range(1, n):
            p[i] += p[i-1]
        @cache
        def rec(i):
            if i == n - 2:
                return p[i+1]
            alice_cont = rec(i+1)
            alice_done = p[i+1] - rec(i+1)
            return max(alice_cont, alice_done)
        return rec(0)

class Solution:
    def stoneGameVIII(self, p: List[int]) -> int:
        p=[*accumulate(p)];f=lambda i:p[-1]if i+2==len(p)else max((c:=f(i+1)),p[i+1]-c);return f(0)

class Solution:
    def stoneGameVIII(self, p: List[int]) -> int:
        return(f:=lambda i,p=[*accumulate(p)]:i+2<len(p)and max((c:=f(i+1)),p[i+1]-c)or p[-1])(0)

# https://leetcode.com/problems/stone-game-viii/solutions/8459517/swift-1-line-by-orchidhunter-6s54/?envType=daily-question&envId=2026-08-24

class Solution:
    def stoneGameVIII(self, s: List[int]) -> int:
        return reduce(lambda x,y:max(x,y-x),[*accumulate(s)][-2:0:-1],sum(s))

class Solution:
    def stoneGameVIII(self, s: List[int]) -> int:
        a=p=sum(s);[a:=max(a,(p:=p-x)-a)for x in s[:1:-1]];return a

test('''
1872. Stone Game VIII
Solved
Hard
Topics
premium lock icon
Companies
Hint
Alice and Bob take turns playing a game, with Alice starting first.

There are n stones arranged in a row. On each player's turn, while the number of stones is more than one, they will do the following:

Choose an integer x > 1, and remove the leftmost x stones from the row.
Add the sum of the removed stones' values to the player's score.
Place a new stone, whose value is equal to that sum, on the left side of the row.
The game stops when only one stone is left in the row.

The score difference between Alice and Bob is (Alice's score - Bob's score). Alice's goal is to maximize the score difference, and Bob's goal is the minimize the score difference.

Given an integer array stones of length n where stones[i] represents the value of the ith stone from the left, return the score difference between Alice and Bob if they both play optimally.

 

Example 1:

Input: stones = [-1,2,-3,4,-5]
Output: 5
Explanation:
- Alice removes the first 4 stones, adds (-1) + 2 + (-3) + 4 = 2 to her score, and places a stone of
  value 2 on the left. stones = [2,-5].
- Bob removes the first 2 stones, adds 2 + (-5) = -3 to his score, and places a stone of value -3 on
  the left. stones = [-3].
The difference between their scores is 2 - (-3) = 5.
Example 2:

Input: stones = [7,-6,5,10,5,-2,-6]
Output: 13
Explanation:
- Alice removes all stones, adds 7 + (-6) + 5 + 10 + 5 + (-2) + (-6) = 13 to her score, and places a
  stone of value 13 on the left. stones = [13].
The difference between their scores is 13 - 0 = 13.
Example 3:

Input: stones = [-10,-12]
Output: -22
Explanation:
- Alice can only make one move, which is to remove both stones. She adds (-10) + (-12) = -22 to her
  score and places a stone of value -22 on the left. stones = [-22].
The difference between their scores is (-22) - 0 = -22.
 

Constraints:

n == stones.length
2 <= n <= 105
-104 <= stones[i] <= 104
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
14,656/26.9K
Acceptance Rate
54.5%
Topics
Senior Staff
Array
Math
Dynamic Programming
Minimax
Prefix Sum
Game Theory
Zero-Sum Game
Weekly Contest 242
icon
Companies
Hint 1
Let's note that the only thing that matters is how many stones were removed so we can maintain dp[numberOfRemovedStones]
Hint 2
dp[x] = max(sum of all elements up to y - dp[y]) for all y > x
Similar Questions
Stone Game
Medium
Stone Game II
Medium
Stone Game III
Hard
Stone Game IV
Hard
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
''')
