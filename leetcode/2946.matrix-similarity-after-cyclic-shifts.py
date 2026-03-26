from lc import *

# https://leetcode.com/problems/matrix-similarity-after-cyclic-shifts/solutions/7515141/simple-o1-space-one-liner-by-asnorkin-5myq/?envType=daily-question&envId=2026-03-27

class Solution:
    def areSimilar(self, m: List[List[int]], k: int) -> bool:
        return all(all(r[c]==r[(c+[k,-k][t%2])%len(m[0])]for c in range(len(m[0])))for t,r in enumerate(m))

# https://leetcode.com/problems/matrix-similarity-after-cyclic-shifts/solutions/4331812/one-line-solution-by-seaqen_kani-3jgy/?envType=daily-question&envId=2026-03-27

class Solution:
    def areSimilar(self, m: List[List[int]], k: int) -> bool:
        return all(m[x][y]==m[x][(y+k)%len(m[0])]for x in range(len(m))for y in range(len(m[0])))

# https://leetcode.com/problems/matrix-similarity-after-cyclic-shifts/description/?envType=daily-question&envId=2026-03-27

class Solution:
    def areSimilar(self, m: List[List[int]], k: int) -> bool:
        return(n:=len(m[0]))and all(r[i]==r[(i+k)%n]for i in range(n)for r in m)

class Solution:
    def areSimilar(self, m: List[List[int]], k: int) -> bool:
        return all(r==r[k%len(r):]+r[:k%len(r)]for r in m)

test('''
2946. Matrix Similarity After Cyclic Shifts
Solved
Easy
Topics
premium lock icon
Companies
Hint
You are given an m x n integer matrix mat and an integer k. The matrix rows are 0-indexed.

The following proccess happens k times:

Even-indexed rows (0, 2, 4, ...) are cyclically shifted to the left.


Odd-indexed rows (1, 3, 5, ...) are cyclically shifted to the right.


Return true if the final modified matrix after k steps is identical to the original matrix, and false otherwise.

 

Example 1:

Input: mat = [[1,2,3],[4,5,6],[7,8,9]], k = 4

Output: false

Explanation:

In each step left shift is applied to rows 0 and 2 (even indices), and right shift to row 1 (odd index).



Example 2:

Input: mat = [[1,2,1,2],[5,5,5,5],[6,3,6,3]], k = 2

Output: true

Explanation:



Example 3:

Input: mat = [[2,2],[2,2]], k = 3

Output: true

Explanation:

As all the values are equal in the matrix, even after performing cyclic shifts the matrix will remain the same.

 

Constraints:

1 <= mat.length <= 25
1 <= mat[i].length <= 25
1 <= mat[i][j] <= 25
1 <= k <= 50
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
31,210/52.4K
Acceptance Rate
59.5%
Topics
Mid Level
Array
Math
Matrix
Simulation
Weekly Contest 373
icon
Companies
Hint 1
You can reduce k shifts to (k % n) shifts as after n shifts the matrix will become similar to the initial matrix.
''')
