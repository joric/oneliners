from lc import *

class Solution:
    def allPossibleFBT(s, n: int) -> List[Optional[TreeNode]]:
        t = [[]for _ in range(n+1)]
        t[1] = [TreeNode()]
        for k in range(n+1):
            for i in range(1,k-1,2):
                for l in t[i]:
                    for r in t[k-i-1]:
                        t[k].append(TreeNode(0,l,r))
        return t[-1]

class Solution:
    def allPossibleFBT(s, n: int) -> List[Optional[TreeNode]]:
        t = [[]for _ in range(n+1)];t[1]=[TreeNode()];[t[k].append(TreeNode(0,l,r))for k in range(n+1)for i in range(1,k-1,2)for l in t[i]for r in t[k-i-1]];return t[-1]

# https://leetcode.com/problems/all-possible-full-binary-trees/discuss/163429/Simple-Python-recursive-solution.

class Solution:
    def allPossibleFBT(s, n: int) -> List[Optional[TreeNode]]:
        t,n=[],n-1
        if n==0:
            return [TreeNode(0)]
        for i in range(1,min(20,n),2):
            for l in s.allPossibleFBT(i):
                for r in s.allPossibleFBT(n-i):
                    t += [TreeNode(0,l,r)]
        return t

class Solution:
    def allPossibleFBT(s, n: int) -> List[Optional[TreeNode]]:
        o,f,t,n=TreeNode,s.allPossibleFBT,[],n-1;return[(t:=t+[o(0,l,r)])for i in range(1,min(20,n),2)for l in f(i)for r in f(n-i)]and t if n else[o(0)]

test('''
894. All Possible Full Binary Trees
Medium

3688

262

Add to List

Share
Given an integer n, return a list of all possible full binary trees with n nodes. Each node of each tree in the answer must have Node.val == 0.

Each element of the answer is the root node of one possible tree. You may return the final list of trees in any order.

A full binary tree is a binary tree where each node has exactly 0 or 2 children.

 

Example 1:


Input: n = 7
Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
Example 2:

Input: n = 3
Output: [[0,0,0]]
 

Constraints:

1 <= n <= 20
''')

