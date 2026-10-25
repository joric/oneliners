from lc import *

# https://leetcode.com/problems/count-islands-with-total-value-divisible-by-k/solutions/8580142/six-simple-lines-of-code-by-mikposp-rkck/?envType=daily-question&envId=2026-10-26

class Solution:
    def countIslands(self, g: List[List[int]], k: int) -> int:
        m,n = len(g),len(g[0])
        def f(i,j):
            if not m>i>=0<=j<n or g[i][j]==0: return 0
            q,g[i][j] = g[i][j],0
            return q+f(i,j+1)+f(i+1,j)+f(i,j-1)+f(i-1,j)
        return sum(g[i][j]>0==f(i,j)%k for i in range(m) for j in range(n))

# POTD 2026-10-25

class Solution:
    def countIslands(self, g: List[List[int]], k: int) -> int:
        import scipy.ndimage as s;l,c=s.label(g);return int(sum(x%k<1for x in s.sum(g,l,range(1,c+1))))

class Solution:
    def countIslands(self, g: List[List[int]], k: int) -> int:
        import scipy.ndimage as s;l,c=s.label(g);return int(sum(s.sum(g,l,range(1,c+1))%k<1))

test('''
3619. Count Islands With Total Value Divisible by K
Medium
Topics
premium lock icon
Companies
Hint
You are given an m x n matrix grid and a positive integer k. An island is a group of positive integers (representing land) that are 4-directionally connected (horizontally or vertically).

The total value of an island is the sum of the values of all cells in the island.

Return the number of islands with a total value divisible by k.

 

Example 1:


Input: grid = [[0,2,1,0,0],[0,5,0,0,5],[0,0,1,0,0],[0,1,4,7,0],[0,2,0,0,8]], k = 5

Output: 2

Explanation:

The grid contains four islands. The islands highlighted in blue have a total value that is divisible by 5, while the islands highlighted in red do not.

Example 2:


Input: grid = [[3,0,3,0], [0,3,0,3], [3,0,3,0]], k = 3

Output: 6

Explanation:

The grid contains six islands, each with a total value that is divisible by 3.

 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 1000
1 <= m * n <= 105
0 <= grid[i][j] <= 106
1 <= k <= 106
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
34,890/62.8K
Acceptance Rate
55.6%
Topics
Senior
Array
Depth-First Search
Breadth-First Search
Union-Find
Matrix
Biweekly Contest 161
icon
Companies
Hint 1
Use a BFS/DFS to find connected components.
Similar Questions
Number of Islands
''')
