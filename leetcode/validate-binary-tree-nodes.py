from lc import *

# editorial (DFS)

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        def find_root():
            children = set(leftChild) | set(rightChild)
            for i in range(n):
                if i not in children:
                    return i
            return -1
        root = find_root()
        if root == -1:
            return False
        seen = {root}
        stack = [root]
        while stack:
            node = stack.pop()
            for child in [leftChild[node], rightChild[node]]:
                if child != -1:
                    if child in seen:
                        return False
                    stack.append(child)
                    seen.add(child)
        return len(seen) == n

# editorial (BFS)

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        def find_root():
            children = set(leftChild) | set(rightChild)
            for i in range(n):
                if i not in children:
                    return i
            return -1
        root = find_root()
        if root == -1:
            return False
        seen = {root}
        queue = deque([root])
        while queue:
            node = queue.popleft()
            for child in [leftChild[node], rightChild[node]]:
                if child != -1:
                    if child in seen:
                        return False
                    queue.append(child)
                    seen.add(child)
        return len(seen) == n

# editorial (union find)

class UnionFind:
    def __init__(self, n):
        self.components = n
        self.parents = list(range(n))
    def union(self, parent, child):
        parent_parent = self.find(parent)
        child_parent = self.find(child)
        if child_parent != child or parent_parent == child_parent:
            return False
        self.components -= 1
        self.parents[child_parent] = parent_parent
        return True
    def find(self, node):
        if self.parents[node] != node:
            self.parents[node] = self.find(self.parents[node])
        return self.parents[node]

class Solution:
    def validateBinaryTreeNodes(self, n: int, l: List[int], r: List[int]) -> bool:
        t = UnionFind(n)
        for u in range(n):
            for v in (l[u], r[u]):
                if v == -1:
                    continue
                if not t.union(u,v):
                    return False
        return t.components == 1

# https://leetcode.com/problems/validate-binary-tree-nodes/discuss/845610/python-10-lines-with-only-if-else

class Solution:
    def validateBinaryTreeNodes(self, n: int, l: List[int], r: List[int]) -> bool:
        v,p = set([0]), set([0])
        for i in range(len(l)):
            if (l[i]!=-1 and l[i]==r[i] or l[i]!=-1 and i in v and l[i] in v or r[i]!=-1 and i in v and r[i] in v or r[i]==i or l[i]==i):
                return False
            (i not in v and p.add(i),l[i]in p and p.remove(l[i]),r[i]in p and p.remove(r[i]),l[i]!=-1 and v.add(l[i]),r[i]!=-1 and v.add(r[i]))
        return len(p) == 1

class Solution:
    def validateBinaryTreeNodes(self, n: int, l: List[int], r: List[int]) -> bool:
        v,p=set([0]),set([0]);return next((0 for i in range(len(l))if (l[i]!=-1 and l[i]==r[i] or l[i]!=-1 and i in v and l[i] in v or r[i]!=-1 and i in v and r[i] in v or r[i]==i or l[i]==i)or not(i not in v and p.add(i),l[i]in p and p.remove(l[i]),r[i]in p and p.remove(r[i]),l[i]!=-1 and v.add(l[i]),r[i]!=-1 and v.add(r[i]))),1)==len(p)

# TODO: try unicode find? https://leetcode.com/problems/redundant-connection/discuss/108002/Unicode-Find-(5-short-lines)

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

