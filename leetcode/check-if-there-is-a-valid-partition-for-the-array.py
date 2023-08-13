from lc import *

# https://leetcode.com/problems/check-if-there-is-a-valid-partition-for-the-array/discuss/2390802/JavaC%2B%2BPython-DP-O(1)-Space

class Solution:
    def validPartition(self, a: List[int]) -> bool:
        n = len(a)
        d = [False]*3+[True]
        for i in range(n):
            d[i%4] = False
            if i>0 and a[i]==a[i-1]:
                d[i%4] |= d[(i-2)%4]
            if i>1 and (a[i]==a[i-1]==a[i-2] or a[i]==a[i-1]+1==a[i-2]+2):
                d[i%4] |= d[(i-3)%4]
        return d[(n-1)%4]

class Solution:
    def validPartition(self, a: List[int]) -> bool:
        d = [1]+[0]*len(a)
        for i in range(len(a)):
            if i>0 and a[i]==a[i-1]:
                d[i+1] |= d[i-1]
            if i>1 and (a[i]==a[i-1]==a[i-2] or a[i]==a[i-1]+1==a[i-2]+2):
                d[i+1] |= d[i-2]
        return d[-1]

# https://leetcode.com/problems/check-if-there-is-a-valid-partition-for-the-array/discuss/2390825/Python-or-Recursion

class Solution:
    def validPartition(self, a: List[int]) -> bool:
        n = len(a)
        @cache
        def f(i):
            if i==n:
                return True
            if i<n-1 and a[i]==a[i+1] and f(i+2):
                return True
            if i<n-2 and (a[i]==a[i+1]==a[i+2] or a[i]==a[i+1]-1==a[i+2]-2) and f(i+3):
                return True
            return False
        return f(0)

class Solution:
    def validPartition(self, a: List[int]) -> bool:
        n=len(a);return(f:=cache(lambda i:(i<n-2and(a[i]==a[i+1]==a[i+2]or a[i]==a[i+1]-1==a[i+2]-2)and f(i+3))or(i<n-1and a[i]==a[i+1]and f(i+2))or i==n))(0)

test('''
2369. Check if There is a Valid Partition For The Array
Medium

563

98

Add to List

Share
You are given a 0-indexed integer array nums. You have to partition the array into one or more contiguous subarrays.

We call a partition of the array valid if each of the obtained subarrays satisfies one of the following conditions:

The subarray consists of exactly 2 equal elements. For example, the subarray [2,2] is good.
The subarray consists of exactly 3 equal elements. For example, the subarray [4,4,4] is good.
The subarray consists of exactly 3 consecutive increasing elements, that is, the difference between adjacent elements is 1. For example, the subarray [3,4,5] is good, but the subarray [1,3,5] is not.
Return true if the array has at least one valid partition. Otherwise, return false.

 

Example 1:

Input: nums = [4,4,4,5,6]
Output: true
Explanation: The array can be partitioned into the subarrays [4,4] and [4,5,6].
This partition is valid, so we return true.
Example 2:

Input: nums = [1,1,1,2]
Output: false
Explanation: There is no valid partition for this array.
 

Constraints:

2 <= nums.length <= 10^5
1 <= nums[i] <= 10^6
''')

