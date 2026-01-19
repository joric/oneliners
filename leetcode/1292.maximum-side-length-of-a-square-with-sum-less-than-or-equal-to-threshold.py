from lc import *

# https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/solutions/7496803/five-simple-lines-of-code-by-mikposp-gihw/?envType=daily-question&envId=2026-01-19

class Solution:
    def maxSideLength(self, g: List[List[int]], t: int) -> int:
        m,n,p = len(g),len(g[0]),[*zip(*map(accumulate,zip(*map(accumulate,g))))]
        f=lambda q:all(p[i][j]-(i>=q and p[i-q][j])-(j>=q and p[i][j-q])+(i>=q<=j and p[i-q][j-q])>t for i,j in product(range(q-1,m),range(q-1,n)))
        return bisect_left(range(1,min(m,n)+1),1,key=f)

class Solution:
    def maxSideLength(self, g: List[List[int]], t: int) -> int:
        m,n,p=len(g),len(g[0]),[*zip(*map(accumulate,zip(*map(accumulate,g))))];f=lambda q:all(p[i][j]-(i>=q and p[i-q][j])-(j>=q and p[i][j-q])+(i>=q<=j and p[i-q][j-q])>t for i,j in product(range(q-1,m),range(q-1,n)));return bisect_left(range(1,min(m,n)+1),1,key=f)

# https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/solutions/452701/8-lines-omn-by-stefanpochmann-twun/?envType=daily-question&envId=2026-01-19

class Solution:
    def maxSideLength(self, g: List[List[int]], t: int) -> int:
        f=lambda i,j:i>-1<j and g[i][j]or 0
        s=0
        for i in range(len(g)):
            for j in range(len(g[0])):
                g[i][j] += f(i-1,j)+f(i,j-1)-f(i-1,j-1)
                s += i>=s<=j and t>=f(i,j)-f(i-s-1,j)-f(i,j-s-1)+f(i-s-1,j-s-1)
        return s

class Solution:
    def maxSideLength(self, g: List[List[int]], t: int) -> int:
        s,f=0,lambda i,j:i>-1<j and g[i][j]or 0;[(setitem(g[i],j,g[i][j]+f(i-1,j)+f(i,j-1)-f(i-1,j-1)),s:=s+(i>=s<=j and t>=f(i,j)-f(i-s-1,j)-f(i,j-s-1)+f(i-s-1,j-s-1)))for i in range(len(g))for j in range(len(g[0]))];return s

class Solution:
    def maxSideLength(self, g: List[List[int]], t: int) -> int:
        f,s,e=lambda i,j:i>-1<j and g[i][j]or 0,0,enumerate;[(setitem(g[i],j,g[i][j]+f(i-1,j)+f(i,j-1)-f(i-1,j-1)),s:=s+(i>=s<=j and t>=f(i,j)-f(i-s-1,j)-f(i,j-s-1)+f(i-s-1,j-s-1)))for i,r in e(g)for j,x in e(r)];return s

class Solution:
    def maxSideLength(self, g: List[List[int]], t: int) -> int:
        f,s,e=lambda i,j:i|j>-1 and g[i][j],0,enumerate;[(setitem(r,j,x+f(i-1,j)+f(i,j-1)-f(i-1,j-1)),s:=s+(i>=s<=j and t>=f(i,j)-f(i+~s,j)-f(i,j+~s)+f(i+~s,j+~s)))for i,r in e(g)for j,x in e(r)];return s

# https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/solutions/452383/c-no-dp-recursion-beats-100-on-space-wit-h3av/

class Solution:
    def maxSideLength(self, g: List[List[int]], t: int) -> int:
        h, w = len(g), len(g[0])
        def f(k, y, x, z):
            r,c = y+z,x+z
            if r == h or c == w: return z
            k -= g[r][c]
            if k<0 or next((1 for i in range(z-1,-1,-1)if(k:=k-g[y+i][c]-g[r][x+i])<0),0):
                return z
            return f(k,y,x,z+1)
        return max(t>=g[i][j]and f(t-g[i][j],i,j,1)for i in range(h)for j in range(w))

class Solution:
    def maxSideLength(self, g: List[List[int]], t: int) -> int:
        h, w = len(g), len(g[0])
        def f(x, y, z):
            if x + z - 1 >= h or y + z - 1 >= w: return 0
            if sum(sum(r[y:y + z]) for r in g[x:x + z]) <= t:
                return 1 + f(x, y, z + 1)
            return 0
        return~-max((k:=1)and[k:=k+f(i,j,k)for j in range(w)][-1]for i in range(h))

class Solution:
    def maxSideLength(self, g: List[List[int]], t: int) -> int:
        h,w=len(g),len(g[0]);f=lambda x,y,z:h-x>z-1<w-y and t>=sum(sum(r[y:y+z])for r in g[x:x+z])and 1+f(x,y,z+1);return~-max((k:=1)and[k:=k+f(i,j,k)for j in range(w)][-1]for i in range(h))

class Solution:
    def maxSideLength(self, g: List[List[int]], t: int) -> int:
        h,w,s=len(g),len(g[0]),0;f=lambda x,y,z:h-x>=z<=w-y and t>=sum(sum(r[y:y+z])for r in g[x:x+z])and-~f(x,y,z+1);[s:=s+f(i,j,s+1)for i in range(h)for j in range(w)];return s

test('''
1292. Maximum Side Length of a Square with Sum Less than or Equal to Threshold
Medium
Topics
premium lock icon
Companies
Hint
Given a m x n matrix mat and an integer threshold, return the maximum side-length of a square with a sum less than or equal to threshold or return 0 if there is no such square.

 

Example 1:


Input: mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4
Output: 2
Explanation: The maximum side length of square with sum less than 4 is 2 as shown.
Example 2:

Input: mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], threshold = 1
Output: 0

Other examples:

Input: mat = [[18,70],[61,1],[25,85],[14,40],[11,96],[97,96],[63,45]], threshold = 40184
Output: 2

Input: mat = [[5,5,1],[5,5,5],[5,5,5]], threshold = 1
Output: 1

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 300
0 <= mat[i][j] <= 104
0 <= threshold <= 105
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
60,805/103.3K
Acceptance Rate
58.9%
Topics
Array
Binary Search
Matrix
Prefix Sum
Weekly Contest 167
icon
Companies
Hint 1
Store prefix sum of all grids in another 2D array.
Hint 2
Try all possible solutions and if you cannot find one return -1.
Hint 3
If x is a valid answer then any y < x is also valid answer. Use binary search to find answer.
''')
