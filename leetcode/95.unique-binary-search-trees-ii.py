from lc import *

# https://leetcode.com/problems/unique-binary-search-trees-ii/discuss/31495/Should-be-6-Liner

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return(f:=lambda a,b:[TreeNode(x,l,r)for x in range(a,b+1)for l in f(a,x-1)for r in f(x+1,b)]or[None])(1,n)

test('''
95. Unique Binary Search Trees II
Medium

6206

403

Add to List

Share
Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

 

Example 1:


Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
Example 2:

Input: n = 1
Output: [[1]]
 

Constraints:

1 <= n <= 8
''')
