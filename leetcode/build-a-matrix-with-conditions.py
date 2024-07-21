from lc import *

# https://leetcode.com/problems/build-a-matrix-with-conditions/discuss/2492822/Python3-topological-sort

class Solution:
    def buildMatrix(self, k: int, r: List[List[int]], c: List[List[int]]) -> List[List[int]]:
        def f(c): 
            g = [[] for _ in range(k)]
            d = [0]*k
            for u,v in c: 
                g[u-1].append(v-1)
                d[v-1] += 1
            q = deque(u for u,x in enumerate(d) if x==0)
            a = []
            while q:
                u = q.popleft()
                a.append(u+1)
                for v in g[u]:
                    d[v] -= 1
                    if d[v] == 0:
                        q.append(v)
            return a
        r,c = f(r), f(c)
        if len(r)<k or len(c)<k:
            return []
        a = [[0]*k for _ in range(k)]
        r,c =[{x:i for i,x in enumerate(t)}for t in(r,c)]
        for x in range(1,k+1):
            a[r[x]][c[x]] = x
        return a

class Solution:
    def buildMatrix(self, k: int, r: List[List[int]], c: List[List[int]]) -> List[List[int]]:
        p=[*map(lambda c:(g:=[[] for _ in range(k)],d:=[0]*k,a:=[],[g[u-1].append(v-1)or setitem(d,v-1,d[v-1]+1)for u,v in c],q:=deque(u for u,x in enumerate(d) if x==0),(t:=lambda:q and(a.append(1+(u:=q.popleft())),[setitem(d,v,d[v]-1)or d[v]==0 and q.append(v)for v in g[u]],t()))())and a,(r,c))];return[]if any(len(x)<k for x in p)else(a:=[[0]*k for _ in range(k)],p:=[{x:i for i,x in enumerate(t)}for t in p],[setitem(a[p[0][x]],p[1][x],x)for x in range(1,k+1)])and a

test('''
2392. Build a Matrix With Conditions
Hard

840

24

Add to List

Share
You are given a positive integer k. You are also given:

a 2D integer array rowConditions of size n where rowConditions[i] = [abovei, belowi], and
a 2D integer array colConditions of size m where colConditions[i] = [lefti, righti].
The two arrays contain integers from 1 to k.

You have to build a k x k matrix that contains each of the numbers from 1 to k exactly once. The remaining cells should have the value 0.

The matrix should also satisfy the following conditions:

The number abovei should appear in a row that is strictly above the row at which the number belowi appears for all i from 0 to n - 1.
The number lefti should appear in a column that is strictly left of the column at which the number righti appears for all i from 0 to m - 1.
Return any matrix that satisfies the conditions. If no answer exists, return an empty matrix.

 

Example 1:


Input: k = 3, rowConditions = [[1,2],[3,2]], colConditions = [[2,1],[3,2]]
Output: [[3,0,0],[0,0,1],[0,2,0]]
Explanation: The diagram above shows a valid example of a matrix that satisfies all the conditions.
The row conditions are the following:
- Number 1 is in row 1, and number 2 is in row 2, so 1 is above 2 in the matrix.
- Number 3 is in row 0, and number 2 is in row 2, so 3 is above 2 in the matrix.
The column conditions are the following:
- Number 2 is in column 1, and number 1 is in column 2, so 2 is left of 1 in the matrix.
- Number 3 is in column 0, and number 2 is in column 1, so 3 is left of 2 in the matrix.
Note that there may be multiple correct answers.
Example 2:

Input: k = 3, rowConditions = [[1,2],[2,3],[3,1],[2,3]], colConditions = [[2,1]]
Output: []
Explanation: From the first two conditions, 3 has to be below 1 but the third conditions needs 3 to be above 1 to be satisfied.
No matrix can satisfy all the conditions, so we return the empty matrix.
 

Constraints:

2 <= k <= 400
1 <= rowConditions.length, colConditions.length <= 104
rowConditions[i].length == colConditions[i].length == 2
1 <= abovei, belowi, lefti, righti <= k
abovei != belowi
lefti != righti
Accepted
22,953
Submissions
33,536
'''
,check=lambda res,exp,*args:sorted(res)==sorted(exp)
)
