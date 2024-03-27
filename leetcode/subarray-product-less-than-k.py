from lc import *

# https://leetcode.com/problems/subarray-product-less-than-k/discuss/131805/Python-sliding-window-6-lines-simple-solution-304-ms-beats-90

class Solution:
    def numSubarrayProductLessThanK(self, a: List[int], k: int) -> int:
        l,s,p = 0,0,1
        for r,x in enumerate(a):
            p *= x
            while p>=k and l<r:
                p //= a[l]
                l += 1
            if p<k:
                s += r-l+1
        return s

class Solution:
    def numSubarrayProductLessThanK(self, a: List[int], k: int) -> int:
        l,s,p=0,0,1;return sum((p:=p*x,all(p>=k and l<r and(p:=p//a[l],l:=l+1)for _ in a))and p<k and r-l+1 for r,x in enumerate(a))

test('''
713. Subarray Product Less Than K
Medium

6027

192

Add to List

Share
Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

 

Example 1:

Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
Example 2:

Input: nums = [1,2,3], k = 0
Output: 0
 

Constraints:

1 <= nums.length <= 3 * 104
1 <= nums[i] <= 1000
0 <= k <= 106
Accepted
274,205
Submissions
579,693
''')
