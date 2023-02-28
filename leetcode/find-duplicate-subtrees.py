from lc import *

# https://leetcode.com/problems/find-duplicate-subtrees/discuss/106016/O(n)-time-and-space-lots-of-analysis

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        t = defaultdict(list)
        d = defaultdict()
        d.default_factory = d.__len__
        def f(x):
            if x:
                i = d[x.val,f(x.left),f(x.right)]
                t[i].append(x)
                return i
        f(root)
        return [r[0] for r in t.values() if r[1:]]

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        return (t:=defaultdict(list),d:=defaultdict(),setattr(d,'default_factory',d.__len__),
        (f:=lambda x:x and (t[i:=d[x.val,f(x.left),f(x.right)]].append(x) or i))(root),[r[0] for r in t.values() if r[1:]])[-1]

test('''
652. Find Duplicate Subtrees
Medium

4547

371

Add to List

Share
Given the root of a binary tree, return all duplicate subtrees.

For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with the same node values.

Example 1:

Input: root = [1,2,3,4,null,2,4,null,null,4]
Output: [[2,4],[4]]

Example 2:

Input: root = [2,1,1]
Output: [[1]]

Example 3:

Input: root = [2,2,2,3,null,3,null]
Output: [[2,3],[3]]

Example 4:

Input: root = [0,0,0,0,null,null,0,null,null,0]
Output: [[0,0],[0]]

Constraints:

The number of the nodes in the tree will be in the range [1, 5000]
-200 <= Node.val <= 200
''', check=lambda res,exp,_: sorted(json.loads(str(res)))==sorted(json.loads(str(exp)))
)

