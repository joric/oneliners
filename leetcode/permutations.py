from lc import *

# https://leetcode.com/problems/permutations/discuss/18241/One-Liners-in-Python

# Solution 1: Recursive, take any number as first
# Take any number as the first number and append any permutation of the other numbers.
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return [[n] + p
                for i, n in enumerate(nums)
                for p in self.permute(nums[:i] + nums[i+1:])] or [[]]
  
# Solution 2: Recursive, insert first number anywhere
# Insert the first number anywhere in any permutation of the remaining numbers.
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return nums and [p[:i] + [nums[0]] + p[i:]
                         for p in self.permute(nums[1:])
                         for i in range(len(nums))] or [[]]

# Solution 3: Reduce, insert next number anywhere
# Use reduce to insert the next number anywhere in the already built permutations.
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return reduce(lambda P, n: [p[:i] + [n] + p[i:]
                                    for p in P for i in range(len(p)+1)],
                                    nums, [[]])

# Solution 4: Using the library
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return permutations(nums)

# minus-two-liner:
class Solution: permute=permutations

# Heap's permutation scheme with 2 swaps, see https://en.wikipedia.org/wiki/Heap%27s_algorithm
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def h(j):
            if j==len(nums)-1:
                res.append(nums[:])
            for i in range(j, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                h(j+1)
                nums[i], nums[j] = nums[j], nums[i]
        h(0)
        return res

class Solution:
    def permute(self, a: List[int]) -> List[List[int]]:
        return (
            r:=[],
            s:=lambda a,x,y:exec('a[x],a[y]=a[y],a[x]'),
            h:=lambda j=0: j==len(a)-1 and r.append(a[:]) or any(s(a,i,j) or h(j+1) or s(a,i,j) for i in range(j,len(a)))
        ) and h() or r

class Solution:
    def permute(self, a: List[int]) -> List[List[int]]:
        return (
            r:=[],
            s:=lambda a,x,y:(t:=a[x],a.__setitem__(x,a[y]),a.__setitem__(y,t))[1],
            h:=lambda j=0: j==len(a)-1 and r.append(a[:]) or any(s(a,i,j) or h(j+1) or s(a,i,j) for i in range(j,len(a)))
        ) and h() or r

test('''

46. Permutations
Medium

13684

225

Add to List

Share
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
 

Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.

'''
, check=lambda res,exp,s:(u:=lambda v: sorted(list(map(sorted,v))))(res)==u(exp)
)
