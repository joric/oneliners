from lc import *

# https://leetcode.com/problems/minimum-swaps-to-arrange-a-binary-grid/solutions/768029/python-greedy-on2-15-lines-600ms-by-gdko-vv4e/?envType=daily-question&envId=2026-03-02

class Solution:
    def minSwaps(self, a: List[List[int]]) -> int:
        n = len(a)
        r = 0
        for i in range(n-1):
            if not all(v==0 for v in a[i][i+1:]):
                for j in range(i+1, n):
                    if all(v==0 for v in a[j][i+1:]):
                        a.insert(i,a.pop(j))
                        r += j-i
                        break
                    elif j == n-1:
                        return -1
        return r

class Solution:
    def minSwaps(self, a: List[List[int]]) -> int:
        n=len(a);return max(-1,sum(next((j-i for j in range(i,n)if not(any(a[j][i+1:])or a.insert(i,a.pop(j)))),-inf)for i in range(n-1)))

class Solution:
    def minSwaps(self, a: List[List[int]]) -> int:
        return max(-1,sum(next((k for k,r in enumerate(a[i:])if not(any(r[i+1:])or a.insert(i,a.pop(i+k)))),-inf)for i in range(len(a))))

test('''
1536. Minimum Swaps to Arrange a Binary Grid
Medium
Topics
premium lock icon
Companies
Hint
Given an n x n binary grid, in one step you can choose two adjacent rows of the grid and swap them.

A grid is said to be valid if all the cells above the main diagonal are zeros.

Return the minimum number of steps needed to make the grid valid, or -1 if the grid cannot be valid.

The main diagonal of a grid is the diagonal that starts at cell (1, 1) and ends at cell (n, n).

 

Example 1:


Input: grid = [[0,0,1],[1,1,0],[1,0,0]]
Output: 3
Example 2:


Input: grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
Output: -1
Explanation: All rows are similar, swaps have no effect on the grid.
Example 3:


Input: grid = [[1,0,0],[1,1,0],[1,1,1]]
Output: 0


Other examples:

Input: grid = [[0,1,1,0],[1,1,1,0],[1,1,1,0],[1,0,0,0]]
Output: -1

Constraints:

n == grid.length == grid[i].length
1 <= n <= 200
grid[i][j] is either 0 or 1
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
18,626/37.8K
Acceptance Rate
49.3%
Topics
Staff
Array
Greedy
Matrix
Weekly Contest 200
icon
Companies
Hint 1
For each row of the grid calculate the most right 1 in the grid in the array maxRight.
Hint 2
To check if there exist answer, sort maxRight and check if maxRight[i] ≤ i for all possible i's.
Hint 3
If there exist an answer, simulate the swaps.
''')
