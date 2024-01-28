from lc import *

# https://leetcode.com/problems/number-of-submatrices-that-sum-to-target

class Solution:
    def numSubmatrixSumTarget(self, m: List[List[int]], t: int) -> int:
        m, w, r = [[*accumulate(a)]for a in m],len(m[0]),0
        for j in range(w):
            for k in range(j,w):
                c = Counter([0])
                s = 0
                for x in m:
                    s += x[k] - (j and x[j-1])
                    r += c[s-t]
                    c[s] += 1
        return r

class Solution:
    def numSubmatrixSumTarget(self, m: List[List[int]], t: int) -> int:
        m,w,r=[[*accumulate(a)]for a in m],len(m[0]),0;[(c:=Counter([0]),s:=0,[c.update([(r:=r+c[(s:=s+x[k]-(j and x[j-1]))-t],s)[1]])for x in m])for j in range(w)for k in range(j,w)];return r

class Solution:
    def numSubmatrixSumTarget(self, m: List[List[int]], t: int) -> int:
        a=0
        for i in range(len(m)):
            u = [0]*len(m[0])
            for r in m[i:]:
                u = [*starmap(add,zip(u,r))]
                c = Counter([0])
                s = 0
                for x in u:
                    s += x
                    a += c[s-t]
                    c[s] += 1
        return a

class Solution:
    def numSubmatrixSumTarget(self, m: List[List[int]], t: int) -> int:
        a=0;[(u:=[0]*len(m[0]),[(u:=[*starmap(add,zip(u,r))],c:=Counter([0]),s:=0,[(a:=a+c[(s:=s+x)-t],c.update([s]))for x in u])for r in m[i:]])for i in range(len(m))];return a

test('''
1074. Number of Submatrices That Sum to Target
Hard

3069

65

Add to List

Share
Given a matrix and a target, return the number of non-empty submatrices that sum to target.

A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.

Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate that is different: for example, if x1 != x1'.

 

Example 1:


Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
Output: 4
Explanation: The four 1x1 submatrices that only contain 0.
Example 2:

Input: matrix = [[1,-1],[-1,1]], target = 0
Output: 5
Explanation: The two 1x2 submatrices, plus the two 2x1 submatrices, plus the 2x2 submatrix.
Example 3:

Input: matrix = [[904]], target = 0
Output: 0
 

Constraints:

1 <= matrix.length <= 100
1 <= matrix[0].length <= 100
-1000 <= matrix[i] <= 1000
-10^8 <= target <= 10^8
Accepted
91,491
Submissions
131,343
''')
