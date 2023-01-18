from lc import *


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_so_far = min_so_far = min_ending_here = max_ending_here = nums[0]
        for x in nums[1:]:
            max_ending_here = max(x, max_ending_here + x)
            max_so_far = max(max_so_far, max_ending_here)
            min_ending_here = min(x, min_ending_here + x)
            min_so_far = min(min_so_far, min_ending_here)
        if min_so_far == sum(nums):
            return max_so_far
        else:
            return max(max_so_far,sum(nums)-min_so_far)

class Solution:
    def maxSubarraySumCircular(self, v: List[int]) -> int:
        return ((a:=(b:=(c:=(d:=v[0])))),s:=sum(v),[(a:=max(x,a+x),b:=max(a,b),c:=min(x,c+x),d:=min(c,d)) for x in v[1:]],s==d and b or max(b,s-d))[-1]

test('''
918. Maximum Sum Circular Subarray
Medium

4038

181

Add to List

Share
Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.

A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].

A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.

 

Example 1:

Input: nums = [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3.
Example 2:

Input: nums = [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.
Example 3:

Input: nums = [-3,-2,-3]
Output: -2
Explanation: Subarray [-2] has maximum sum -2.
 

Example 4:

Input: nums = [0,2,-2]
Output: 2

Example 5:

Input: nums = [3,1,3,2,6]
Output: 15

Constraints:

n == nums.length
1 <= n <= 3 * 10^4
-3 * 104 <= nums[i] <= 3 * 10^4
''')

