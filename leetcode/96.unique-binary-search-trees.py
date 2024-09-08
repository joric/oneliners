from lc import *

# https://leetcode.com/problems/unique-binary-search-trees

class Solution:
    def numTrees(self, n: int) -> int:
        return factorial(2*n)//(factorial(n)*factorial(n+1))

test('''
96. Unique Binary Search Trees
Medium

10408

407

Add to List

Share
Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

 

Example 1:


Input: n = 3
Output: 5
Example 2:

Input: n = 1
Output: 1
 

Constraints:

1 <= n <= 19
Accepted
690,920
Submissions
1,123,259
''')
