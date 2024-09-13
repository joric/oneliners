from lc import *

# https://leetcode.com/problems/path-sum-ii/discuss/5529668/shortest-and-simplest-friendly-solution

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        paths = self.pathSum(root.left, targetSum - root.val) + self.pathSum(root.right, targetSum - root.val)
        for i in range(len(paths)):
            paths[i] = [root.val] + paths[i]
        if targetSum == root.val and root.left is None and root.right is None:
            paths.append([root.val])
        return paths

# https://leetcode.com/problems/path-sum-ii/discuss/1382332/C%2B%2BPython-DFS-Clean-and-Concise-Time-complexity-explained

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        def dfs(root, targetSum, path):
            if root == None: return None
            targetSum -= root.val
            path.append(root.val)
            if root.left == None and root.right == None:
                if targetSum == 0:
                    ans.append(path.copy())
            else:
                dfs(root.left, targetSum, path)
                dfs(root.right, targetSum, path)
            path.pop()
        ans = []
        dfs(root, targetSum, [])
        return ans

# https://leetcode.com/problems/path-sum-ii/discuss/254431/Python-One-Line-DFS

class Solution:
    def pathSum(self, t: TreeNode, s: int) -> List[List[int]]:
        return [] if not t else [[t.val]] if not (t.left or t.right) and t.val == s else [[t.val] + p for p in self.pathSum(t.left,s-t.val) + self.pathSum(t.right, s-t.val)]

class Solution:
    def pathSum(self, t: TreeNode, s: int) -> List[List[int]]:
        return(f:=lambda t,s:t and(not((r:=s-t.val)or t.left or t.right)and[[t.val]]or[[t.val]+p for p in f(t.left,r)+f(t.right,r)])or[])(t,s)

test('''
113. Path Sum II
Medium

8007

156

Add to List

Share
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

 

Example 1:


Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22
Example 2:


Input: root = [1,2,3], targetSum = 5
Output: []
Example 3:

Input: root = [1,2], targetSum = 0
Output: []
 

Other examples:

Input: root = [1,2], targetSum = 1
Output: []

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000
Accepted
904,475
Submissions
1,529,283
''')
