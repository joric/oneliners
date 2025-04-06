from lc import *

# https://leetcode.com/problems/largest-divisible-subset/discuss/684738/Python-Short-DP-with-O(n2)-explained-(update)

class Solution:
    def largestDivisibleSubset(self, nums):
        if len(nums) == 0:
            return []
        nums.sort()
        sol = [[num] for num in nums]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(sol[i]) < len(sol[j]) + 1:
                    sol[i] = sol[j] + [nums[i]]
        return max(sol, key=len)

# https://leetcode.com/problems/largest-divisible-subset/discuss/84002/4-lines-in-Python

class Solution:
    def largestDivisibleSubset(self, n: List[int]) -> List[int]:
        s = {-1:set()}
        for x in sorted(n):
            s[x] = max((s[d] for d in s if x%d == 0),key=len)|{x}
        return max(s.values(),key=len)

class Solution:
    def largestDivisibleSubset(self, n):
        return max(reduce(lambda s,x:setitem(s,x,max((s[d]for d in s if x%d<1),key=len)+[x])or s,sorted(n),{-1:[]}).values(),key=len)

class Solution:
    def largestDivisibleSubset(self, n: List[int]) -> List[int]:
        s={-1:set()};[setitem(s,x,max((s[d]for d in s if x%d<1),key=len)|{x})for x in sorted(n)];return max(s.values(),key=len)

class Solution:
    def largestDivisibleSubset(self, n):
        s={-1:[]};[setitem(s,x,max((s[d]for d in s if x%d<1),key=len)+[x])for x in sorted(n)];return max(s.values(),key=len)

# POTD 2025-04-06

class Solution:
    def largestDivisibleSubset(self, n: List[int]) -> List[int]:
        s={-1:[]};[setitem(s,x,max((s[d]for d in s if x%d<1),key=len)+[x])for x in sorted(n)];return[*max(s.values(),key=len)]

test('''
368. Largest Divisible Subset
Medium

5267

220

Add to List

Share
Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

answer[i] % answer[j] == 0, or
answer[j] % answer[i] == 0
If there are multiple solutions, return any of them.

 

Example 1:

Input: nums = [1,2,3]
Output: [1,2]
Explanation: [1,3] is also accepted.
Example 2:

Input: nums = [1,2,4,8]
Output: [1,2,4,8]
 

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 2 * 10^9
All the integers in nums are unique.
Accepted
220,330
Submissions
512,530
''', check=lambda r,e,n:(s:={-1:[]},[setitem(s,x,max((s[d]for d in s if x%d<1),key=len)+[x])for x in sorted(n)],l:=len(max(s.values(),key=len)))and len(r)==l and r in s.values()
)