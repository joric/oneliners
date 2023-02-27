from lc import *

class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

    def __eq__(self, other):
        return all(a==b if (not a or not b or a[0]==1 or b[0]==1) else True for a,b in zip(self.serialize(),other))

    def serialize(self):
        res = []
        root = self
        q = deque()
        res = []
        q.append(root)
        while len(q):
            nodes = len(q)
            for _ in range(nodes):
                root = q.popleft()
                res.append(root and [int(root.isLeaf), 1 if isinstance(root.val,str) else int(root.val)])
                if root:
                    q.append(root.topLeft)
                    q.append(root.topRight)
                    q.append(root.bottomLeft)
                    q.append(root.bottomRight)
        while res and res[-1] is None:
            res.pop()
        return res

    def __repr__(self):
        return str(self.serialize())

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def f(top, left, length):
            if length == 1:
                return Node(bool(grid[top][left]), True, None, None, None, None)
            half = length // 2
            right, bottom = left + half, top + half
            kids = [
                f(top, left, half),
                f(top, right, half),
                f(bottom, left, half),
                f(bottom, right, half)
            ]
            if all(k.isLeaf for k in kids) and len(set(k.val for k in kids)) == 1:
                return Node(kids[0].val, True, None, None, None, None)
            else:
                return Node('*', False, *kids)
        return f(0, 0, len(grid))

class Solution:
    def construct(self, g: List[List[int]]) -> 'Node':
        def f(x,y,l,e=[None]*4):
            if l==1:
                r = Node(g[x][y]==1,True,*e)
            else:
                h = l//2
                p = [f(x,y,h),f(x,y+h,h),f(x+h,y,h),f(x+h,y+h,h)]
                v = any(i.val for i in p)
                if all(i.isLeaf for i in p) and 1==len(set(i.val for i in p)):
                    r = Node(v,True,*e)
                else:
                    r = Node(v,False,*p)
            return r
        return g and f(0,0,len(g)) or None

class Solution:
    def construct(self, g: List[List[int]]) -> 'Node':
        return g and (f:=lambda x,y,l,e=[None]*4:Node(g[x][y]==1,True,*e) if l==1 else ((h:=l//2,p:=[f(x,y,h),f(x,y+h,h),f(x+h,y,h),f(x+h,y+h,h)],v:=any(i.val for i in p)) and (Node(v,True,*e) if all(i.isLeaf for i in p) and 1==len(set(i.val for i in p)) else Node(v,False,*p))))(0,0,len(g)) or None

# https://leetcode.com/problems/construct-quad-tree/discuss/160835/Python-2-lines

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        N = len(grid)
        return Node(val=bool(grid[0][0]), isLeaf=True, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None) \
            if all([all([i == grid[0][0] for i in j]) for j in grid]) \
            else Node(val=bool(grid[0][0]), isLeaf=False,
                      topLeft=self.construct([[grid[i][j] for j in range(N // 2)] for i in range(N // 2)]),
                      topRight=self.construct([[grid[i][j] for j in range(N // 2, N)] for i in range(N // 2)]),
                      bottomLeft=self.construct([[grid[i][j] for j in range(N // 2)] for i in range(N // 2, N)]),
                      bottomRight=self.construct([[grid[i][j] for j in range(N // 2, N)] for i in range(N // 2, N)])
                      )

class Solution:
    def construct(self, g: List[List[int]]) -> 'Node':
        return all(all(i==(s:=g[0][0]) for i in j) for j in g) and Node(bool(s),1,*([None]*4)) or Node(bool(s),(h:=len(g)//2)*0,*map(self.construct,[[r[k%2*h:(k%2+1)*h] for r in g[k//2*h:(k//2+1)*h]] for k in range(4)]))

# https://leetcode.com/problems/construct-quad-tree/discuss/3235773/Python-one-liner

class Solution:
    def construct(self, g: List[List[int]]) -> 'Node':
        return (not(s:=sum(sum(r) for r in g)) or s==(n:=len(g))*n) and Node(bool(s),1,*([None]*4)) or Node(bool(s),(h:=n//2)*0,*map(self.construct,[[r[k%2*h:(k%2+1)*h] for r in g[k//2*h:(k//2+1)*h]] for k in range(4)]))


test('''

427. Construct Quad Tree
Medium

589

791

Add to List

Share
Given a n * n matrix grid of 0's and 1's only. We want to represent the grid with a Quad-Tree.

Return the root of the Quad-Tree representing the grid.

Notice that you can assign the value of a node to True or False when isLeaf is False, and both are accepted in the answer.

A Quad-Tree is a tree data structure in which each internal node has exactly four children. Besides, each node has two attributes:

val: True if the node represents a grid of 1's or False if the node represents a grid of 0's.
isLeaf: True if the node is leaf node on the tree or False if the node has the four children.
class Node {
    public boolean val;
    public boolean isLeaf;
    public Node topLeft;
    public Node topRight;
    public Node bottomLeft;
    public Node bottomRight;
}
We can construct a Quad-Tree from a two-dimensional area using the following steps:

If the current grid has the same value (i.e all 1's or all 0's) set isLeaf True and set val to the value of the grid and set the four children to Null and stop.
If the current grid has different values, set isLeaf to False and set val to any value and divide the current grid into four sub-grids as shown in the photo.
Recurse for each of the children with the proper sub-grid.

If you want to know more about the Quad-Tree, you can refer to the wiki.

Quad-Tree format:

The output represents the serialized format of a Quad-Tree using level order traversal, where null signifies a path terminator where no node exists below.

It is very similar to the serialization of the binary tree. The only difference is that the node is represented as a list [isLeaf, val].

If the value of isLeaf or val is True we represent it as 1 in the list [isLeaf, val] and if the value of isLeaf or val is False we represent it as 0.

 

Example 1:


Input: grid = [[0,1],[1,0]]
Output: [[0,1],[1,0],[1,1],[1,1],[1,0]]
Explanation: The explanation of this example is shown below:
Notice that 0 represnts False and 1 represents True in the photo representing the Quad-Tree.

Example 2:

Input: grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
Output: [[0,1],[1,1],[0,1],[1,1],[1,0],null,null,null,null,[1,0],[1,0],[1,1],[1,1]]

Explanation: All values in the grid are not the same. We divide the grid into four sub-grids.
The topLeft, bottomLeft and bottomRight each has the same value.
The topRight have different values so we divide it into 4 sub-grids where each has the same value.
Explanation is shown in the photo below:

 

Constraints:

n == grid.length == grid[i].length
n == 2x where 0 <= x <= 6

''')


