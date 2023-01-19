from lc import *

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        r=p=0
        c = [1] + [0] * k
        for x in nums:
            p = (p + x) % k
            r += c[p]
            c[p] += 1
        return r

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        c, r = [1]+[0]*(k-1), 0
        for i in accumulate(nums):
            r += c[i%k]
            c[i%k] += 1
        return r

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        return reduce(lambda p,i:(p[0]+p[1][i%k],p[1].update({i%k:1}) or p[1]),accumulate(nums),[0,Counter([0])])[0]

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        return (c:=Counter([0])) and reduce(lambda r,i:c.update({i%k:1}) or r+c[i%k]-1,accumulate(nums),0)


test('''

974. Subarray Sums Divisible by K
Medium

4128

161

Add to List

Share
Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by k = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
Example 2:

Input: nums = [5], k = 9
Output: 0
 

Constraints:

1 <= nums.length <= 3 * 10^4
-104 <= nums[i] <= 10^4
2 <= k <= 10^4

''')

