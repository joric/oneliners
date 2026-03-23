from lc import *

# https://leetcode.com/problems/construct-product-matrix/solutions/4173067/python-3-7-lines-flatten-solve-fold-back-5uk2/?envType=daily-question&envId=2026-03-24

class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        mod = 12345
        m, n = len(grid), len(grid[0])
        myMul = lambda x, y : (x*y) % mod
        arr = list(chain(*grid))                                    #  <-- flatten
        pref = list(accumulate(arr,       myMul, initial=1))        #
        suff = list(accumulate(arr[::-1], myMul, initial=1))[::-1]  #  <-- solve
        ans = [p*s %mod for p,s in zip(pref,suff[1:])]              #
        return list(zip(*[iter(ans)] * n))                          #  <-- fold back up

# https://leetcode.com/problems/construct-product-matrix/solutions/7681213/four-simple-lines-of-code-by-mikposp-hgaz/?envType=daily-question&envId=2026-03-24

class Solution:
    def constructProductMatrix(self, g: List[List[int]]) -> List[List[int]]:
        f = lambda a:[1,*accumulate(a,lambda q,v:q*v%12345)]
        pref,suff = f(chain(*g)),f(chain(*map(reversed,reversed(g))))[::-1]
        b = (v*u%12345 for v,u in zip(pref,suff[1:]))
        return [*zip(*[iter(b)]*len(g[0]))]

class Solution:
    def constructProductMatrix(self, g: List[List[int]]) -> List[List[int]]:
        f=lambda a:[1,*accumulate(a,lambda q,v:q*v%12345)];p,s=f(chain(*g)),f(chain(*map(reversed,reversed(g))))[::-1];b=(v*u%12345 for v,u in zip(p,s[1:]));return [*zip(*[iter(b)]*len(g[0]))]

class Solution:
    def constructProductMatrix(self, g: List[List[int]]) -> List[List[int]]:
        c=sum(g,[]);f=lambda x:[1,*accumulate(x,lambda q,v:q*v%12345)];s=f(c[::-1])[::-1];b=iter(x*y%12345for x,y in zip(f(c),s[1:]));return[*zip(*[b]*len(g[0]))]

class Solution:
    def constructProductMatrix(self, g: List[List[int]]) -> List[List[int]]:
        c=sum(g,[]);f=lambda v:[x:=1]+[x:=x*y%12345 for y in v];return[*zip(*[map(lambda x,y:x*y%12345,f(c),f(c[::-1])[-2::-1])]*len(g[0]))]

class Solution:
    def constructProductMatrix(self, g: List[List[int]]) -> List[List[int]]:
        t=lambda x,y:x*y%12345;c=sum(g,[]);f=lambda v:[x:=1]+[x:=t(x,y)for y in v];return[*zip(*[map(t,f(c),f(c[::-1])[-2::-1])]*len(g[0]))]

class Solution:
    def constructProductMatrix(self, g: List[List[int]]) -> List[List[int]]:
        t=lambda x,y:x*y%12345;f=lambda v:[*accumulate([1]+v,t)];return[*zip(*[map(t,f(c:=sum(g,[])),f(c[::-1])[-2::-1])]*len(g[0]))]

test('''
2906. Construct Product Matrix
Medium
Topics
premium lock icon
Companies
Hint
Given a 0-indexed 2D integer matrix grid of size n * m, we define a 0-indexed 2D matrix p of size n * m as the product matrix of grid if the following condition is met:

Each element p[i][j] is calculated as the product of all elements in grid except for the element grid[i][j]. This product is then taken modulo 12345.
Return the product matrix of grid.

 

Example 1:

Input: grid = [[1,2],[3,4]]
Output: [[24,12],[8,6]]
Explanation: p[0][0] = grid[0][1] * grid[1][0] * grid[1][1] = 2 * 3 * 4 = 24
p[0][1] = grid[0][0] * grid[1][0] * grid[1][1] = 1 * 3 * 4 = 12
p[1][0] = grid[0][0] * grid[0][1] * grid[1][1] = 1 * 2 * 4 = 8
p[1][1] = grid[0][0] * grid[0][1] * grid[1][0] = 1 * 2 * 3 = 6
So the answer is [[24,12],[8,6]].
Example 2:

Input: grid = [[12345],[2],[1]]
Output: [[2],[0],[0]]
Explanation: p[0][0] = grid[0][1] * grid[0][2] = 2 * 1 = 2.
p[0][1] = grid[0][0] * grid[0][2] = 12345 * 1 = 12345. 12345 % 12345 = 0. So p[0][1] = 0.
p[0][2] = grid[0][0] * grid[0][1] = 12345 * 2 = 24690. 24690 % 12345 = 0. So p[0][2] = 0.
So the answer is [[2],[0],[0]].
 

Constraints:

1 <= n == grid.length <= 105
1 <= m == grid[i].length <= 105
2 <= n * m <= 105
1 <= grid[i][j] <= 109
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
17,495/54K
Acceptance Rate
32.4%
Topics
Staff
Array
Matrix
Prefix Sum
Weekly Contest 367
icon
Companies
Hint 1
Try to solve this without using the '/' (division operation).
Hint 2
Create two 2D arrays for suffix and prefix product, and use them to find the product for each position.
Similar Questions
Product of Array Except Self
Medium
''')
