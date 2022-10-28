from lc import *

class Solution1:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] + [0]*(n-1)
        for i in range(1, n):
            res[i] = res[i-1] * nums[i-1]
        t = 1;
        for i in reversed(range(n)):
            res[i] *= t
            t *= nums[i]
        return res

class Solution2:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        return [l*r for l, r in zip(chain([1], accumulate(nums,mul)),islice(chain(reversed(list(accumulate(reversed(nums),mul))), [1]), 1, None))]

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        return list(starmap(mul, zip([1]+list(accumulate(nums[:-1], mul)),list(accumulate(nums[::-1][:-1],mul))[::-1]+[1])))

test('''
238. Product of Array Except Self
Medium

15127

860

Add to List

Share
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 
''')
