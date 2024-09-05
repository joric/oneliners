from lc import *

# https://leetcode.com/problems/count-nice-pairs-in-an-array/discuss/1937102/Python-One-line-Solution

class Solution:
    def countNicePairs(self, n: List[int]) -> int:
        return sum(comb(x,2)for x in Counter(x-int(str(x)[::-1])for x in n).values())%(10**9+7)

class Solution:
    def countNicePairs(self, n: List[int]) -> int:
        c=Counter(x-int(str(x)[::-1])for x in n);return sum(comb(c[x],2)for x in c)%(10**9+7)

test('''
1814. Count Nice Pairs in an Array
Medium

854

34

Add to List

Share
You are given an array nums that consists of non-negative integers. Let us define rev(x) as the reverse of the non-negative integer x. For example, rev(123) = 321, and rev(120) = 21. A pair of indices (i, j) is nice if it satisfies all of the following conditions:

0 <= i < j < nums.length
nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
Return the number of nice pairs of indices. Since that number can be too large, return it modulo 109 + 7.

 

Example 1:

Input: nums = [42,11,1,97]
Output: 2
Explanation: The two pairs are:
 - (0,3) : 42 + rev(97) = 42 + 79 = 121, 97 + rev(42) = 97 + 24 = 121.
 - (1,2) : 11 + rev(1) = 11 + 1 = 12, 1 + rev(11) = 1 + 11 = 12.
Example 2:

Input: nums = [13,10,35,24,76]
Output: 4
 

Constraints:

1 <= nums.length <= 10^5
0 <= nums[i] <= 10^9
Accepted
28,799
Submissions
68,805
''')