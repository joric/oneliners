from lc import *

# https://leetcode.com/problems/maximum-product-of-three-numbers/
# same as https://binarysearch.com/problems/Max-Product-of-Three-Numbers

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        l1 = l2 = l3 = -inf
        s1 = s2 = inf
        for n in nums:
            l1, l2, l3 = max(l1, n), max(l2, min(n, l1)), max(l3, min(l2, n))
            s1, s2 = min(s1, n), min(s2, max(n, s1))
        return max(l1 * l2 * l3, s1 * s2 * l1)

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        return max((v:=sorted(nums))[-1]*v[-2]*v[-3], v[0]*v[1]*v[-1])

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        return max(prod((v:=sorted(nums))[-3:]), v[0]*v[1]*v[-1])

test('''

628. Maximum Product of Three Numbers
Easy

3276

563

Add to List

Share
Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

 

Example 1:

Input: nums = [1,2,3]
Output: 6
Example 2:

Input: nums = [1,2,3,4]
Output: 24
Example 3:

Input: nums = [-1,-2,-3]
Output: -6
 

Constraints:

3 <= nums.length <= 10^4
-1000 <= nums[i] <= 1000

''')
