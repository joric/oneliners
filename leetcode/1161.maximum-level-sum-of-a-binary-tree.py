from lc import *

# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/description/?envType=daily-question&envId=2026-01-06

class Solution:
    def maxLevelSum(self, t: TreeNode) -> int:
        c=Counter();f=lambda n,d:n and(c.update({d:n.val}),f(n.left,d+1),f(n.right,d+1));f(t,1);return max(c,key=c.get)

test('''
1161. Maximum Level Sum of a Binary Tree
Medium

2014

71

Add to List

Share
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

 

Example 1:


Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.
Example 2:

Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [1, 10^4].
-10^5 <= Node.val <= 10^5
Accepted
132,994
Submissions
201,317
Seen this question in a real interview before?

Yes

No
Calculate the sum for each level then find the level with the maximum sum.
How can you traverse the tree ?
How can you sum up the values for every level ?
Use DFS or BFS to traverse the tree keeping the level of each node, and sum up those values with a map or a frequency array.
''')
