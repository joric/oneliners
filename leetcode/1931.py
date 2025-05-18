from lc import *

# https://leetcode.com/problems/painting-a-grid-with-three-different-colors/solutions/1330889/python-o-2-m-n-m-dp-solution-explained/?envType=daily-question&envId=2025-05-18

class Solution:
    def colorTheGrid(self, m, n):
        C = [c for c in product([0,1,2], repeat = m) if all(x!=y for x,y in zip(c, c[1:]))]

        MOD, dp, d = 10**9 + 7, Counter(C), defaultdict(list)

        for c1, c2 in product(C, C):
            if all(x != y for x, y in zip(c1, c2)):
                d[c1].append(c2)

        for _ in range(n-1):
            dp2 = Counter()
            for c1 in C:
                for c2 in d[c1]:
                    dp2[c2] = (dp2[c2] + dp[c1]) % MOD
            dp = dp2

        return sum(dp.values()) % MOD


# https://leetcode.com/problems/painting-a-grid-with-three-different-colors/description/?envType=daily-question&envId=2025-05-18

class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        # Initialize the cache
        cache = {}

        def dp(seq, lastRow):
            if seq == m * n:
                return 1
            if (seq, lastRow) in cache:
                return cache[(seq, lastRow)]
            i = seq // m
            j = seq % m
            lastRowList = list(lastRow)
            ans = 0
            neighborColors = set()
            if i > 0:
                neighborColors.add(lastRowList[j])
            if j > 0:
                neighborColors.add(lastRowList[j - 1])
            for c in (0, 1, 2):
                if c not in neighborColors:
                    newLastRow = lastRowList[:]
                    newLastRow[j] = c
                    ans += dp(seq + 1, tuple(newLastRow))
            ans = ans % mod
            cache[(seq, lastRow)] = ans  # Cache the result
            return ans
        mod = 10**9 + 7
        return dp(0, tuple([0] * m))

class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        @cache
        def f(k,p):
            if k<m*n:
                i,j = divmod(k,m)
                s={*([p[j]]if i else[]),*([p[j-1]]if j else[])}
                return sum(f(k+1,tuple((x,c)[i==j]for i,x in enumerate(p)))for c in(0,1,2)if c not in s)%(10**9+7)
            return 1
        return f(0,tuple([0]*m))

# TODO

class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        @cache
        def f(k,p):
            if k==m*n: return 1
            s={*([p[j-1]]if(j:=k%m)else[]),*([p[j]]if(i:=k//m)else[])}
            return sum(f(k+1,tuple((x,c)[i==j]for i,x in enumerate(p)))for c in(0,1,2)if c not in s)%(10**9+7)
        return f(0,tuple([0]*m))

test('''
1931. Painting a Grid With Three Different Colors
Solved
Hard
Topics
Companies
Hint
You are given two integers m and n. Consider an m x n grid where each cell is initially white. You can paint each cell red, green, or blue. All cells must be painted.

Return the number of ways to color the grid with no two adjacent cells having the same color. Since the answer can be very large, return it modulo 109 + 7.

 

Example 1:


Input: m = 1, n = 1
Output: 3
Explanation: The three possible colorings are shown in the image above.
Example 2:


Input: m = 1, n = 2
Output: 6
Explanation: The six possible colorings are shown in the image above.
Example 3:

Input: m = 5, n = 5
Output: 580986
 

Constraints:

1 <= m <= 5
1 <= n <= 1000
Seen this question in a real interview before?
1/5
Yes
No
Accepted
11.2K
Submissions
19.5K
Acceptance Rate
57.2%
Topics
Dynamic Programming
Companies
Hint 1
Represent each colored column by a bitmask based on each cell color.
Hint 2
Use bitmasks DP with state (currentCell, prevColumn).
Similar Questions
Number of Ways to Paint N × 3 Grid
Hard
''')
