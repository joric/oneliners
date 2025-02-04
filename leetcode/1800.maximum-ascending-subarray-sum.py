from lc import *

# https://leetcode.com/problems/maximum-ascending-subarray-sum/solutions/1119686/python3-line-sweep/?envType=daily-question&envId=2025-02-04

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans = 0
        for i, x in enumerate(nums): 
            if not i or nums[i-1] >= nums[i]:
                val = 0
            val += nums[i]
            ans = max(ans, val)
        return ans 

# https://leetcode.com/problems/maximum-ascending-subarray-sum/solutions/6370129/easy-python-code-o-n-time-and-o-1-space-beats-everyone/?envType=daily-question&envId=2025-02-04

class Solution:
    def maxAscendingSum(self, n: List[int]) -> int:
        p = -inf
        m = c = 0
        for x in n:
            c = c+x if x > p else x
            p = x
            m = max(m,c)
        return m

class Solution:
    def maxAscendingSum(self, n: List[int]) -> int:
        return max(c:=c+x if p<x else x for p,x in zip([inf]+n,n))

class Solution:
    def maxAscendingSum(self, n: List[int]) -> int:
        c=0;return max(c:=(x,c+x)[p<x]for p,x in zip([-inf]+n,n))

class Solution:
    def maxAscendingSum(self, n: List[int]) -> int:
        p=c=0;return max((c:=x+c*(x>p),p:=x)[0]for x in n)

test('''
1800. Maximum Ascending Subarray Sum
Solved
Easy
Topics
Companies
Hint
Given an array of positive integers nums, return the maximum possible sum of an ascending subarray in nums.

A subarray is defined as a contiguous sequence of numbers in an array.

A subarray [numsl, numsl+1, ..., numsr-1, numsr] is ascending if for all i where l <= i < r, numsi  < numsi+1. Note that a subarray of size 1 is ascending.

 

Example 1:

Input: nums = [10,20,30,5,10,50]
Output: 65
Explanation: [5,10,50] is the ascending subarray with the maximum sum of 65.
Example 2:

Input: nums = [10,20,30,40,50]
Output: 150
Explanation: [10,20,30,40,50] is the ascending subarray with the maximum sum of 150.
Example 3:

Input: nums = [12,17,15,13,10,11,12]
Output: 33
Explanation: [10,11,12] is the ascending subarray with the maximum sum of 33.
 

Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100
Seen this question in a real interview before?
1/5
Yes
No
Accepted
65.7K
Submissions
105.9K
Acceptance Rate
62.1%
Topics
Array
Companies
Hint 1
It is fast enough to check all possible subarrays
Hint 2
The end of each ascending subarray will be the start of the next
Similar Questions
Find Good Days to Rob the Bank
Medium
Maximum Number of Books You Can Take
Hard
Count Strictly Increasing Subarrays
Medium
''')

