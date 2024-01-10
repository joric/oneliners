from lc import *

# https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/discuss/4538587/Python-Graph-DFS-Solution

class Solution:
    def amountOfTime(self, r: Optional[TreeNode], s: int) -> int:
        e = defaultdict(list)
        v = set()
        def g(r):
            if r:
                if r.left:
                    e[r.val].append(r.left.val)
                    e[r.left.val].append(r.val)
                    g(r.left)
                if r.right:
                    e[r.val].append(r.right.val)
                    e[r.right.val].append(r.val)
                    g(r.right)
        def f(i,d):
            v.add(i)
            m = d
            for j in e[i]:
                if j in v:
                    continue
                m = max(m, f(j, d + 1))
            return m
        g(r)
        return f(s,0)

class Solution:
    def amountOfTime(self, r: Optional[TreeNode], s: int) -> int:
        e,v=defaultdict(list),set()
        (g:=lambda r:r and[(e[r.val].append(p.val),e[p.val].append(r.val),g(p))for p in(r.left,r.right)if p])(r)
        return(f:=lambda i,d:v.add(i)or max([d]+[f(j,d+1)for j in e[i]if j not in v]))(s,0)

class Solution:
    def amountOfTime(self, r: Optional[TreeNode], s: int) -> int:
        e,v=defaultdict(list),set();(g:=lambda r:r and[(e[r.val].append(p.val),e[p.val].append(r.val),g(p))for p in(r.left,r.right)if p])(r);return(f:=lambda i,d:v.add(i)or max([d]+[f(j,d+1)for j in e[i]if j not in v]))(s,0)

# https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/discuss/2467516/Python3-DFS-Efficient-Solution

class Solution:
    def amountOfTime(self, r: Optional[TreeNode], s: int) -> int:
        def f(n):
            if not n:
                return -1, 0
            p,l = f(n.left)
            q,r = f(n.right)
            if n.val == s:
                return 0,max(l,r)
            if p>=0:
                return p+1,max(p+1,l,p+r+1)
            if q>=0:
                return q+1,max(q+1,r,q+l+1)
            return -1,max(l,r)+1
        return f(r)[1]

class Solution:
    def amountOfTime(self, r: Optional[TreeNode], s: int) -> int:
        return(f:=lambda n:n and(lambda p,l,q,r:(0,max(l,r))if n.val==s else(p+1,max(p+1,l,p+r+1))if p>=0 else(q+1,max(q+1,r,q+l+1))if q>=0 else(-1,max(l,r)+1))(*f(n.left),*f(n.right))or(-1,0))(r)[1]

# another solution

class Solution:
    def amountOfTime(self, n: Optional[TreeNode], s: int) -> int:
        return(f:=lambda n:(n.val==s)*(1,1,max((l:=f(n.left))[0],(r:=f(n.right))[0]))or(l[1]+r[1])*(1+l[1]*l[0]+r[1]*r[0],1,max(l[0]+r[0],l[2],r[2]))or(1+max(l[0],r[0]),0,0)if n else(0,0,0))(n)[2]

class Solution:
    def amountOfTime(self, n: Optional[TreeNode], s: int) -> int:
        return(f:=lambda n:n and(lambda a,b,c,d,e,f:(n.val==s)*(1,1,max(a,d))or(b+e)*(1+b*a+e*d,1,max(a+d,c,f))or(1+max(a,d),0,0))(*f(n.left),*f(n.right))or[0]*3)(n)[2]

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
 

Example 3:

Input: root = [1,2,null,3,null,4,null,5], start = 2
Output: 3

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

