from lc import *

# https://leetcode.com/problems/maximum-alternating-sum-of-squares/solutions/8567899/one-line-solution-by-mikposp-jjae/?envType=daily-question&envId=2026-10-13

class Solution:
    def maxAlternatingSum(self, a: List[int]) -> int:
        return sum(s:=sorted(x*x for x in a))-2*sum(s[:len(a)>>1])

class Solution:
    def maxAlternatingSum(self, a: List[int]) -> int:
        return sum(s:=sorted(map(mul,a,a)))-2*sum(s[:len(a)//2])

test('''
3727. Maximum Alternating Sum of Squares
Medium
Topics
premium lock icon
Companies
Hint
You are given an integer array nums. You may rearrange the elements in any order.

The alternating score of an array arr is defined as:

score = arr[0]2 - arr[1]2 + arr[2]2 - arr[3]2 + ...
Return an integer denoting the maximum possible alternating score of nums after rearranging its elements.

 

Example 1:

Input: nums = [1,2,3]

Output: 12

Explanation:

A possible rearrangement for nums is [2,1,3], which gives the maximum alternating score among all possible rearrangements.

The alternating score is calculated as:

score = 22 - 12 + 32 = 4 - 1 + 9 = 12

Example 2:

Input: nums = [1,-1,2,-2,3,-3]

Output: 16

Explanation:

A possible rearrangement for nums is [-3,-1,-2,1,3,2], which gives the maximum alternating score among all possible rearrangements.

The alternating score is calculated as:

score = (-3)2 - (-1)2 + (-2)2 - (1)2 + (3)2 - (2)2 = 9 - 1 + 4 - 1 + 9 - 4 = 16

 

Constraints:

1 <= nums.length <= 105
-4 * 104 <= nums[i] <= 4 * 104
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
35,906/58.4K
Acceptance Rate
61.4%
Topics
Senior
Array
Greedy
Sorting
Weekly Contest 473
icon
Companies
Hint 1
The score uses squares of values. The original signs of nums don't affect the squared terms.
Hint 2
In the alternating sum, even indices contribute positively and odd indices negatively.
''')
