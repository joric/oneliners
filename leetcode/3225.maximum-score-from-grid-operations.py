from lc import *

# https://leetcode.com/problems/maximum-score-from-grid-operations/solutions/5508404/python-3-14-lines-dp-prefix-sum-ts-59-70-h0r5/?envType=daily-question&envId=2026-04-29

class Solution:
    def maximumScore(self, g: List[List[int]]) -> int:
        n = len(g)
        a, b, p = range(n), range(n+1), []
        c = [[0,0]for _ in b]
        p = [[*accumulate(x,initial=0)]for x in zip(*g)]
        for i in reversed(a):
            t = c
            c = [[0, 0] for _ in b]
            for j, k, o in product(b, b, (0,1)):
                if k > j and i != 0 and o == 1:
                    c[j][1] = max(c[j][1], p[i-1][k] - p[i-1][j] + t[k][1])
                elif j > k:
                    c[j][o] = max(c[j][o], p[i][j] - p[i][k] + t[k][0])
                else:
                    c[j][o] = max(c[j][0], t[k][1])
        return max(*c[0])

class Solution:
    def maximumScore(self, g: List[List[int]]) -> int:
        n,s=len(g),setitem;a,b,p=range(n),range(n+1),[];c=[[0,0]for _ in b];p=[[*accumulate((0,*x))]for x in zip(*g)];[(t:=c,c:=[[0,0]for _ in b],[s(c[j],1,max(c[j][1],p[i-1][k]-p[i-1][j]+t[k][1]))if k>j and i and o==1 else s(c[j],o,max(c[j][o],p[i][j]-p[i][k]+t[k][0]))if j>k else s(c[j],o,max(c[j][0],t[k][1]))for j,k,o in product(b,b,(0,1))])for i in reversed(a)];return max(*c[0])

class Solution:
    def maximumScore(self, g: List[List[int]]) -> int:
        n,r,m=len(g),range,max;b=r(n+1);c=[[0,0]for _ in b];x=[[0,*accumulate(y)]for y in zip(*g)];[(t:=c,c:=[[0,0]for _ in b],[[setitem(c[j],o,m(c[j][o],x[i-1][k]-x[i-1][j]+t[k][1])if k>j and i and o else m(c[j][o],x[i][j]-x[i][k]+t[k][0])if j>k else m(c[j][0],t[k][1]))for j,k,o in product(b,b,r(2))]])for i in r(n)[::-1]];return m(*c[0])

test('''
3225. Maximum Score From Grid Operations
Hard
Topics
premium lock icon
Companies
Hint
You are given a 2D matrix grid of size n x n. Initially, all cells of the grid are colored white. In one operation, you can select any cell of indices (i, j), and color black all the cells of the jth column starting from the top row down to the ith row.

The grid score is the sum of all grid[i][j] such that cell (i, j) is white and it has a horizontally adjacent black cell.

Return the maximum score that can be achieved after some number of operations.

 

Example 1:

Input: grid = [[0,0,0,0,0],[0,0,3,0,0],[0,1,0,0,0],[5,0,0,3,0],[0,0,0,0,2]]

Output: 11

Explanation:


In the first operation, we color all cells in column 1 down to row 3, and in the second operation, we color all cells in column 4 down to the last row. The score of the resulting grid is grid[3][0] + grid[1][2] + grid[3][3] which is equal to 11.

Example 2:

Input: grid = [[10,9,0,0,15],[7,1,0,8,0],[5,20,0,11,0],[0,0,0,1,2],[8,12,1,10,3]]

Output: 94

Explanation:


We perform operations on 1, 2, and 3 down to rows 1, 4, and 0, respectively. The score of the resulting grid is grid[0][0] + grid[1][0] + grid[2][1] + grid[4][1] + grid[1][3] + grid[2][3] + grid[3][3] + grid[4][3] + grid[0][4] which is equal to 94.

Other examples:

Input: grid = [[7,3,0],[7,0,0],[3,6,0]]
Output: 20

Constraints:

1 <= n == grid.length <= 100
n == grid[i].length
0 <= grid[i][j] <= 109
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
3,510/12.6K
Acceptance Rate
27.8%
Topics
Principal
Array
Dynamic Programming
Matrix
Prefix Sum
Biweekly Contest 135
icon
Companies
Hint 1
Use dynamic programming.
Hint 2
Solve the problem in O(N^4) using a 3-states dp.
Hint 3
Let dp[i][lastHeight][beforeLastHeight] denote the maximum score if the grid was limited to column i, and the height of column i - 1 is lastHeight and the height of column i - 2 is beforeLastHeight.
Hint 4
The third state, beforeLastHeight, is used to determine which values of column i - 1 will be added to the score. We can replace this state with another state that only takes two values 0 or 1.
Hint 5
Let dp[i][lastHeight][isBigger] denote the maximum score if the grid was limited to column i, and where the height of column i - 1 is lastHeight. Additionally, if isBigger == 1, the number of black cells in column i is assumed to be larger than the number of black cells in column i - 2, and vice versa. Note that if our assumption is wrong, it would lead to a suboptimal score and, therefore, it would not be considered as the final answer.
Similar Questions
Maximum Difference Score in a Grid
Medium
''')
