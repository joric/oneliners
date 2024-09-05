from lc import *

# https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/discuss/2729720/Python-one-line-O(n)-time-(not-brute-force)

class Solution:
    def findMaxK(self, n: List[int]) -> int:
        return max((filter(n.__contains__,map(neg,n))),default=-1)

class Solution:
    def findMaxK(self, n: List[int]) -> int:
        s=set(n);return max([-1]+[x for x in s if-x in s])

class Solution:
    def findMaxK(self, n: List[int]) -> int:
        return max([-1]+[x for x in n if-x in n])

class Solution:
    def findMaxK(self, n: List[int]) -> int:
        return max({*n}&{*map(neg,n)}|{-1})

class Solution:
    def findMaxK(self, n: List[int]) -> int:
        return-min({1,*n}&{1,*map(neg,n)})

test('''
2441. Largest Positive Integer That Exists With Its Negative
Easy

517

14

Add to List

Share
Given an integer array nums that does not contain any zeros, find the largest positive integer k such that -k also exists in the array.

Return the positive integer k. If there is no such integer, return -1.

 

Example 1:

Input: nums = [-1,2,-3,3]
Output: 3
Explanation: 3 is the only valid k we can find in the array.
Example 2:

Input: nums = [-1,10,6,7,-7,1]
Output: 7
Explanation: Both 1 and 7 have their corresponding negative values in the array. 7 has a larger value.
Example 3:

Input: nums = [-10,8,6,7,-2,-3]
Output: -1
Explanation: There is no a single valid k, we return -1.
 

Constraints:

1 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
nums[i] != 0
Accepted
61,590
Submissions
90,145
''')
