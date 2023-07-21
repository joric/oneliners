from lc import *

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [[1, 1] for _ in range(len(nums))]
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    if dp[i][0] >= dp[j][0]: dp[j] = [dp[i][0] + 1, dp[i][1]]
                    elif dp[i][0] == dp[j][0] - 1: dp[j][1] += dp[i][1]
        dp.sort()
        return dp and sum(d[1] for d in dp if d[0] == dp[-1][0]) or 0

# https://leetcode.com/problems/number-of-longest-increasing-subsequence/discuss/199093/short-python-50ms-beats-100-with-binary-search

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        d = defaultdict(Counter)
        d[-1][-inf] = 1
        t = []
        for i in nums:
            k = bisect_left(t, i)
            if k == len(t):
                t.append(i)
            else:
                t[k] = i 
            d[k][i] += sum(d[k-1][j] for j in d[k-1] if j < i)
        return sum(d[max(0, len(t)-1)].values()) 

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        d,t=defaultdict(Counter),[];setitem(d[-1],-inf,1);[((k:=bisect_left(t,i))==len(t)and t.append(i)or setitem(t,k,i),d[k].update({i:sum(d[k-1][j]for j in d[k-1]if j<i)}))for i in nums];return sum(d[max(0,len(t)-1)].values())

test('''
673. Number of Longest Increasing Subsequence
Medium

5132

210

Add to List

Share
Given an integer array nums, return the number of longest increasing subsequences.

Notice that the sequence has to be strictly increasing.

 

Example 1:

Input: nums = [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].
Example 2:

Input: nums = [2,2,2,2,2]
Output: 5
Explanation: The length of the longest increasing subsequence is 1, and there are 5 increasing subsequences of length 1, so output 5.
 

Constraints:

1 <= nums.length <= 2000
-10^6 <= nums[i] <= 10^6
''')

