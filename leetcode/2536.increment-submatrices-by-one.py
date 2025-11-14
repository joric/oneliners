from lc import *

# https://leetcode.com/problems/increment-submatrices-by-one/solutions/7343826/four-simple-lines-of-code-by-mikposp-iatl/?envType=daily-question&envId=2025-11-14

class Solution:
    def rangeAddQueries(self, n: int, q: List[List[int]]) -> List[List[int]]:
        z = Counter(p for i1,j1,i2,j2 in q for p in ((i1,j1),(i2+1,j2+1)))
        z.subtract(Counter(p for i1,j1,i2,j2 in q for p in ((i2+1,j1),(i1,j2+1))))
        g = ([*accumulate(z[i,j] for i in range(n))] for j in range(n))
        return [*map(list,map(accumulate,zip(*g)))]

class Solution:
    def rangeAddQueries(self, n: int, q: List[List[int]]) -> List[List[int]]:
        x=Counter(p for a,b,c,d in q for p in ((a,b),(c+1,d+1)))
        y=Counter(p for a,b,c,d in q for p in ((c+1,b),(a,d+1)))
        x.subtract(y)
        return[*map(list,map(accumulate,zip(*([*accumulate(x[i,j]for i in range(n))]for j in range(n)))))]

class Solution:
    def rangeAddQueries(self, n: int, q: List[List[int]]) -> List[List[int]]:
        x=Counter();[x.update({p:v})for a,b,c,d in q for p,v in[((a,b),1),((c+1,d+1),1),((c+1,b),-1),((a,d+1),-1)]];return[*map(list,map(accumulate,zip(*([*accumulate(x[i,j]for i in range(n))]for j in range(n)))))]

# https://leetcode.com/problems/increment-submatrices-by-one/solutions/3053597/python-numpy-2-lines-by-leox2022-t2sk/?envType=daily-question&envId=2025-11-14

class Solution:
    def rangeAddQueries(self, n: int, q: List[List[int]]) -> List[List[int]]:
        t=__import__('numpy').zeros((n,n),int);[t[a:c+1,b:d+1].__iadd__(1)for a,b,c,d in q];return t.tolist()

test('''
2536. Increment Submatrices by One
Medium
Topics
premium lock icon
Companies
Hint
You are given a positive integer n, indicating that we initially have an n x n 0-indexed integer matrix mat filled with zeroes.

You are also given a 2D integer array query. For each query[i] = [row1i, col1i, row2i, col2i], you should do the following operation:

Add 1 to every element in the submatrix with the top left corner (row1i, col1i) and the bottom right corner (row2i, col2i). That is, add 1 to mat[x][y] for all row1i <= x <= row2i and col1i <= y <= col2i.
Return the matrix mat after performing every query.

 

Example 1:


Input: n = 3, queries = [[1,1,2,2],[0,0,1,1]]
Output: [[1,1,0],[1,2,1],[0,1,1]]
Explanation: The diagram above shows the initial matrix, the matrix after the first query, and the matrix after the second query.
- In the first query, we add 1 to every element in the submatrix with the top left corner (1, 1) and bottom right corner (2, 2).
- In the second query, we add 1 to every element in the submatrix with the top left corner (0, 0) and bottom right corner (1, 1).
Example 2:


Input: n = 2, queries = [[0,0,1,1]]
Output: [[1,1],[1,1]]
Explanation: The diagram above shows the initial matrix and the matrix after the first query.
- In the first query we add 1 to every element in the matrix.
 

Constraints:

1 <= n <= 500
1 <= queries.length <= 104
0 <= row1i <= row2i < n
0 <= col1i <= col2i < n
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
36,342/61.2K
Acceptance Rate
59.4%
Topics
Array
Matrix
Prefix Sum
Weekly Contest 328
icon
Companies
Hint 1
Imagine each row as a separate array. Instead of updating the whole submatrix together, we can use prefix sum to update each row separately.
Hint 2
For each query, iterate over the rows i in the range [row1, row2] and add 1 to prefix sum S[i][col1], and subtract 1 from S[i][col2 + 1].
Hint 3
After doing this operation for all the queries, update each row separately with S[i][j] = S[i][j] + S[i][j - 1].
Similar Questions
Range Sum Query 2D - Mutable
Medium
Count Positions on Street With Required Brightness
Medium
''')
