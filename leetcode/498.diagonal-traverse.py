from lc import *

# https://leetcode.com/problems/diagonal-traverse/solutions/405383/1-line-python-3-solution/?envType=daily-question&envId=2025-08-25

class Solution:
    def findDiagonalOrder(self, m:List[List[int]]) -> List[int]:
        return[a[2]for a in sorted((i+j,(i-j)*((i+j)%2*2-1),m[i][j])for i in range(len(m))for j in range(len(m[0])))]

class Solution:
    def findDiagonalOrder(self, m:List[List[int]]) -> List[int]:
        e=enumerate;return[a[2]for a in sorted((i+j,(i-j)*((i+j)%2*2-1),x)for i,r in e(m)for j,x in e(r))]

class Solution:
    def findDiagonalOrder(self, m:List[List[int]]) -> List[int]:
        e=enumerate;return[a[2]for a in sorted((i+j,(-1)**(i+j+1)*(i-j),x)for i,r in e(m)for j,x in e(r))]

test('''
498. Diagonal Traverse
Solved
Medium
Topics
premium lock icon
Companies
Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

 

Example 1:


Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]
Example 2:

Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
-105 <= mat[i][j] <= 105
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
408,261/642.7K
Acceptance Rate
63.5%
Topics
Array
Matrix
Simulation
icon
Companies
Similar Questions
Decode the Slanted Ciphertext
Medium
''')
