from Leetcode import *

class Solution0:
    def solveNQueens(self, n):
        def dfs(board, i, c1, c2, c3):
            if i == n: ans.append(["."*j + "Q" + "."*(n-j-1) for j in board])
            for j in range(n):
                if c1 & 1<<j or c2 & 1<<i-j+n or c3 & 1<<i+j: continue
                dfs(board + [j], i + 1, c1 ^ 1<<j, c2 ^ 1<<i-j+n, c3 ^ 1<<i+j)
        ans = []
        dfs([], 0, 0, 0, 0)
        return ans

class Solution1:
    def solveNQueens(self, n: int) -> List[List[str]]:
        return[['.'*v+'Q'+'.'*(n-v-1)for v in c]for c in permutations(range(n))if(len(set(i+v for i,v in enumerate(c)))==n)and(len(set(i-v for i,v in enumerate(c)))==n)]

class Solution2:
    def solveNQueens(self, n: int) -> List[List[str]]:
        return[['.'*v+'Q'+'.'*(n-v-1)for v in c]for c in permutations(range(n)) if (a,b:=zip(*[(i+v,i-v) for i,v in enumerate(c)])) and len(set(a))==len(set(b))==n]

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        return[['.'*v+'Q'+'.'*(n-v-1)for v in c]for c in permutations(range(n))if(len(set(x for i,v in enumerate(c)for x in(i+v+n,i-v)))==2*n)]


test(Solution,'''
51. N-Queens

Hard

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

Example 1:

Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

Example 2:

Input: n = 1
Output: [["Q"]]

Constraints:

1 <= n <= 9
''')