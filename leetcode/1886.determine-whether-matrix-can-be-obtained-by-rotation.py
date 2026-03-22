from lc import *

# https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/solutions/4050979/one-line-solution-by-xxxxkav-ogl9/?envType=daily-question&envId=2026-03-22

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        return all(map(lambda a, b: eq(tuple(a), b), mat, zip(*reversed(target)))) | all(map(lambda a, b: eq(a, tuple(b)), zip(*reversed(mat)), target)) | all(map(lambda a, b: eq(a, list(reversed(b))), mat, reversed(target))) | all(map(eq, mat, target))

# https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/solutions/1563208/python-numpy-solution-by-tovam-4963/?envType=daily-question&envId=2026-03-22

import numpy as np

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for i in range(4):
            if np.allclose(mat, target):
                return True
            mat = np.rot90(mat)
        return False

class Solution:
    def findRotation(self, m: List[List[int]], t: List[List[int]]) -> bool:
        n=__import__('numpy');return any(n.allclose(n.rot90(m,k),t)for k in range(4))

# https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/solutions/1257918/python-3-five-one-liners-by-l1ne-8m1j/?envType=daily-question&envId=2026-03-22


class Solution:
  def findRotation(self, A: List[List[int]], B: List[List[int]]) -> bool:
    return len(set.intersection(*({k for k,x in enumerate((A[i][j], A[j][-i-1], A[-i-1][-j-1], A[-j-1][i])) if x==B[i][j]} for i in range(len(A)) for j in range(len(A))))) > 0

class Solution:
  def findRotation(self, A: List[List[int]], B: List[List[int]]) -> bool:
    return tuple(x for r in B for x in r) in zip(*([A[i][j], A[j][-i-1], A[-i-1][-j-1], A[-j-1][i]] for i in range(len(A)) for j in range(len(A))))

class Solution:
  def findRotation(self, A: List[List[int]], B: List[List[int]]) -> bool:
    return B in (A, [*map(list, zip(*A[::-1]))], [x[::-1] for x in A][::-1], [*map(list, zip(*A))][::-1])

class Solution:
  def findRotation(self, A: List[List[int]], B: List[List[int]]) -> bool:
    return B in accumulate([A] * 4, lambda m,_: [*map(list, zip(*m[::-1]))])

# POTD 2026-03-22

class Solution:
    def findRotation(self, m: List[List[int]], t: List[List[int]]) -> bool:
        return t in accumulate([m]*4,lambda x,_:[*map(list,zip(*x[::-1]))])

# https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/solutions/3069104/python-one-liner-by-aaron1101-1zb4/?envType=daily-question&envId=2026-03-22

class Solution:
    def findRotation(self, m: List[List[int]], t: List[List[int]]) -> bool:
        return any(t==(m:=[*map(list,zip(*m[::-1]))])for _ in range(4))

class Solution:
    def findRotation(self, m: List[List[int]], t: List[List[int]]) -> bool:
        return any(t==(m:=[list(t)for t in zip(*m[::-1])])for _ in m*4)

class Solution:
    def findRotation(self, m: List[List[int]], t: List[List[int]]) -> bool:
        return any(t==(m:=[*map(list,zip(*m[::-1]))])for _ in m*4)

test('''
1886. Determine Whether Matrix Can Be Obtained By Rotation
Easy
Topics
premium lock icon
Companies
Hint
Given two n x n binary matrices mat and target, return true if it is possible to make mat equal to target by rotating mat in 90-degree increments, or false otherwise.

 

Example 1:


Input: mat = [[0,1],[1,0]], target = [[1,0],[0,1]]
Output: true
Explanation: We can rotate mat 90 degrees clockwise to make mat equal target.
Example 2:


Input: mat = [[0,1],[1,1]], target = [[1,0],[0,1]]
Output: false
Explanation: It is impossible to make mat equal to target by rotating mat.
Example 3:


Input: mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]]
Output: true
Explanation: We can rotate mat 90 degrees clockwise two times to make mat equal target.
 

Constraints:

n == mat.length == target.length
n == mat[i].length == target[i].length
1 <= n <= 10
mat[i][j] and target[i][j] are either 0 or 1.
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
97,780/164.8K
Acceptance Rate
59.3%
Topics
Mid Level
Array
Matrix
Weekly Contest 244
icon
Companies
Hint 1
What is the maximum number of rotations you have to check?
Hint 2
Is there a formula you can use to rotate a matrix 90 degrees?
Similar Questions
Rotate Image
Medium
''')
