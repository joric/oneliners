from lc import *

# https://leetcode.com/problems/validate-binary-tree-nodes/discuss/2770216/Python-(Simple-Union-Find)
# unicode find: https://leetcode.com/problems/redundant-connection/discuss/108002/Unicode-Find-(5-short-lines)

class Solution:
    def validateBinaryTreeNodes(self, n: int, l: List[int], r: List[int]) -> bool:
        t,c=''.join(map(chr, range(n))),set()
        for u in range(n):
            for v in (l[u], r[u]):
                if v != -1:
                    if v in c or t[u]==t[v]:
                        return False
                    t = t.replace(t[u],t[v])
                    c.add(v)
        return len({*t})==1

class Solution:
    def validateBinaryTreeNodes(self, n: int, L: List[int], R: List[int]) -> bool:
        t = 1 + sum(x != -1 for x in L + R)
        print(t, len(L), len(R))
        return len(L)==t

class Solution:
    def validateBinaryTreeNodes(self, n: int, l: List[int], r: List[int]) -> bool:
        t,c=''.join(map(chr,range(n))),set();return any(v in c or t[u]==t[v]or not(t:=t.replace(t[u],t[v]),c.add(v))for u in range(n)for v in(l[u],r[u])if v!=-1)==1-len({*t})

test('''
1361. Validate Binary Tree Nodes
Medium

1266

345

Add to List

Share
You have n binary tree nodes numbered from 0 to n - 1 where node i has two children leftChild[i] and rightChild[i], return true if and only if all the given nodes form exactly one valid binary tree.

If node i has no left child then leftChild[i] will equal -1, similarly for the right child.

Note that the nodes have no values and that we only use the node numbers in this problem.

 

Example 1:


Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
Output: true
Example 2:


Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]
Output: false
Example 3:


Input: n = 2, leftChild = [1,0], rightChild = [-1,-1]
Output: false


Example 4:

Input: n = 3, leftChild = [1,-1,-1], rightChild = [-1,-1,1]
Output: false

Example 5:

Input: n = 4, leftChild = [3,-1,1,-1], rightChild = [-1,-1,0,-1]
Output: true

Example 6:

Input: n = 4, leftChild = [1,0,3,-1], rightChild = [-1,-1,-1,-1]
Output: false

Example 7:

Input: n = 4, leftChild = [1, 2, 0, -1], rightChild = [-1, -1, -1, -1]
Output: false

Constraints:

n == leftChild.length == rightChild.length
1 <= n <= 10^4
-1 <= leftChild[i], rightChild[i] <= n - 1
''')

