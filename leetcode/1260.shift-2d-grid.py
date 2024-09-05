from lc import *

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        h, w = len(grid), len(grid[0])
        n = h * w
        shift = n - (k % n)
        def reverse(a, b):
            for i in range(a, (a + b)//2):
                j = a + b - i - 1
                grid[j//w][j%w], grid[i//w][i%w] = grid[i//w][i%w], grid[j//w][j%w]
        reverse(0, shift)
        reverse(shift, n)
        reverse(0, n)
        return grid

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        h, w = len(grid), len(grid[0])
        n = h * w
        shift = n - (k % n)
        for i in range(gcd(n, shift)):
            j = i
            while (k := (j + shift) % n) != i:
                grid[j//w][j%w], grid[k//w][k%w] = grid[k//w][k%w], grid[j//w][j%w]
                j = k
        return grid

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        return (a:=deque(chain.from_iterable(grid)), a.rotate(k % len(a))) and [list(row) for row in zip(*[iter(a)]*len(grid[0]))]


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        return (m:=len(grid),n:=len(grid[0])) and [[grid[(pos:=(i*n+j-k)%(m*n))//n][pos%n] for j in range(n)] for i in range(m)]

test('''

1260. Shift 2D Grid
Easy

1506

314

Add to List

Share
Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.

In one shift operation:

Element at grid[i][j] moves to grid[i][j + 1].
Element at grid[i][n - 1] moves to grid[i + 1][0].
Element at grid[m - 1][n - 1] moves to grid[0][0].
Return the 2D grid after applying shift operation k times.

 

Example 1:


Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
Output: [[9,1,2],[3,4,5],[6,7,8]]
Example 2:


Input: grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4
Output: [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]
Example 3:

Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9
Output: [[1,2,3],[4,5,6],[7,8,9]]
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m <= 50
1 <= n <= 50
-1000 <= grid[i][j] <= 1000
0 <= k <= 100

''')