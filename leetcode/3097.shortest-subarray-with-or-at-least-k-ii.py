from lc import *

# https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-ii/discuss/4948586/Python-3-oror-14-lines-two-pointers-oror-TS%3A-44-95

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int, mxBits = 32) -> int:
        def f(num, incr, mask = 0):
            for bit in range(mxBits):
                if num & (1 << bit):
                    bitCtr[bit] += incr
                if bitCtr[bit]:
                    mask |= 1 << bit
            return mask

        if k == 0 or max(nums) >= k:
            return 1

        leftPtr, ans, bitCtr = 0, inf, [0] * mxBits
        for rghtPtr in range(len(nums)):
            mask = f(nums[rghtPtr], 1)
            while mask >= k:
                ans = min(ans, rghtPtr - leftPtr + 1)
                mask = f(nums[leftPtr], -1)
                leftPtr += 1
        return -1 if ans == inf else ans

# https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-ii/discuss/4948429/O(n)-one-liner-(fastest-solution-on-leetcode)

class Solution:
    def minimumSubarrayLength(self, n: List[int], k: int) -> int:
        i,t,a,d,r = 0,0,inf,[0]*32,range(32)
        for j,x in enumerate(n):
            t |= x
            for b in r:
                d[b] += (x >> b) & 1
            while i <= j and t >= k:
                a = min(a, j - i + 1)
                for b in r:
                    d[b] -= (n[i] >> b) & 1
                    if d[b] == 0:
                        t &= ~(1 << b)
                i += 1
        return(-1,a)[a<inf]

# TODO
class Solution:
    def minimumSubarrayLength(self, n: List[int], k: int) -> int:
        i,t,a,d,r = 0,0,inf,[0]*32,range(32)
        for j,x in enumerate(n):
            t |= x
            [setitem(d,b,d[b]+(1&(x>>b)))for b in r]
            for i in range(i,j+1):
                if t<k: break
                a = min(a,j-i+1)
                [setitem(d,b,d[b]-(1&(n[i]>>b)&1))or 0==d[b]and(t:=t&~(1<<b))for b in r]
        return(-1,a)[a<inf]

test('''
3097. Shortest Subarray With OR at Least K II
Medium

257

13

Add to List

Share
You are given an array nums of non-negative integers and an integer k.

An array is called special if the bitwise OR of all of its elements is at least k.

Return the length of the shortest special non-empty subarray of nums, or return -1 if no special subarray exists.

 

Example 1:

Input: nums = [1,2,3], k = 2

Output: 1

Explanation:

The subarray [3] has OR value of 3. Hence, we return 1.

Example 2:

Input: nums = [2,1,8], k = 10

Output: 3

Explanation:

The subarray [2,1,8] has OR value of 11. Hence, we return 3.

Example 3:

Input: nums = [1,2], k = 0

Output: 1

Explanation:

The subarray [1] has OR value of 1. Hence, we return 1.

 

Other examples:

Input: nums = [1,2,12,50,96,1], k = 93
Output: 1

Constraints:

1 <= nums.length <= 2 * 105
0 <= nums[i] <= 109
0 <= k <= 109
Accepted
19,518
Submissions
56,053
''')
