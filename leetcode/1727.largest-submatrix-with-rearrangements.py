from lc import *

# https://leetcode.com/problems/largest-submatrix-with-rearrangements/discuss/3969542/Fully-vectorize-Python-(Numpy)-code-that-beats-100

import numpy as np

class Solution:
    def largestSubmatrix(self, m: List[List[int]]) -> int:
        m = np.array(m)
        t = np.cumsum(m,axis = 0)
        m = t - np.maximum.accumulate(t * (m == 0), axis = 0)
        m = np.fliplr(np.sort(m, axis = 1))
        r = np.arange(1, m.shape[1] + 1)
        return np.max(m * np.repeat(r[np.newaxis, :], m.shape[0], 0))

# https://leetcode.com/problems/largest-submatrix-with-rearrangements/discuss/1021893/Python3-Concise-Solution-8-Lines

class Solution:
    def largestSubmatrix(self, m: List[List[int]]) -> int:
        t = 0
        for i,r in enumerate(m):
            for j,c in enumerate(r):
                if i and c:
                    m[i][j]+=m[i-1][j]
            for k,v in enumerate(sorted(r)[::-1],1):
                t = max(t,k*v)
        return t

class Solution:
    def largestSubmatrix(self, m: List[List[int]]) -> int:
        e,t=enumerate,0;[([setitem(m[i],j,m[i][j]+m[i-1][j]*(i and c))for j,c in e(r)],[t:=max(t,k*v)for k,v in e(sorted(r)[::-1],1)])for i,r in e(m)];return t

test('''
1727. Largest Submatrix With Rearrangements
Medium

984

28

Add to List

Share
You are given a binary matrix matrix of size m x n, and you are allowed to rearrange the columns of the matrix in any order.

Return the area of the largest submatrix within matrix where every element of the submatrix is 1 after reordering the columns optimally.

 

Example 1:


Input: matrix = [[0,0,1],[1,1,1],[1,0,1]]
Output: 4
Explanation: You can rearrange the columns as shown above.
The largest submatrix of 1s, in bold, has an area of 4.
Example 2:


Input: matrix = [[1,0,1,0,1]]
Output: 3
Explanation: You can rearrange the columns as shown above.
The largest submatrix of 1s, in bold, has an area of 3.
Example 3:

Input: matrix = [[1,1,0],[1,0,1]]
Output: 2
Explanation: Notice that you must rearrange entire columns, and there is no way to make a submatrix of 1s larger than an area of 2.
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m * n <= 105
matrix[i][j] is either 0 or 1.
Accepted
16,479
Submissions
26,553
''')
