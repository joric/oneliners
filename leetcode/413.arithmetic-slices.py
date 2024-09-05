from lc import *

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        total_sequences = seq_count = 0
        for i in range(2, len(nums)):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                seq_count += 1
                total_sequences += seq_count
            else:
                seq_count = 0
        return total_sequences 

class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        return reduce(lambda a,i:((0,a[1]),(a[0]+1,a[0]+a[1]+1))[A[i]-A[i-1]==A[i-1]-A[i-2]],range(2,len(A)),(0,0))[1]

test('''
413. Arithmetic Slices
Medium

4335

264

Add to List

Share
An integer array is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic sequences.
Given an integer array nums, return the number of arithmetic subarrays of nums.

A subarray is a contiguous subsequence of the array.

 

Example 1:

Input: nums = [1,2,3,4]
Output: 3
Explanation: We have 3 arithmetic slices in nums: [1, 2, 3], [2, 3, 4] and [1,2,3,4] itself.
Example 2:

Input: nums = [1]
Output: 0
 

Constraints:

1 <= nums.length <= 5000
-1000 <= nums[i] <= 1000
''')