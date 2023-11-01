from lc import *

# editorial (boyer-moore + morris traversal) https://leetcode.com/problems/find-mode-in-binary-search-tree/solution

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def add(num):
            nonlocal max_streak, curr_streak, curr_num, ans
            if num == curr_num:
                curr_streak += 1
            else:
                curr_streak = 1
                curr_num = num

            if curr_streak > max_streak:
                ans = []
                max_streak = curr_streak

            if curr_streak == max_streak:
                ans.append(num)

        max_streak = 0
        curr_streak = 0
        curr_num = 0
        ans = []
        
        curr = root
        while curr:
            if curr.left:
                friend = curr.left
                while friend.right and friend.right != curr:
                    friend = friend.right
                
                if not friend.right:
                    friend.right = curr
                    curr = curr.left
                else:
                    friend.right = None
                    add(curr.val)
                    curr = curr.right
            else:
                add(curr.val)
                curr = curr.right
        
        return ans

# https://leetcode.com/problems/find-mode-in-binary-search-tree/discuss/2235862/Python-or-One-Pass-or-O(n)

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        c,m = Counter(),[0,set()]
        def f(r):
            if not r:
                return
            c[r.val] += 1
            if c[r.val] > m[0]:
                m[0] = c[r.val]
                m[1] = set([r.val])
            elif c[r.val] == m[0]:
                m[1].add(r.val)
            f(r.left)
            f(r.right)
        f(root)
        return m[1]

# https://leetcode.com/problems/find-mode-in-binary-search-tree/discuss/3645799/Python-3-oror-10-lines-dfs-oror-TM%3A-99-89

class Solution:
    def findMode(self, r: Optional[TreeNode]) -> List[int]:
        c = Counter();
        f = lambda r:r and(c.update({r.val:1}),f(r.left),f(r.right))
        f(r)
        m = max(c.values())
        return [k for k in c if c[k]==m]

# https://leetcode.com/problems/find-mode-in-binary-search-tree/discuss/471622/Python-3-(five-lines)-(52-ms)

class Solution:
    def findMode(self, r: Optional[TreeNode]) -> List[int]:
        return multimode((f:=lambda r:r and[r.val]+f(r.left)+f(r.right)or[])(r))

test('''
501. Find Mode in Binary Search Tree
Easy

3087

678

Add to List

Share
Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.

If the tree has more than one mode, return them in any order.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:


Input: root = [1,null,2,2]
Output: [2]
Example 2:

Input: root = [0]
Output: [0]
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-10^5 <= Node.val <= 10^5
''')

