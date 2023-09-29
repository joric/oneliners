from lc import *

class Solution:
    def isMonotonic(self, n: List[int]) -> bool:
        increasing = decreasing = True
        for a,b in pairwise(n):
            if b>a:
                decreasing = False
            elif b<a:
                increasing = False
            if not increasing and not decreasing:
                return False
        return True

class Solution:
    def isMonotonic(self, n: List[int]) -> bool:
        return all(a<=b for a,b in pairwise(n))or all(a>=b for a,b in pairwise(n))

class Solution:
    def isMonotonic(self, n: List[int]) -> bool:
        return not{1,-1}.issubset({(a>b)-(a<b)for a,b in pairwise(n)})

class Solution:
    def isMonotonic(self, n: List[int]) -> bool:
        return not{(a>b)-(a<b)for a,b in pairwise(n)}>={1,-1}

class Solution:
    def isMonotonic(self, n: List[int]) -> bool:
        return any(n==sorted(n,reverse=r)for r in(0,1))

class Solution:
    def isMonotonic(self, n: List[int]) -> bool:
        return n==(t:=sorted(n))or n==t[::-1]

# https://leetcode.com/problems/monotonic-array/discuss/165960/Python-Solution-Easy-to-Understand/216811

class Solution:
    def isMonotonic(self, n: List[int]) -> bool:
        return sorted(n)in(n,n[::-1])

test('''
896. Monotonic Array
Easy

2489

76

Add to List

Share
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, or false otherwise.

 

Example 1:

Input: nums = [1,2,2,3]
Output: true
Example 2:

Input: nums = [6,5,4,4]
Output: true
Example 3:

Input: nums = [1,3,2]
Output: false
 

Constraints:

1 <= nums.length <= 10^5
-10^5 <= nums[i] <= 10^5
''')

