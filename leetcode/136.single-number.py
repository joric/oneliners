from lc import *

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return 2*sum(set(nums))-sum(nums)

class Solution:
    def singleNumber(self, n: List[int]) -> int:
        return 2*sum({*n})-sum(n)

class Solution:
    def singleNumber(self, n: List[int]) -> int:
        return reduce(xor,n)

test('''
136. Single Number
Easy

15688

651

Add to List

Share
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
 

Constraints:

1 <= nums.length <= 3 * 10^4
-3 * 104 <= nums[i] <= 3 * 10^4
Each element in the array appears twice except for one element which appears only once.
Accepted
2,499,123
Submissions
3,473,558
''')
