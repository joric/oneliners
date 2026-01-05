from lc import *

# https://leetcode.com/problems/maximum-matrix-sum/discuss/3088994/Python-3-line-solution-or-negative-frequency-is-evenodd

class Solution:
    def maxMatrixSum(self, m: List[List[int]]) -> int:
        return sum(abs(x)for r in m for x in r)-2*(sum(x<1 for r in m for x in r)%2 and min(abs(x) for r in m for x in r)or 0)

class Solution:
    def maxMatrixSum(self, m: List[List[int]]) -> int:
        t=[x for r in m for x in r];p=[*map(abs,t)];return sum(p)-2*(sum(map(0..__ge__,t))%2 and min(p))

class Solution:
    def maxMatrixSum(self, m: List[List[int]]) -> int:
        p=[*map(abs,t:=[*chain(*m)])];return sum(p)-2*(sum(map(0..__ge__,t))%2 and min(p))

class Solution:
    def maxMatrixSum(self, m: List[List[int]]) -> int:
        p=[*map(abs,t:=[*chain(*m)])];return sum(p)-2*(sum(x<1 for x in t)%2*min(p))

# 2026-01-05 POTD

class Solution:
    def maxMatrixSum(self, m: List[List[int]]) -> int:
        return sum(p:=[*map(abs,t:=sum(m,[]))])-sum(x<0 for x in t)%2*2*min(p)

test('''
1975. Maximum Matrix Sum
Medium

570

25

Add to List

Share
You are given an n x n integer matrix. You can do the following operation any number of times:

Choose any two adjacent elements of matrix and multiply each of them by -1.
Two elements are considered adjacent if and only if they share a border.

Your goal is to maximize the summation of the matrix's elements. Return the maximum sum of the matrix's elements using the operation mentioned above.

 

Example 1:


Input: matrix = [[1,-1],[-1,1]]
Output: 4
Explanation: We can follow the following steps to reach sum equals 4:
- Multiply the 2 elements in the first row by -1.
- Multiply the 2 elements in the first column by -1.
Example 2:


Input: matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]
Output: 16
Explanation: We can follow the following step to reach sum equals 16:
- Multiply the 2 last elements in the second row by -1.
 

Other examples:

Input: matrix = [[10000,10000,10000],[10000,10000,10000],[10000,10000,10000]]
Output: 90000

Constraints:

n == matrix.length == matrix[i].length
2 <= n <= 250
-105 <= matrix[i][j] <= 105
Accepted
20,967
Submissions
41,241
''')
