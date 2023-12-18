from lc import *

class Solution:
    def maxProductDifference(self, n: List[int]) -> int:
        l1 = l2 = -inf
        s1 = s2 = inf
        for x in n:
            l1, l2 = max(l1, x), max(l2, min(x, l1))
            s1, s2 = min(s1, x), min(s2, max(x, s1))
        return l1*l2-s1*s2

class Solution:
    def maxProductDifference(self, n: List[int]) -> int:
        n.sort();return n[-1]*n[-2]-n[0]*n[1]

test('''
1913. Maximum Product Difference Between Two Pairs
Easy

866

47

Add to List

Share
The product difference between two pairs (a, b) and (c, d) is defined as (a * b) - (c * d).

For example, the product difference between (5, 6) and (2, 7) is (5 * 6) - (2 * 7) = 16.
Given an integer array nums, choose four distinct indices w, x, y, and z such that the product difference between pairs (nums[w], nums[x]) and (nums[y], nums[z]) is maximized.

Return the maximum such product difference.

 

Example 1:

Input: nums = [5,6,2,7,4]
Output: 34
Explanation: We can choose indices 1 and 3 for the first pair (6, 7) and indices 2 and 4 for the second pair (2, 4).
The product difference is (6 * 7) - (2 * 4) = 34.
Example 2:

Input: nums = [4,2,5,9,7,4,8]
Output: 64
Explanation: We can choose indices 3 and 6 for the first pair (9, 8) and indices 1 and 5 for the second pair (2, 4).
The product difference is (9 * 8) - (2 * 4) = 64.
 

Constraints:

4 <= nums.length <= 10^4
1 <= nums[i] <= 10^4
Accepted
107,174
Submissions
131,894
''')

