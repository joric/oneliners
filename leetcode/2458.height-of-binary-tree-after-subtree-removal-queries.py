from lc import *

# https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries/discuss/2758375/Python3-C%2B%2B-Clean-9-lines-Dfs

class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        ans = {}
        @cache
        def height(r): return 1 + max(height(r.left), height(r.right)) if r else 0
        def dfs(r, depth, mx):
            if not r: return
            ans[r.val] = mx
            dfs(r.left, depth + 1, max(mx, depth + height(r.right)))
            dfs(r.right, depth + 1, max(mx, depth + height(r.left)))
        dfs(root, 0, 0)
        return [ans[v] for v in queries]

class Solution:
    def treeQueries(self, r: Optional[TreeNode], q: List[int]) -> List[int]:
        a={};h=cache(lambda t:t and 1+max(h(t.left),h(t.right))or 0);f=lambda t,d,m:t and(setitem(a,t.val,m),f(t.left,d+1,max(m,d+h(t.right))),f(t.right,d+1,max(m,d+h(t.left))));f(r,0,0);return[a[v] for v in q]

class Solution:
    def treeQueries(self, r: Optional[TreeNode], q: List[int]) -> List[int]:
        a={};h=cache(lambda t:t and 1+max(h(t.left),h(t.right))or 0);f=lambda t,d,m:t and(setitem(a,t.val,m),f(l:=t.left,d+1,max(m,d+h(r:=t.right))),f(r,d+1,max(m,d+h(l))));f(r,0,0);return[a[v] for v in q]

test('''
2458. Height of Binary Tree After Subtree Removal Queries
Hard

868

19

Add to List

Share
You are given the root of a binary tree with n nodes. Each node is assigned a unique value from 1 to n. You are also given an array queries of size m.

You have to perform m independent queries on the tree where in the ith query you do the following:

Remove the subtree rooted at the node with the value queries[i] from the tree. It is guaranteed that queries[i] will not be equal to the value of the root.
Return an array answer of size m where answer[i] is the height of the tree after performing the ith query.

Note:

The queries are independent, so the tree returns to its initial state after each query.
The height of a tree is the number of edges in the longest simple path from the root to some node in the tree.
 

Example 1:


Input: root = [1,3,4,2,null,6,5,null,null,null,null,null,7], queries = [4]
Output: [2]
Explanation: The diagram above shows the tree after removing the subtree rooted at node with value 4.
The height of the tree is 2 (The path 1 -> 3 -> 2).
Example 2:


Input: root = [5,8,9,2,1,3,7,4,6], queries = [3,2,4,8]
Output: [3,2,3,2]
Explanation: We have the following queries:
- Removing the subtree rooted at node with value 3. The height of the tree becomes 3 (The path 5 -> 8 -> 2 -> 4).
- Removing the subtree rooted at node with value 2. The height of the tree becomes 2 (The path 5 -> 8 -> 1).
- Removing the subtree rooted at node with value 4. The height of the tree becomes 3 (The path 5 -> 8 -> 2 -> 6).
- Removing the subtree rooted at node with value 8. The height of the tree becomes 2 (The path 5 -> 9 -> 3).
 

Constraints:

The number of nodes in the tree is n.
2 <= n <= 105
1 <= Node.val <= n
All the values in the tree are unique.
m == queries.length
1 <= m <= min(n, 104)
1 <= queries[i] <= n
queries[i] != root.val
Accepted
28,250
Submissions
68,098
''')
