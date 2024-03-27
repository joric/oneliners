from lc import *

# https://leetcode.com/problems/subarray-product-less-than-k/discuss/4730547/Binary-Search-and-Math

class Solution:
    def numSubarrayProductLessThanK(self, a: List[int], k: int) -> int:
        m,p,c=[*accumulate(a,mul)],1,0
        for i,x in enumerate(a):
            j = bisect_left(m,k*p,i,len(a))-1
            c += j-i+1 if i<j else 1 if i==j and a[i]<k else 0
            p *= x
        return c

class Solution:
    def numSubarrayProductLessThanK(self, a: List[int], k: int) -> int:
        m,p,c=[*accumulate(a,mul)],1,0;return sum((i<=(j:=bisect_left(m,k*(p:=p*x)//x,i,len(a))-1))*(j-i+1,1)[i==j and a[i]<k]for i,x in enumerate(a))

# https://leetcode.com/problems/subarray-product-less-than-k/discuss/560093/Python3-two-pointer-O(N)-O(1)-with-breakdown

class Solution:
    def numSubarrayProductLessThanK(self, a: List[int], k: int) -> int:
        l,p,c=0,1,0
        for r in range(len(a)):
            p *= a[r]
            while p>=k and l<=r:
                p /= a[l]
                l += 1
            c += r-l+1
        return c

class Solution:
    def numSubarrayProductLessThanK(self, a: List[int], k: int) -> int:
        l,p,c=0,1,0;return sum((p:=p*x,all(p>=k and l<=r and(p:=p/a[l],l:=l+1)for _ in a),r-l+1)[2]for r,x in enumerate(a))

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
