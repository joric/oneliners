from lc import *

# https://leetcode.com/problems/minimum-distance-to-the-target-element/solutions/4044167/one-line-solution-by-xxxxkav-ram7/?envType=daily-question&envId=2026-04-13

class Solution:
    def getMinDistance(self, a: List[int], t: int, s: int) -> int:
        return min(abs(i-s)for i,x in enumerate(a)if x==t)

test('''
1848. Minimum Distance to the Target Element
Easy
Topics
premium lock icon
Companies
Hint
Given an integer array nums (0-indexed) and two integers target and start, find an index i such that nums[i] == target and abs(i - start) is minimized. Note that abs(x) is the absolute value of x.

Return abs(i - start).

It is guaranteed that target exists in nums.

 

Example 1:

Input: nums = [1,2,3,4,5], target = 5, start = 3
Output: 1
Explanation: nums[4] = 5 is the only value equal to target, so the answer is abs(4 - 3) = 1.
Example 2:

Input: nums = [1], target = 1, start = 0
Output: 0
Explanation: nums[0] = 1 is the only value equal to target, so the answer is abs(0 - 0) = 0.
Example 3:

Input: nums = [1,1,1,1,1,1,1,1,1,1], target = 1, start = 0
Output: 0
Explanation: Every value of nums is 1, but nums[0] minimizes abs(i - start), which is abs(0 - 0) = 0.
 

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 104
0 <= start < nums.length
target is in nums.
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
61,250/112.7K
Acceptance Rate
54.3%
Topics
Mid Level
Array
Weekly Contest 239
icon
Companies
Hint 1
Loop in both directions until you find the target element.
Hint 2
For each index i such that nums[i] == target calculate abs(i - start).
''')
