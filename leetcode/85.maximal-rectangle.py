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

# https://leetcode.com/problems/maximal-rectangle/solutions/2892403/short-simple-by-macraiu-qhys/?envType=daily-question&envId=2026-01-11

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        maxarea = 0
        Y = len(matrix)
        X = len(matrix[0])
        for i in range(Y):
            for j in range(X):
                if(maxarea > (Y - i) * (X - j)):
                    break
                row =  0
                col =  X - j 
                for k in range(i, Y):
                    for l in range(j, j + col):
                        if matrix[k][l] == "0":
                            col  = min(col, l - j)
                            break
                    row += 1
                    maxarea = max(maxarea, col * row)
        return maxarea

class Solution:
    def maximalRectangle(self,m:List[List[str]])->int:
        a=0
        h=len(m)
        w=len(m[0])
        for i in range(h):
            for j in range(w):
                if a>(h-i)*(w-j):
                    break
                r=0
                c=w-j
                for k in range(i,h):
                    for l in range(j,j+c):
                        if m[k][l]<'1':
                            c=min(c,l-j)
                            break
                    r+=1
                    a=max(a,c*r)
        return a

class Solution:
    def maximalRectangle(self,m:List[List[str]])->int:
        a,h,w=0,len(m),len(m[0]);[(r:=0,c:=w-j,[(c:=next((min(c,l-j)for l in range(j,j+c)if'1'>m[k][l]),c),a:=max(a,c*(r:=r+1)))for k in range(i,h)])for i in range(h)for j in range(w)if(h-i)*(w-j)>=a];return a

class Solution:
    def maximalRectangle(self,m:List[List[str]])->int:
        a,h,w=0,len(m),len(m[0]);[(c:=w-j,[(c:=(m[k][j:j+c]+['0']).index('0'),a:=max(a,c*(k-i+1)))for k in range(i,h)])for i in range(h)for j in range(w)if(h-i)*(w-j)>=a];return a

# bitwise solution

class Solution:
    def maximalRectangle(self, m: list[list[str]]) -> int:
        a = 0
        for i in range(len(m)):
            x = ~0
            for j,r in enumerate(m[i:]):
                x &= int(''.join(r), 2)
                w = len(max(bin(x)[2:].split('0')))
                a = max(a, w * (j + 1))
        return a

class Solution:
    def maximalRectangle(self,m:List[List[str]])->int:
        return max(len(max(bin(x:=x&int(''.join(r),2))[2:].split('0')))*(j+1)for i in range(len(m))if(x:=~0)for j,r in enumerate(m[i:]))

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