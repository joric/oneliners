from lc import *

# recursion (gives TLE)
# https://leetcode.com/problems/longest-increasing-subsequence/discuss/1396475/Recursive-and-Dp-code

class Solution:
    def lengthOfLIS(self, n: List[int]) -> int:
        @cache
        def f(i,j):
            if i==len(n):
                return 0
            a = 0
            if j==-1 or n[j]<n[i]:
                a = 1+f(i+1,i)
            b = f(i+1,j)
            return max(a,b)
        return f(0,-1)

class Solution:
    def lengthOfLIS(self, n: List[int]) -> int:
        return(f:=cache(lambda i,j:n[i:]and max((j==-1or n[j]<n[i])and 1+f(i+1,i),f(i+1,j))or 0))(0,-1)

# https://leetcode.com/problems/longest-increasing-subsequence/submissions

class Solution:
    def lengthOfLIS(self, n: List[int]) -> int:
        @cache
        def f(i):
            r = 1
            for j in range(i):
                if n[j] < n[i]:
                    r = max(r, f(j) + 1)
            return r
        return max(f(i)for i in range(len(n)))

class Solution:
    def lengthOfLIS(self, n: List[int]) -> int:
        return max(map((f:=cache(lambda i:1+max((f(j)for j in range(i)if n[j]<n[i]),default=0))),range(len(n))))

class Solution:
    def lengthOfLIS(self, n: List[int]) -> int:
        return max(map((f:=cache(lambda i:1+max([0]+[f(j)for j in range(i)if n[j]<n[i]]))),range(len(n))))

# dp solution

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
        d=[]
        for x in n:
            i = bisect_left(d,x)
            d[i:i+1] = [x]
        return len(d)

class Solution:
    def lengthOfLIS(self, n: List[int]) -> int:
        d=[];[setitem(d,i,x)if(i:=bisect_left(d,x))<len(d)else d.append(x)for x in n];return len(d)

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
 

Example 4:
Input: nums = [-1,-2,-3,-4,-5,-6]
Output: 1

Constraints:

1 <= nums.length <= 2500
-10^4 <= nums[i] <= 10^4
 

Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?
''')

