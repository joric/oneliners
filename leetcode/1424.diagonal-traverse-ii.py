from lc import *

# https://leetcode.com/problems/diagonal-traverse-ii/discuss/597794/Python-One-pass

class Solution:
    def findDiagonalOrder(self, n: List[List[int]]) -> List[int]:
        res = []
        for i, r in enumerate(n):
            for j, a in enumerate(r):
                if len(res) <= i + j:
                    res.append([])
                res[i + j].append(a)
        return [a for r in res for a in reversed(r)]

class Solution:
    def findDiagonalOrder(self, n: List[List[int]]) -> List[int]:
        d=defaultdict(list);[d[i+j].append(a)for i,r in enumerate(n)for j,a in enumerate(r)];return chain(*map(reversed,d.values()))

# https://leetcode.com/problems/diagonal-traverse-ii/discuss/647533/One-line-Python

class Solution:
    def findDiagonalOrder(self, n: List[List[int]]) -> List[int]:
        return[x[2]for x in sorted((i+j,j,c)for i,r in enumerate(n)for j,c in enumerate(r))]

class Solution:
    def findDiagonalOrder(self, n: List[List[int]]) -> List[int]:
        return map(list.pop,sorted([i+j,j,c]for i,r in enumerate(n)for j,c in enumerate(r)))

class Solution:
    def findDiagonalOrder(self, n: List[List[int]]) -> List[int]:
        e=enumerate;return map(list.pop,sorted([i+j,j,c]for i,r in e(n)for j,c in e(r)))

test('''
1424. Diagonal Traverse II
Medium

1495

120

Add to List

Share
Given a 2D integer array nums, return all elements of nums in diagonal order as shown in the below images.

 

Example 1:


Input: nums = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,4,2,7,5,3,8,6,9]
Example 2:


Input: nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
Output: [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]
 

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i].length <= 10^5
1 <= sum(nums[i].length) <= 10^5
1 <= nums[i][j] <= 10^5
Accepted
76,028
Submissions
141,667
''')