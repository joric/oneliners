from lc import *

# https://leetcode.com/problems/maximum-width-ramp/discuss/5660313/One-Line-Solution

class Solution:
    def maxWidthRamp(self, a: List[int]) -> int:
        a = [i for _,i in sorted((v,i) for i,v in enumerate(a))]
        b = accumulate(a, min)
        return max(map(sub, a, b))

# updated 2024-10-10 (POTD)

class Solution:
    def maxWidthRamp(self, a: List[int]) -> int:
        return max(map(sub,a:=[i for _,i in sorted((v,i)for i,v in enumerate(a))],accumulate(a,min)))

test('''
962. Maximum Width Ramp
Medium

1707

51

Add to List

Share
A ramp in an integer array nums is a pair (i, j) for which i < j and nums[i] <= nums[j]. The width of such a ramp is j - i.

Given an integer array nums, return the maximum width of a ramp in nums. If there is no ramp in nums, return 0.

 

Example 1:

Input: nums = [6,0,8,2,1,5]
Output: 4
Explanation: The maximum width ramp is achieved at (i, j) = (1, 5): nums[1] = 0 and nums[5] = 5.
Example 2:

Input: nums = [9,8,1,0,1,9,4,0,4,1]
Output: 7
Explanation: The maximum width ramp is achieved at (i, j) = (2, 9): nums[2] = 1 and nums[9] = 1.
 

Constraints:

2 <= nums.length <= 5 * 104
0 <= nums[i] <= 5 * 104
Accepted
51,058
Submissions
100,417
''')
