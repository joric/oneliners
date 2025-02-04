from lc import *

# divide and conquer

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def divide(nums, l, r):
            if l == r: return nums[l]
            mid = l + (r - l)//2
            lmax = divide(nums, l, mid)
            rmax = divide(nums, mid+1, r)
            left, right = float('-inf'), float('-inf')
            ans = 0
            for i in range(mid, l-1, -1):
                ans += nums[i]
                left = max(left, ans)
            ans = 0
            for j in range(mid+1, r+1):
                ans += nums[j]
                right = max(ans, right)
                
            return max(lmax, rmax, left+right)
        ans = divide(nums, 0, len(nums)-1)
        return ans

# dp

class Solution:
    def maxSubArray(self, a: List[int]) -> int:
        for i in range(1,len(a)):
            a[i] = max(a[i],a[i]+a[i-1])
        return max(a)

# kadane

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_max, max_till_now = 0, -inf
        for c in nums:
            cur_max = max(c, cur_max + c)
            max_till_now = max(max_till_now, cur_max)
        return max_till_now

# accumulate

class Solution:
    def maxSubArray(self, a: List[int]) -> int:
        return max(accumulate(a,lambda x,y:max(x+y,y)))

# smaller kadane

class Solution:
    def maxSubArray(self, n: List[int]) -> int:
        c,p = 0,-inf
        for x in n:
            p=max(p,c:=max(x,c+x))
        return p

class Solution:
    def maxSubArray(self, n: List[int]) -> int:
        c=0;return max(c:=max(x,c+x)for x in n)

test('''
53. Maximum Subarray
Medium

32009

1340

Add to List

Share
Given an integer array nums, find the subarray with the largest sum, and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 

Constraints:

1 <= nums.length <= 10^5
-104 <= nums[i] <= 10^4
 

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
''')
