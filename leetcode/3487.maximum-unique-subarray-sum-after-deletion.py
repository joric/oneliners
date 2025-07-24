from lc import *

# https://leetcode.com/problems/maximum-unique-subarray-sum-after-deletion/solutions/6998581/one-line-solution/

class Solution:
    def maxSum(self, a: List[int]) -> int:
        return sum(x*(x>0)for x in{*a})or max(a)

test('''
3487. Maximum Unique Subarray Sum After Deletion
Solved
Easy
Topics
premium lock icon
Companies
Hint
You are given an integer array nums.

You are allowed to delete any number of elements from nums without making it empty. After performing the deletions, select a subarray of nums such that:

All elements in the subarray are unique.
The sum of the elements in the subarray is maximized.
Return the maximum sum of such a subarray.

 

Example 1:

Input: nums = [1,2,3,4,5]

Output: 15

Explanation:

Select the entire array without deleting any element to obtain the maximum sum.

Example 2:

Input: nums = [1,1,0,1,1]

Output: 1

Explanation:

Delete the element nums[0] == 1, nums[1] == 1, nums[2] == 0, and nums[3] == 1. Select the entire array [1] to obtain the maximum sum.

Example 3:

Input: nums = [1,2,-1,-2,1,0,-1]

Output: 3

Explanation:

Delete the elements nums[2] == -1 and nums[3] == -2, and select the subarray [2, 1] from [1, 2, 1, 0, -1] to obtain the maximum sum.

 

Constraints:

1 <= nums.length <= 100
-100 <= nums[i] <= 100
Seen this question in a real interview before?
1/5
Yes
No
Accepted
31,883/114.7K
Acceptance Rate
27.8%
Topics
Array
Hash Table
Greedy
Weekly Contest 441
icon
Companies
Hint 1
If the maximum element in the array is less than zero, the answer is the maximum element.
Hint 2
Otherwise, the answer is the sum of all unique values that are greater than or equal to zero.
Similar Questions
Maximum Subarray Sum with One Deletion
Medium
''')
