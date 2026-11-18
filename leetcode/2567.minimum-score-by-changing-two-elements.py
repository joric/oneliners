from lc import *

# https://leetcode.com/problems/minimum-score-by-changing-two-elements/solutions/3202036/python-2-line-solution-w-explanation-by-8mz2y/?envType=daily-question&envId=2026-11-19

class Solution:
    def minimizeSum(self, a: List[int]) -> int:
        a.sort();return min(a[-1]-a[2],a[-2]-a[1],a[-3]-a[0])

class Solution:
    def minimizeSum(self, a: List[int]) -> int:
        a.sort();return min(map(int.__sub__,a[-3:],a))

test('''
2567. Minimum Score by Changing Two Elements
Medium
Topics
premium lock icon
Companies
Hint
You are given an integer array nums.

The low score of nums is the minimum absolute difference between any two integers.
The high score of nums is the maximum absolute difference between any two integers.
The score of nums is the sum of the high and low scores.
Return the minimum score after changing two elements of nums.

 

Example 1:

Input: nums = [1,4,7,8,5]

Output: 3

Explanation:

Change nums[0] and nums[1] to be 6 so that nums becomes [6,6,7,8,5].
The low score is the minimum absolute difference: |6 - 6| = 0.
The high score is the maximum absolute difference: |8 - 5| = 3.
The sum of high and low score is 3.
Example 2:

Input: nums = [1,4,3]

Output: 0

Explanation:

Change nums[1] and nums[2] to 1 so that nums becomes [1,1,1].
The sum of maximum absolute difference and minimum absolute difference is 0.
 

Constraints:

3 <= nums.length <= 105
1 <= nums[i] <= 109
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
24,354/48.2K
Acceptance Rate
50.5%
Topics
Senior
Array
Greedy
Sorting
Biweekly Contest 98
icon
Companies
Hint 1
Changing the minimum or maximum values will only minimize the score.
Hint 2
Think about what all possible pairs of minimum and maximum values can be changed to form the minimum score.
''')
