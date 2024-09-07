from lc import *

# https://leetcode.com/problems/n-queens-ii/discuss/1222447/Python-3-one-line

class Solution:
    def totalNQueens(self, n: int) -> int:
        def dfs(cols):
            y = len(cols)
            if y == n:
                return 1
            total = 0
            for x in set(range(n)) - set(cols):
                if all(abs(y-r) != abs(x-c) for r,c in enumerate(cols)):
                    total += dfs(cols + [x])
            return total
        return dfs([])

class Solution:
    def totalNQueens(self, n: int) -> int:
        return(f:=lambda p:sum(f(p+[x])for x in set(range(n))-set(p)if all(abs(y-r)!=abs(x-c)for r,c in enumerate(p)))if n>(y:=len(p))else 1)([])

test('''
52. N-Queens II
Hard

3897

266

Add to List

Share
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

 

Example 1:


Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
Example 2:

Input: n = 1
Output: 1
 

Constraints:

1 <= n <= 9
Accepted
417,584
Submissions
557,774
''')
