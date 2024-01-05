from lc import *

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 0
        dp = [nums[0]]
        res = 1
        for num in nums[1:]:
            pos = bisect_left(dp, num)
            if pos == len(dp):
                dp.append(num)
            else:
                dp[pos] = num
            res = max(res, pos + 1)
        return res

# https://leetcode.com/problems/longest-increasing-subsequence/discuss/667975/Python-3-Lines-dp-with-binary-search-explained

class Solution:
    def lengthOfLIS(self, n: List[int]) -> int:
        d=[];[setitem(d,slice(i:=bisect_left(d,x),i+1),[x])for x in n];return len(d)

class Solution:
    def lengthOfLIS(self, n: List[int]) -> int:
        d=[inf]*2501;[setitem(d,bisect_left(d,x),x)for x in n];return d.index(inf)

test('''
300. Longest Increasing Subsequence
Medium

19534

372

Add to List

Share
Given an integer array nums, return the length of the longest strictly increasing subsequence.

 

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1
 

Constraints:

1 <= nums.length <= 2500
-10^4 <= nums[i] <= 10^4
 

Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?
''')

