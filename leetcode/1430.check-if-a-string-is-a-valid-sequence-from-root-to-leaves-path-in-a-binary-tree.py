from lc import *

# https://leetcode.com/problems/check-if-a-string-is-a-valid-sequence-from-root-to-leaves-path-in-a-binary-tree

class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        def dfs(root, u):
            if root is None or root.val != arr[u]:
                return False
            if u == len(arr) - 1:
                return root.left is None and root.right is None
            return dfs(root.left, u + 1) or dfs(root.right, u + 1)
        return dfs(root, 0)

class Solution:
    def isValidSequence(self, t: TreeNode, a: List[int]) -> bool:
        def f(t,u):
            if not t or t.val != a[u]:
                return False
            if u == len(a) - 1:
                return not t.left and not t.right
            return f(t.left,u+1)or f(t.right,u+1)
        return f(t, 0)

class Solution:
    def isValidSequence(self, t: TreeNode, a: List[int]) -> bool:
        return(f:=lambda t,u:t!=None and t.val==a[u]and(f(t.left,u+1)or f(t.right,u+1)if u+1<len(a)else not t.left and not t.right))(t,0)

test('''
1430. Check if there is a root to leaf path with given sequence

Medium

Must be Premium, copied from github here
https://github.com/doocs/leetcode/blob/main/solution/1400-1499/1430.Check%20If%20a%20String%20Is%20a%20Valid%20Sequence%20from%20Root%20to%20Leaves%20Path%20in%20a%20Binary%20Tree/README_EN.md

Description
Given a binary tree where each path going from the root to any leaf form a valid sequence, check if a given string is a valid sequence in such binary tree. 

We get the given string from the concatenation of an array of integers arr and the concatenation of all values of the nodes along a path results in a sequence in the given binary tree.


Example 1:

Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,1,0,1]
Output: true
Explanation: 
The path 0 -> 1 -> 0 -> 1 is a valid sequence (green color in the figure). 
Other valid sequences are: 
0 -> 1 -> 1 -> 0 
0 -> 0 -> 0
Example 2:



Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,0,1]
Output: false 
Explanation: The path 0 -> 0 -> 1 does not exist, therefore it is not even a sequence.
Example 3:



Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,1,1]
Output: false
Explanation: The path 0 -> 1 -> 1 is a sequence, but it is not a valid sequence.
 

Constraints:

1 <= arr.length <= 5000
0 <= arr[i] <= 9
Each node's value is between [0 - 9].

''')