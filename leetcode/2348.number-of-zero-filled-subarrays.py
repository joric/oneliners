from lc import *

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        r=c=0
        for x in nums:
            if x:
                c = 0
            else:
                c += 1
            r += c
        return r

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        return sum(accumulate(nums,lambda c,x:0 if x else c+1,initial=0))

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        return sum(c:=0 if x else c+1 for x in[1]+nums)

class Solution:
    def zeroFilledSubarray(self, a: List[int]) -> int:
        c=0;return sum(c:=-~c*(x==0)for x in a)

test('''
2348. Number of Zero-Filled Subarrays
Medium

427

13

Add to List

Share
Given an integer array nums, return the number of subarrays filled with 0.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,3,0,0,2,0,0,4]
Output: 6
Explanation: 
There are 4 occurrences of [0] as a subarray.
There are 2 occurrences of [0,0] as a subarray.
There is no occurrence of a subarray with a size more than 2 filled with 0. Therefore, we return 6.
Example 2:

Input: nums = [0,0,0,2,0,0]
Output: 9
Explanation:
There are 5 occurrences of [0] as a subarray.
There are 3 occurrences of [0,0] as a subarray.
There is 1 occurrence of [0,0,0] as a subarray.
There is no occurrence of a subarray with a size more than 3 filled with 0. Therefore, we return 9.
Example 3:

Input: nums = [2,10,2019]
Output: 0
Explanation: There is no subarray filled with 0. Therefore, we return 0.

Other examples:

Input: nums = [13,17,-8,-18,1,11,-19,1,-15,-7,2,-4]
Output: 0

Constraints:

1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9

Accepted
28,514
Submissions
49,369
''')