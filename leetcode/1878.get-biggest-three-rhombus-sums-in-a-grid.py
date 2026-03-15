from lc import *

# https://leetcode.com/problems/get-biggest-three-rhombus-sums-in-a-grid/solutions/1238730/python-dp-omnminmn-solution-explained-by-fq5s/?envType=daily-question&envId=2026-03-16

class Solution:
    def getBiggestThree(self, g: List[List[int]]) -> List[int]:
        m,n,h=len(g),len(g[0]),[];[*map(u:=lambda x:x in h or(heappush(h,x),h[3:]and heappop(h)),chain(*g))];f=cache(lambda i,j,k:n>i>-1<j<m and f(i-1,j+k,k)+g[j][i]);[u(f(i+q,j,-1)-f(i,j-q,-1)+f(i-1,j+q-1,-1)-f(i-q-1,j-1,-1)+f(i,j-q,1)-f(i-q,j,1)+f(i+q-1,j+1,1)-f(i-1,j+q+1,1))for q in range(1,(1+min(m,n))//2)for i in range(q,n-q)for j in range(q,m-q)];return sorted(h)[::-1]

test('''
1878. Get Biggest Three Rhombus Sums in a Grid
Medium
Topics
premium lock icon
Companies
Hint
You are given an m x n integer matrix grid​​​.

A rhombus sum is the sum of the elements that form the border of a regular rhombus shape in grid​​​. The rhombus must have the shape of a square rotated 45 degrees with each of the corners centered in a grid cell. Below is an image of four valid rhombus shapes with the corresponding colored cells that should be included in each rhombus sum:


Note that the rhombus can have an area of 0, which is depicted by the purple rhombus in the bottom right corner.

Return the biggest three distinct rhombus sums in the grid in descending order. If there are less than three distinct values, return all of them.

 

Example 1:


Input: grid = [[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]]
Output: [228,216,211]
Explanation: The rhombus shapes for the three biggest distinct rhombus sums are depicted above.
- Blue: 20 + 3 + 200 + 5 = 228
- Red: 200 + 2 + 10 + 4 = 216
- Green: 5 + 200 + 4 + 2 = 211
Example 2:


Input: grid = [[1,2,3],[4,5,6],[7,8,9]]
Output: [20,9,8]
Explanation: The rhombus shapes for the three biggest distinct rhombus sums are depicted above.
- Blue: 4 + 2 + 6 + 8 = 20
- Red: 9 (area 0 rhombus in the bottom right corner)
- Green: 8 (area 0 rhombus in the bottom middle)
Example 3:

Input: grid = [[7,7,7]]
Output: [7]
Explanation: All three possible rhombus sums are the same, so return [7].
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
1 <= grid[i][j] <= 105
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
20,647/41.1K
Acceptance Rate
50.3%
Topics
Staff
Array
Math
Sorting
Heap (Priority Queue)
Matrix
Prefix Sum
Biweekly Contest 53
icon
Companies
Hint 1
You need to maintain only the biggest 3 distinct sums
Hint 2
The limits are small enough for you to iterate over all rhombus sizes then iterate over all possible borders to get the sums
Similar Questions
Count Fertile Pyramids in a Land
Hard
''')
