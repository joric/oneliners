from lc import *

# https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/discuss/3265641/Python-Solution-that-bests-100-oror-10-Line-python-solution-oror-level-order-traversal

class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        summ = []
        tree = [root]
        while tree:
            temp = []
            summ += [sum(i.val for i in tree)]
            for i in tree: 
                if i.left: temp.append(i.left)
                if i.right: temp.append(i.right)
            tree = temp
        return sorted(summ)[-k] if len(summ)>=k else -1

# https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/discuss/3811485/Python-Easy-to-understand-solution-with-recursive-traversal

class Solution:
    def kthLargestLevelSum(self, t: Optional[TreeNode], k: int) -> int:
        c = Counter()
        m = 0
        def f(t,i):
            nonlocal m
            if not t:
                return
            m = max(m, i)
            c.update({i:t.val})
            f(t.left, i+1)
            f(t.right, i+1)
        f(t,0)
        return m>=k-1 and sorted(c.values())[-k] or -1

class Solution:
    def kthLargestLevelSum(self, t: Optional[TreeNode], k: int) -> int:
        c=Counter();return(f:=lambda t,i,m:t and(c.update({i:t.val})or max(f(t.left,i+1,m:=max(m,i)),f(t.right,i+1,m)))or m)(t,0,0)>=k-1 and sorted(c.values())[-k]or-1

test('''
2583. Kth Largest Sum in a Binary Tree
Medium

561

19

Add to List

Share
You are given the root of a binary tree and a positive integer k.

The level sum in the tree is the sum of the values of the nodes that are on the same level.

Return the kth largest level sum in the tree (not necessarily distinct). If there are fewer than k levels in the tree, return -1.

Note that two nodes are on the same level if they have the same distance from the root.

 

Example 1:


Input: root = [5,8,9,2,1,3,7,4,6], k = 2
Output: 13
Explanation: The level sums are the following:
- Level 1: 5.
- Level 2: 8 + 9 = 17.
- Level 3: 2 + 1 + 3 + 7 = 13.
- Level 4: 4 + 6 = 10.
The 2nd largest level sum is 13.
Example 2:


Input: root = [1,2,null,3], k = 1
Output: 3
Explanation: The largest level sum is 3.
 

Other examples:

Input: root = [705478,839185,null,null,588573,null,776836,630597,5167], k = 4
Output: 635764

Input: root = [411310,211244,111674], k = 2
Output: 322918

Input: root = [5,8,9,2,1,3,7], k = 4
Output: -1

Constraints:

The number of nodes in the tree is n.
2 <= n <= 105
1 <= Node.val <= 106
1 <= k <= n
Accepted
42,759
Submissions
89,039
''')
