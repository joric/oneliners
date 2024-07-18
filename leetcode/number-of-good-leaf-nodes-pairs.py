from lc import *

# https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/discuss/755767/Python-Postorder-Traversal

class Solution:
    def countPairs(self, r: TreeNode, d: int) -> int:
        c = 0
        def f(t):
            nonlocal c
            if not t:
                return []
            if t.left==t.right:
                return [1]
            l,r = f(t.left), f(t.right)
            c += sum(x+y<=d for x in l for y in r)
            return [x+1 for x in l+r if x+1<d]
        f(r)
        return c

class Solution:
    def countPairs(self, r: TreeNode, d: int) -> int:
        c=[0];(f:=lambda t:t and([1]if t.left==t.right else(l:=f(t.left),r:=f(t.right),setitem(c,0,c[0]+sum(x+y<=d for x in l for y in r)),[x+1 for x in l+r if x+1<d])[-1])or[])(r);return c[0]

class Solution:
    def countPairs(self, r: TreeNode, d: int) -> int:
        c=[0];(f:=lambda t:t and([1]if(l:=t.left)==(r:=t.right)else(l:=f(l),r:=f(r),setitem(c,0,c[0]+sum(x+y<=d for x in l for y in r)))and[x+1 for x in l+r if x+1<d])or[])(r);return c[0]

test('''
1530. Number of Good Leaf Nodes Pairs
Medium

1934

65

Add to List

Share
You are given the root of a binary tree and an integer distance. A pair of two different leaf nodes of a binary tree is said to be good if the length of the shortest path between them is less than or equal to distance.

Return the number of good leaf node pairs in the tree.

 

Example 1:


Input: root = [1,2,3,null,4], distance = 3
Output: 1
Explanation: The leaf nodes of the tree are 3 and 4 and the length of the shortest path between them is 3. This is the only good pair.
Example 2:


Input: root = [1,2,3,4,5,6,7], distance = 3
Output: 2
Explanation: The good pairs are [4,5] and [6,7] with shortest path = 2. The pair [4,6] is not good because the length of ther shortest path between them is 4.
Example 3:

Input: root = [7,1,4,6,null,5,3,null,null,null,null,null,2], distance = 3
Output: 1
Explanation: The only good pair is [2,5].


Other examples:

Input: root = [11,99,88,77,null,null,66,55,null,null,44,33,null,null,22], distance = 4
Output: 0

Constraints:

The number of nodes in the tree is in the range [1, 210].
1 <= Node.val <= 100
1 <= distance <= 10
Accepted
67,023
Submissions
100,589
''')
