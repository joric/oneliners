from lc import *

# https://leetcode.com/problems/maximal-rectangle/discuss/5014380/Python-3-oror-10-lines-histogram-oror-TS%3A-98-76
# also see https://leetcode.com/problems/largest-rectangle-in-histogram

class Solution:
    def maximalRectangle(self, a: list[list[str]]) -> int:
        r,m,n = 0,len(a),len(a[0])
        d = [0]*(n+1)
        for i in range(m):
            q = deque([-1])
            for j in range(n+1):
                d[j] = d[j]+1 if j<n and a[i][j]=='1' else 0
                while d[q[0]]>d[j]:
                    r = max(r,d[q.popleft()]*(j-q[0]-1))
                q.appendleft(j)
        return r

class Solution:
    def maximalRectangle(self, a: list[list[str]]) -> int:
        m,n,r=len(a),len(a[0]),0;d=[0]*(n+1);[(q:=deque([-1]),[(setitem(d,j,1+d[j]if j<n and a[i][j]=='1'else 0),all(d[q[0]]>d[j]and(r:=max(r,d[q.popleft()]*(j-q[0]-1)))for _ in d),q.appendleft(j))for j in range(n+1)])for i in range(m)];return r

test('''
85. Maximal Rectangle
Hard

9845

170

Add to List

Share
Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

 

Example 1:


Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.
Example 2:

Input: matrix = [["0"]]
Output: 0
Example 3:

Input: matrix = [["1"]]
Output: 1
 

Constraints:

rows == matrix.length
cols == matrix[i].length
1 <= row, cols <= 200
matrix[i][j] is '0' or '1'.
Accepted
405,045
Submissions
855,421
''')