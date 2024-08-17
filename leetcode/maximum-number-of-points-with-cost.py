from lc import *

# https://leetcode.com/problems/maximum-number-of-points-with-cost/discuss/1959299/8-lines-of-python-code-faster-than-99.73-explained

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        for i, row in enumerate(points[:-1]):
            for j in range(1, len(row)):
                row[j] = max(row[j], row[j-1]-1)
            for j in range(len(row)-2, -1, -1):
                row[j] = max(row[j], row[j+1]-1)
            for j in range(len(row)):
                points[i+1][j] += points[i][j]
        return max(points[-1])

class Solution:
    def maxPoints(self, p: List[List[int]]) -> int:
        s,e=setitem,range;[([s(r,j,max(r[j],r[j-1]-1))for j in e(1,len(r))],[s(r,j,max(r[j], r[j+1]-1))for j in e(len(r)-2,-1,-1)],[s(p[i+1],j,p[i+1][j]+p[i][j])for j in e(len(r))])for i,r in enumerate(p[:-1])];return max(p[-1])

# https://leetcode.com/problems/maximum-number-of-points-with-cost/discuss/1345059/Python-DP-like-Solution

class Solution:
    def maxPoints(self, p: List[List[int]]) -> int:
        m,n,s,e=len(p),len(p[0]),setitem,range
        for i in e(m-1):
            for j in e(n - 2, -1, -1):
                s(p[i],j,max(p[i][j],p[i][j+1]-1))
            for j in e(n):
                s(p[i],j,max(p[i][j],j and p[i][j-1]-1))
                s(p[i+1],j,p[i+1][j]+p[i][j])
        return max(p[-1])

class Solution:
    def maxPoints(self, p: List[List[int]]) -> int:
        m,n,s,e=len(p),len(p[0]),setitem,range;[[s(p[i],j,max(p[i][j],p[i][j+1]-1))for j in e(n-2,-1,-1)]and[s(p[i],j,max(p[i][j],j and p[i][j-1]-1))or s(p[i+1],j,p[i+1][j]+p[i][j])for j in e(n)]for i in e(m-1)];return max(p[-1])

# https://leetcode.com/problems/maximum-number-of-points-with-cost/discuss/1344898/Python-very-short-dp-solution-explained

class Solution:
    def maxPoints(self, P):
        m, n = len(P), len(P[0])
        dp = P[0]
        for i in range(1, m):
            c1 = list(accumulate([a+b for a,b in zip(dp, range(n))], max))
            c2 = list(accumulate([a-b for a,b in zip(dp[::-1], range(n-1,-1,-1))], max))
            dp2 = [max(c1[i] - i, c2[n-1-i] + i) for i in range(n)]
            dp = [x+y for x,y in zip(dp2, P[i])]
        return max(dp)

# https://leetcode.com/problems/maximum-number-of-points-with-cost/discuss/1947800/Python-Top-Down-%2B-Memorization-O(mn)-Passes

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        M = len(points)
        N = len(points[0])
        @cache
        def dp(r, c):
            if r == M - 1:
                return points[r][c]
            return points[r][c] + max(best_relative_right(r+1, c), best_relative_left(r+1, c))
        @cache
        def best_relative_left(r, c):
            if c == 0:
                return dp(r, c)
            return max(dp(r, c), best_relative_left(r, c-1) - 1)
        
        @cache
        def best_relative_right(r, c):
            if c == N-1:
                return dp(r, c)
            return max(dp(r, c), best_relative_right(r, c+1) - 1)

        return max(dp(0, c) for c in range(N))

class Solution:
    def maxPoints(self, p: List[List[int]]) -> int:
        m,n=len(p),len(p[0])
        f=cache(lambda r,c:p[r][c]if r == m-1 else p[r][c]+max(a(r+1,c),b(r+1,c)))
        a=cache(lambda r,c:f(r,c)if c==0 else max(f(r,c),a(r,c-1)-1))
        b=cache(lambda r,c:f(r,c)if c==n-1 else max(f(r,c),b(r,c+1)-1))
        return max(f(0,c)for c in range(n))

class Solution:
    def maxPoints(self, p: List[List[int]]) -> int:
        m,n=len(p),len(p[0]);f=cache(lambda r,c:p[r][c]if r==m-1 else p[r][c]+max(a(r+1,c,0,-1),a(r+1,c,n-1,1)));a=cache(lambda r,c,l,s:f(r,c)if c==l else max(f(r,c),a(r,c+s,l,s)-1));return max(f(0,c)for c in range(n))

test('''
1937. Maximum Number of Points with Cost
Medium

2338

140

Add to List

Share
You are given an m x n integer matrix points (0-indexed). Starting with 0 points, you want to maximize the number of points you can get from the matrix.

To gain points, you must pick one cell in each row. Picking the cell at coordinates (r, c) will add points[r][c] to your score.

However, you will lose points if you pick a cell too far from the cell that you picked in the previous row. For every two adjacent rows r and r + 1 (where 0 <= r < m - 1), picking cells at coordinates (r, c1) and (r + 1, c2) will subtract abs(c1 - c2) from your score.

Return the maximum number of points you can achieve.

abs(x) is defined as:

x for x >= 0.
-x for x < 0.
 

Example 1:


Input: points = [[1,2,3],[1,5,1],[3,1,1]]
Output: 9
Explanation:
The blue cells denote the optimal cells to pick, which have coordinates (0, 2), (1, 1), and (2, 0).
You add 3 + 5 + 3 = 11 to your score.
However, you must subtract abs(2 - 1) + abs(1 - 0) = 2 from your score.
Your final score is 11 - 2 = 9.
Example 2:


Input: points = [[1,5],[2,3],[4,2]]
Output: 11
Explanation:
The blue cells denote the optimal cells to pick, which have coordinates (0, 1), (1, 1), and (2, 0).
You add 5 + 3 + 4 = 12 to your score.
However, you must subtract abs(1 - 1) + abs(1 - 0) = 1 from your score.
Your final score is 12 - 1 = 11.
 

Constraints:

m == points.length
n == points[r].length
1 <= m, n <= 105
1 <= m * n <= 105
0 <= points[r][c] <= 105
Accepted
60,436
Submissions
169,322
''')
