from lc import *

# In short, start with mod =0, then we always do mod = (mod+nums[i])%k,
# if mod repeats, that means between these two mod = x occurences the sum is multiple of k.

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        m, c = {0: -1}, 0
        for i,x in enumerate(nums):
            c = (c + x) % abs(k) if k else c + x
            if i - m.setdefault(c, i) > 1:
                return True
        return False

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        return next((1 for i,x in enumerate(nums) if i-m.setdefault(c:=(c+x)%abs(k) if k else c+x or 1,i)>1),(m:={0:-1}) and (c:=0))

# updated 2024-06-08

# https://leetcode.com/problems/continuous-subarray-sum/discuss/99568/3-lines-Python

class Solution:
    def checkSubarraySum(self, n: List[int], k: int) -> bool:
        p=__import__('numpy').cumsum([0]+n)%(k or 2**31);return any(x in p[i+2:]for i,x in enumerate(p))


class Solution:
    def checkSubarraySum(self, n: List[int], k: int) -> bool:
        p=__import__('numpy').cumsum([0]+n)%(k or 2**31);

        d = map(lambda x:x%(k or 2**31),accumulate([0]+n))

        print(n,p,d)

        return any(x in p[i+2:]for i,x in enumerate(p))

test('''
523. Continuous Subarray Sum
Medium

2634

320

Add to List

Share
Given an integer array nums and an integer k, return true if nums has a continuous subarray of size at least two
whose elements sum up to a multiple of k, or false otherwise.

An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.

Example 1:

Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.

Example 2:

Input: nums = [23,2,6,4,7], k = 6
Output: true
Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.

Example 3:

Input: nums = [23,2,6,4,7], k = 13
Output: false

Other examples:

Input: nums = [23,2,4,6,6], k = 7
Output: true

Constraints:

1 <= nums.length <= 10^5
0 <= nums[i] <= 10^9
0 <= sum(nums[i]) <= 2^31 - 1
1 <= k <= 2^31 - 1
''')