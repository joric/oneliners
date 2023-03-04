from lc import *


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        r = 0
        a = b = c = -1
        for i,x in enumerate(nums):
            if not minK <= x <= maxK:
                c = i
            if x == minK:
                a = i
            if x == maxK:
                b = i
            r += max(0,min(a,b)-c)
        return r


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        return reduce(lambda p,e:(lambda a,b,c,r,i,x:(a:=i if x==minK else a,b:=i if x==maxK else b,c:=c if minK<=x<=maxK else i,r:=r+max(0,min(a,b)-c)))(*p,*e),enumerate(nums),[-1,-1,-1,0])[-1]


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        return (r:=0,a:=(b:=(c:=-1)),[(not minK<=x<=maxK and (c:=i),x==minK and (a:=i),x==maxK and (b:=i),r:=r+max(0,min(a,b)-c)) for i,x in enumerate(nums)],r)[3]

test('''

2444. Count Subarrays With Fixed Bounds
Hard

615

11

Add to List

Share
You are given an integer array nums and two integers minK and maxK.

A fixed-bound subarray of nums is a subarray that satisfies the following conditions:

The minimum value in the subarray is equal to minK.
The maximum value in the subarray is equal to maxK.
Return the number of fixed-bound subarrays.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [1,3,5,2,7,5], minK = 1, maxK = 5
Output: 2
Explanation: The fixed-bound subarrays are [1,3,5] and [1,3,5,2].
Example 2:

Input: nums = [1,1,1,1], minK = 1, maxK = 1
Output: 10
Explanation: Every subarray of nums is a fixed-bound subarray. There are 10 possible subarrays.
 

Constraints:

2 <= nums.length <= 10^5
1 <= nums[i], minK, maxK <= 10^6
''')
