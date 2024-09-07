from lc import *

# https://leetcode.com/problems/linked-list-in-binary-tree/discuss/3331916/2-line-recursion-solution-in-java

class Solution:
    def isSubPath(self, h: Optional[ListNode], r: Optional[TreeNode]) -> bool:
        f=lambda h,r:not h or r and h.val==r.val and (f(h.next,r.left)or f(h.next,r.right));return r and (f(h,r) or self.isSubPath(h,r.left)or self.isSubPath(h,r.right))

# POTD 2024-09-07

class Solution:
    def isSubPath(self, h: Optional[ListNode], r: Optional[TreeNode]) -> bool:
        f=lambda h,r:not h or r and h.val==r.val and(f(h.next,r.left)or f(h.next,r.right));return(g:=lambda h,r:r and(f(h,r)or g(h,r.left)or g(h,r.right)))(h,r)

test('''
1367. Linked List in Binary Tree
Medium

2252

67

Add to List

Share
Given a binary tree root and a linked list with head as the first node. 

Return True if all the elements in the linked list starting from the head correspond to some downward path connected in the binary tree otherwise return False.

In this context downward path means a path that starts at some node and goes downwards.

 

Example 1:



Input: head = [4,2,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: true
Explanation: Nodes in blue form a subpath in the binary Tree.  
Example 2:



Input: head = [1,4,2,6], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: true
Example 3:

Input: head = [1,4,2,6,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: false
Explanation: There is no path in the binary tree that contains all the elements of the linked list from head.
 

Constraints:

The number of nodes in the tree will be in the range [1, 2500].
The number of nodes in the list will be in the range [1, 100].
1 <= Node.val <= 100 for each node in the linked list and binary tree.
Accepted
79,088
Submissions
179,370
''')