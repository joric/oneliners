from lc import *

# https://leetcode.com/problems/find-pivot-index/discuss/4064483/Using-two-accumulate-calls-in-Python

class Solution:
    def pivotIndex(self, n: List[int]) -> int:
        a=accumulate;return next((i for i,(a,b)in enumerate(zip(a(n),[*a(n[::-1])][::-1]))if a==b),-1)

# https://leetcode.com/problems/find-pivot-index/discuss/2406148/Python-or-One-Liner-or-Easy-to-Understand

class Solution:
    def pivotIndex(self, n: List[int]) -> int:
        return next((i for i in range(len(n))if sum(n[:i])==sum(n[i+1:])),-1)



test('''
724. Find Pivot Index
Easy

8030

814

Add to List

Share
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

 

Example 1:

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11
Example 2:

Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.
Example 3:

Input: nums = [2,1,-1]
Output: 0
Explanation:
The pivot index is 0.
Left sum = 0 (no elements to the left of index 0)
Right sum = nums[1] + nums[2] = 1 + -1 = 0
 

Constraints:

1 <= nums.length <= 104
-1000 <= nums[i] <= 1000
 

Note: This question is the same as 1991: https://leetcode.com/problems/find-the-middle-index-in-array/

Accepted
995,456
Submissions
1,755,367
''')

