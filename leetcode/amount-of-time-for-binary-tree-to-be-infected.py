from lc import *

# https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/discuss/2467516/Python3-DFS-Efficient-Solution

# TODO
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        def f(root):
            if root is None:
                return None, 0
            node_l, l = f(root.left)
            node_r, r = f(root.right)
            if root.val == start:
                return 0, max(l, r)
            if node_l is not None:
                return node_l + 1, max(node_l + 1, l, node_l + 1 + r)
            if node_r is not None:
                return node_r + 1, max(node_r + 1, r, node_r + 1 + l)
            return None, max(l, r) + 1
        return f(root)[1]

test('''
2385. Amount of Time for Binary Tree to Be Infected
Medium

1520

14

Add to List

Share
You are given the root of a binary tree with unique values, and an integer start. At minute 0, an infection starts from the node with value start.

Each minute, a node becomes infected if:

The node is currently uninfected.
The node is adjacent to an infected node.
Return the number of minutes needed for the entire tree to be infected.

 

Example 1:


Input: root = [1,5,3,null,4,10,6,9,2], start = 3
Output: 4
Explanation: The following nodes are infected during:
- Minute 0: Node 3
- Minute 1: Nodes 1, 10 and 6
- Minute 2: Node 5
- Minute 3: Node 4
- Minute 4: Nodes 9 and 2
It takes 4 minutes for the whole tree to be infected so we return 4.
Example 2:


Input: root = [1], start = 1
Output: 0
Explanation: At minute 0, the only node in the tree is infected so we return 0.
 

Constraints:

The number of nodes in the tree is in the range [1, 10^5].
1 <= Node.val <= 10^5
Each node has a unique value.
A node with a value of start exists in the tree.
Accepted
37,881
Submissions
64,205
''')

