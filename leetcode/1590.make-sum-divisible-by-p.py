from lc import *

# https://leetcode.com/problems/make-sum-divisible-by-p/discuss/854214/Clean-Python-3-prefix-accumulative-rest-O(N)

class Solution:
    def minSubarray(self, a: List[int], p: int) -> int:
        a=[x%p for x in a]
        r = sum(a) % p
        c, n = {0: -1}, len(a)
        for i,x in enumerate(accumulate(a)):
            if (m := (x-r) % p) in c:
                n = min(n, i - c[m])
            c[x % p] = i
        return -1 if n == len(a) else 0 if r==0 else n

class Solution:
    def minSubarray(self, a: List[int], p: int) -> int:
        c = {0: -1}
        n = len(a)
        t = sum(a) % p
        for i,x in enumerate(accumulate(a)):
            c[x%p] = i
            k = (x-t)%p
            if k in c:
                n = min(n, i-c[k])
        return n if n < len(a) else -1

# POTD 2023-11-30

class Solution:
    def minSubarray(self, a: List[int], p: int) -> int:
        c,n,t={0:-1},len(a),sum(a)%p;return(-1,n:=min(i-c[k]for i,x in enumerate(accumulate(a))if setitem(c,x%p,i)or(k:=(x-t)%p)in c))[n<len(a)]

test('''
1590. Make Sum Divisible by P
Medium

1553

69

Add to List

Share
Given an array of positive integers nums, remove the smallest subarray (possibly empty) such that the sum of the remaining elements is divisible by p. It is not allowed to remove the whole array.

Return the length of the smallest subarray that you need to remove, or -1 if it's impossible.

A subarray is defined as a contiguous block of elements in the array.

 

Example 1:

Input: nums = [3,1,4,2], p = 6
Output: 1
Explanation: The sum of the elements in nums is 10, which is not divisible by 6. We can remove the subarray [4], and the sum of the remaining elements is 6, which is divisible by 6.
Example 2:

Input: nums = [6,3,5,2], p = 9
Output: 2
Explanation: We cannot remove a single element to get a sum divisible by 9. The best way is to remove the subarray [5,2], leaving us with [6,3] with sum 9.
Example 3:

Input: nums = [1,2,3], p = 3
Output: 0
Explanation: Here the sum is 6. which is already divisible by 3. Thus we do not need to remove anything.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= p <= 109
Accepted
31,473
Submissions
107,485
''')
