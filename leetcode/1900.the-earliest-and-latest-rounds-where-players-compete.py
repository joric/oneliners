from lc import *

# https://leetcode.com/problems/the-earliest-and-latest-rounds-where-players-compete/editorial/?envType=daily-question&envId=2025-07-12

class Solution:
    def earliestAndLatest(
        self, n: int, firstPlayer: int, secondPlayer: int
    ) -> List[int]:
        @cache
        def dp(n: int, f: int, s: int) -> (int, int):
            if f + s == n + 1:
                return (1, 1)

            # F(n,f,s)=F(n,n+1-s,n+1-f)
            if f + s > n + 1:
                return dp(n, n + 1 - s, n + 1 - f)

            earliest, latest = float("inf"), float("-inf")
            n_half = (n + 1) // 2

            if s <= n_half:
                # s On the left or in the middle
                for i in range(f):
                    for j in range(s - f):
                        x, y = dp(n_half, i + 1, i + j + 2)
                        earliest = min(earliest, x)
                        latest = max(latest, y)
            else:
                # s on the right
                # s'
                s_prime = n + 1 - s
                mid = (n - 2 * s_prime + 1) // 2
                for i in range(f):
                    for j in range(s_prime - f):
                        x, y = dp(n_half, i + 1, i + j + mid + 2)
                        earliest = min(earliest, x)
                        latest = max(latest, y)

            return (earliest + 1, latest + 1)

        # F(n,f,s) = F(n,s,f)
        if firstPlayer > secondPlayer:
            firstPlayer, secondPlayer = secondPlayer, firstPlayer

        earliest, latest = dp(n, firstPlayer, secondPlayer)
        dp.cache_clear()
        return [earliest, latest]


# https://leetcode.com/problems/the-earliest-and-latest-rounds-where-players-compete/solutions/1268452/python-2-solution-dfs-and-smart-dp-explained/?envType=daily-question&envId=2025-07-12

class Solution:
    def earliestAndLatest(self, n: int, a: int, b: int) -> List[int]:
        @lru_cache(None)
        def dp(l, r, m, q):
            if l > r:  dp(r, l, m, q)
            if l == r: ans.add(q)
            for i in range(1, l + 1):
                for j in range(l-i+1, r-i+1):
                    if not (m+1)//2 >= i + j >= l + r - m//2: continue
                    dp(i, j, (m + 1) // 2, q + 1)
        ans = set()
        dp(a, n - b + 1, n, 1)
        return [min(ans), max(ans)]

class Solution:
    def earliestAndLatest(self, n: int, a: int, b: int) -> list[int]:
        s=set();(f:=lambda l,r,m,q:l>r and f(r,l,m,q)or l==r and s.add(q)or[f(i,j,-~m//2,q+1)for i in range(1,l+1)for j in range(l-i+1,r-i+1)if l+r-m/2<=i+j<=-~m/2])(a,n-b+1,n,1);return min(s),max(s)

test('''
1900. The Earliest and Latest Rounds Where Players Compete
Hard
Topics
premium lock icon
Companies
Hint
There is a tournament where n players are participating. The players are standing in a single row and are numbered from 1 to n based on their initial standing position (player 1 is the first player in the row, player 2 is the second player in the row, etc.).

The tournament consists of multiple rounds (starting from round number 1). In each round, the ith player from the front of the row competes against the ith player from the end of the row, and the winner advances to the next round. When the number of players is odd for the current round, the player in the middle automatically advances to the next round.

For example, if the row consists of players 1, 2, 4, 6, 7
Player 1 competes against player 7.
Player 2 competes against player 6.
Player 4 automatically advances to the next round.
After each round is over, the winners are lined back up in the row based on the original ordering assigned to them initially (ascending order).

The players numbered firstPlayer and secondPlayer are the best in the tournament. They can win against any other player before they compete against each other. If any two other players compete against each other, either of them might win, and thus you may choose the outcome of this round.

Given the integers n, firstPlayer, and secondPlayer, return an integer array containing two values, the earliest possible round number and the latest possible round number in which these two players will compete against each other, respectively.

 

Example 1:

Input: n = 11, firstPlayer = 2, secondPlayer = 4
Output: [3,4]
Explanation:
One possible scenario which leads to the earliest round number:
First round: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
Second round: 2, 3, 4, 5, 6, 11
Third round: 2, 3, 4
One possible scenario which leads to the latest round number:
First round: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
Second round: 1, 2, 3, 4, 5, 6
Third round: 1, 2, 4
Fourth round: 2, 4
Example 2:

Input: n = 5, firstPlayer = 1, secondPlayer = 5
Output: [1,1]
Explanation: The players numbered 1 and 5 compete in the first round.
There is no way to make them compete in any other round.
 

Constraints:

2 <= n <= 28
1 <= firstPlayer < secondPlayer <= n
Seen this question in a real interview before?
1/5
Yes
No
Accepted
6,396/13.2K
Acceptance Rate
48.6%
Topics
Dynamic Programming
Memoization
icon
Companies
Hint 1
Brute force using bitmasks and simulate the rounds.
Hint 2
Calculate each state one time and save its solution.
''')
