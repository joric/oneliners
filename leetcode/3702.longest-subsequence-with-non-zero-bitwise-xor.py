from lc import *

# https://leetcode.com/problems/longest-subsequence-with-non-zero-bitwise-xor/solutions/8450727/one-line-solution-by-mikposp-yp17/?envType=daily-question&envId=2026-08-15

class Solution:
    def longestSubsequence(self, a: List[int]) -> int:
        return any(a) and len(a)-(reduce(xor,a)==0) or 0

class Solution:
    def longestSubsequence(self, a: List[int]) -> int:
        return any(a)*(len(a)-(reduce(xor,a)==0))

test('''
3702. Longest Subsequence With Non-Zero Bitwise XOR
Medium
Topics
premium lock icon
Companies
Hint
You are given an integer array nums.

Return the length of the longest subsequence in nums whose bitwise XOR is non-zero. If no such subsequence exists, return 0.

 

Example 1:

Input: nums = [1,2,3]

Output: 2

Explanation:

One longest subsequence is [2, 3]. The bitwise XOR is computed as 2 XOR 3 = 1, which is non-zero.

Example 2:

Input: nums = [2,3,4]

Output: 3

Explanation:

The longest subsequence is [2, 3, 4]. The bitwise XOR is computed as 2 XOR 3 XOR 4 = 5, which is non-zero.

 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 109
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
33,335/88.5K
Acceptance Rate
37.7%
Topics
Senior
Array
Bit Manipulation
Weekly Contest 470
icon
Companies
Hint 1
What happens if you take the entire array?
Hint 2
If the XOR of the entire array is 0, can removing one element help?
Hint 3
What if all elements are 0?
''')
