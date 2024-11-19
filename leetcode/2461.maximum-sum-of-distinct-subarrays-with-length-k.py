from lc import *

# https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/discuss/2786087/Python-3-oror-sliding-window-w-explanation-oror-TS%3A-56-42

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        res, cur, pos, dup = 0, 0, [-1] * 100001, -1
        for i in range(0,len(nums)):
            cur += nums[i]
            if i >= k:
                cur -= nums[i-k]
            dup = max(dup, pos[nums[i]])
            if i - dup >= k:
                res = max(res, cur)
            pos[nums[i]] = i
        return res

class Solution:
    def maximumSubarraySum(self, a: List[int], k: int) -> int:
        r=c=0;p,d=[-1]*100001,-1;[(c:=c+a[i],i>=k and(c:=c-a[i-k]),d:=max(d,p[a[i]]),setitem(p,a[i],i),i-d>=k and(r:=max(r,c)))for i in range(len(a))];return r

test('''
2461. Maximum Sum of Distinct Subarrays With Length K
Medium

1596

31

Add to List

Share
You are given an integer array nums and an integer k. Find the maximum subarray sum of all the subarrays of nums that meet the following conditions:

The length of the subarray is k, and
All the elements of the subarray are distinct.
Return the maximum subarray sum of all the subarrays that meet the conditions. If no subarray meets the conditions, return 0.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,5,4,2,9,9,9], k = 3
Output: 15
Explanation: The subarrays of nums with length 3 are:
- [1,5,4] which meets the requirements and has a sum of 10.
- [5,4,2] which meets the requirements and has a sum of 11.
- [4,2,9] which meets the requirements and has a sum of 15.
- [2,9,9] which does not meet the requirements because the element 9 is repeated.
- [9,9,9] which does not meet the requirements because the element 9 is repeated.
We return 15 because it is the maximum subarray sum of all the subarrays that meet the conditions
Example 2:

Input: nums = [4,4,4], k = 3
Output: 0
Explanation: The subarrays of nums with length 3 are:
- [4,4,4] which does not meet the requirements because the element 4 is repeated.
We return 0 because no subarrays meet the conditions.
 

Constraints:

1 <= k <= nums.length <= 105
1 <= nums[i] <= 105
Accepted
101,718
Submissions
266,510
''')
