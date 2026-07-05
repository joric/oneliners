from lc import *

# https://leetcode.com/problems/number-of-paths-with-max-score/solutions/463252/python-dp-solution-by-lee215-q55n/?envType=daily-question&envId=2026-07-05

class Solution:
    def pathsWithMaxScore(self, a: List[str]) -> List[int]:
        n, mod = len(a), 10**9 + 7
        dp = [[[-10**5, 0] for j in range(n + 1)] for i in range(n + 1)]
        dp[n - 1][n - 1] = [0, 1]
        for x in range(n)[::-1]:
            for y in range(n)[::-1]:
                if a[x][y] in 'XS': continue
                for i, j in [[0, 1], [1, 0], [1, 1]]:
                    if dp[x][y][0] < dp[x + i][y + j][0]:
                        dp[x][y] = [dp[x + i][y + j][0], 0]
                    if dp[x][y][0] == dp[x + i][y + j][0]:
                        dp[x][y][1] += dp[x + i][y + j][1]
                dp[x][y][0] += int(a[x][y]) if x or y else 0
        return [dp[0][0][0] if dp[0][0][1] else 0, dp[0][0][1] % mod]

# https://leetcode.com/problems/number-of-paths-with-max-score/solutions/7342895/python-from-recursion-to-dp-by-yeyechen-7t7f/?envType=daily-question&envId=2026-07-05

class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD = 10**9 + 7
        m, n = len(board), len(board[0])
        @cache
        def dfs(i: int, j: int) -> tuple:
            if i < 0 or j < 0 or board[i][j] == 'X':
                return (-inf, 0)
            if i == 0 and j == 0:
                return (0, 1)
            score = int(board[i][j]) if board[i][j].isdigit() else 0
            best = -inf
            ways = 0
            for di, dj in [(-1, 0), (0, -1), (-1, -1)]:
                new_i, new_j = i + di, j + dj
                s, w = dfs(new_i, new_j)
                if s > best:
                    best = s
                    ways = w
                elif s == best:
                    ways += w
            return (best + score, ways)
        s, w = dfs(m - 1, n - 1)
        return [max(s, 0), w % MOD]


class Solution:
    def pathsWithMaxScore(self, a: List[str]) -> List[int]:
        @cache
        def f(i,j):
            if i < 0 or j < 0 or a[i][j]=='X':
                return[-inf,0]
            if i == 0 and j == 0:
                return[0,1]
            r=[-inf,0]
            [(p:=f(x,y),r:=((r,[r[0],r[1]+p[1]])[p[0]==r[1]],p)[p[0]>r[0]])for x,y in((i-1,j),(i,j-1),(i-1,j-1))]
            return[r[0]+int(a[i][j].isdigit()and a[i][j]),r[1]]
        p=f(len(a)-1,len(a[0])-1)
        return[max(p[0],0),p[1]%(10**9+7)]

# https://leetcode.com/problems/number-of-paths-with-max-score/solutions/463674/three-solutions-in-python-3-dp-dfs-witho-vyp3/?envType=daily-question&envId=2026-07-05

class Solution:
    def pathsWithMaxScore(self, a: List[str]) -> List[int]:
        n=len(a)
        a[-1]=a[-1][:-1]+'0'
        @cache
        def f(i,j):
            if(i,j)==(0,0):return[0,1]
            if i<0 or j<0 or a[i][j]=='X':return[0,0]
            c=[*map(f,(i-1,i,i-1),(j,j-1,j-1))]
            b=max(x[0]for x in c)
            return[int(a[i][j])+b,sum(y for x,y in c if x==b)]
        m,p=f(n-1,n-1)
        return[p and m,p%(10**9+7)]

class Solution:
    def pathsWithMaxScore(self, a: List[str]) -> List[int]:
        n=len(a);a[-1]=a[-1][:-1]+'0';f=cache(lambda i,j:[0,1]if(i,j)==(0,0)else[0,0]if i<0 or j<0 or a[i][j]=='X'else(c:=[*map(f,(i-1,i,i-1),(j,j-1,j-1))],b:=max(p[0]for p in c),[int(a[i][j])+b,sum(y for x,y in c if x==b)])[2]);m,p=f(n-1,n-1);return[p and m,p%(10**9+7)]

class Solution:
    def pathsWithMaxScore(self, a: List[str]) -> List[int]:
        n=len(a)-1;f=cache(lambda i,j:[0,0]if min(i,j)<0 or a[i][j]>'S'else[0,1]if i+j<1 else(c:=[f(i-1,j),f(i,j-1),f(i-1,j-1)],[int(a[i][j]<'A'and a[i][j])+(b:=max(c)[0]),sum(y*(x==b)for x,y in c)])[1]);m,p=f(n,n);return[p and m,p%(10**9+7)]

test('''
1301. Number of Paths with Max Score
Hard
Topics
premium lock icon
Companies
Hint
You are given a square board of characters. You can move on the board starting at the bottom right square marked with the character 'S'.

You need to reach the top left square marked with the character 'E'. The rest of the squares are labeled either with a numeric character 1, 2, ..., 9 or with an obstacle 'X'. In one move you can go up, left or up-left (diagonally) only if there is no obstacle there.

Return a list of two integers: the first integer is the maximum sum of numeric characters you can collect, and the second is the number of such paths that you can take to get that maximum sum, taken modulo 10^9 + 7.

In case there is no path, return [0, 0].

 

Example 1:

Input: board = ["E23","2X2","12S"]
Output: [7,1]
Example 2:

Input: board = ["E12","1X1","21S"]
Output: [4,2]
Example 3:

Input: board = ["E11","XXX","11S"]
Output: [0,0]
 

Constraints:

2 <= board.length == board[i].length <= 100
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
19,820/46.3K
Acceptance Rate
42.8%
Topics
Principal
Array
Dynamic Programming
Matrix
Biweekly Contest 16
icon
Companies
Hint 1
Use dynamic programming to find the path with the max score.
Hint 2
Use another dynamic programming array to count the number of paths with max score.
''')
