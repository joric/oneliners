from lc import *

# https://leetcode.com/problems/minimum-size-subarray-sum/discuss/433123/JavaC%2B%2BPython-Sliding-Window

class Solution:
    def minSubArrayLen(self, s: int, a: List[int]) -> int:
        n=len(a)
        i,r=0,n+1
        for j in range(n):
            s -= a[j]
            while s <= 0:
                r = min(r, j-i+1)
                s += a[i]
                i += 1
        return r % (n+1)

class Solution:
    def minSubArrayLen(self, s: int, a: List[int]) -> int:
        n=len(a);i,r=0,n+1;[(s:=s-a[j],all(s<=0 and(r:=min(r,j-i+1),s:=s+a[i],i:=i+1)for _ in count()))for j in range(n)];return r%(n+1)

# https://leetcode.com/problems/minimum-size-subarray-sum/discuss/466182/2-lines-immutable-bisect-python

class Solution:
    def minSubArrayLen(self, s: int, a: List[int]) -> int:
        a=[*accumulate(a)];return min([i-bisect_right(a,x-s)+1for i,x in enumerate(a)if x>=s],default=0)


class Solution:
    def minSubArrayLen(self, s: int, a: List[int]) -> int:
        a=[*accumulate(a)];return-max([~i+bisect_right(a,x-s)for i,x in enumerate(a)if x>=s],default=0)

test('''
209. Minimum Size Subarray Sum
Medium

9773

276

Add to List

Share
Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
 

Constraints:

1 <= target <= 10^9
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^4
''')

