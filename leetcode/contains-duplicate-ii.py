from lc import *

class Solution1:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        m = {}
        for i,x in enumerate(nums):
            if x in m and abs(m[x]-i) <= k:
                return True
            m[x] = i
        return False

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        return (f:=lambda i,m:i<len(nums) and (nums[i] in m and abs(m[nums[i]]-i)<=k or setitem(m,nums[i], i) or f(i+1, m)))(0,{})

test('''
219. Contains Duplicate II
Easy

Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false

Constraints:

1 <= nums.length <= 10**5
-10**9 <= nums[i] <= 10**9
0 <= k <= 10**5

''')
