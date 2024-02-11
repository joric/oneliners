from lc import *

# https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, n: List[int]) -> List[List[int]]:
        r = [[]]
        for x in n:
            r += [v+[x]for v in r]
        return r

class Solution:
    def subsets(self, n: List[int]) -> List[List[int]]:
        r = []
        for i in range(len(n)+1): 
            for c in combinations(n,i):
                r.append(list(c))
        return r

class Solution:
    def subsets(self, r: List[int]) -> List[List[int]]:
        return[c for k in range(len(r)+1)for c in combinations(r,k)]

test('''
78. Subsets
Medium

16464

255

Add to List

Share
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
Accepted
1,729,344
Submissions
2,247,188
''', check=lambda r,e,*args: sorted(r)==sorted(e))
