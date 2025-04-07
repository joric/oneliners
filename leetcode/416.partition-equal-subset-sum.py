from lc import *

# https://leetcode.com/problems/partition-equal-subset-sum/description/?envType=daily-question&envId=2025-04-07

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s%2:
            return False
        s //= 2
        dp = [False] * (s+1)
        dp[0] = True
        for num in nums:
            for i in range(1, s+1)[::-1]:
                if i >= num:
                    dp[i] = dp[i] or dp[i-num]
        return dp[s]

class Solution:
    def canPartition(self, a: List[int]) -> bool:
        t=sum(a);return(t+1)%2*reduce(lambda p,x:p|p<<x,a,1)&1<<t//2>0


test('''
416. Partition Equal Subset Sum
Solved
Medium
Topics
Companies
Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

 

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
 

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100
Seen this question in a real interview before?
1/5
Yes
No
Accepted
1.1M
Submissions
2.4M
Acceptance Rate
47.7%
Topics
Array
Dynamic Programming
Companies
Similar Questions
Partition to K Equal Sum Subsets
Medium
Minimize the Difference Between Target and Chosen Elements
Medium
Maximum Number of Ways to Partition an Array
Hard
Partition Array Into Two Arrays to Minimize Sum Difference
Hard
Find Subarrays With Equal Sum
Easy
Number of Great Partitions
Hard
Split With Minimum Sum
Easy
''')
