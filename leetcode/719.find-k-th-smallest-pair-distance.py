from lc import *

# https://leetcode.com/problems/find-k-th-smallest-pair-distance/discuss/109092/%221-liner%22-and-%22almost-O(n)%22
# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/discuss/85170/on-from-paper-yes-orows

# TLE
class Solution:
    def kthSmallest(self, m: List[List[int]], k: int) -> int:
        return sorted(chain(*m))[k-1]
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        class Row(int):
            def __getitem__(self, j):
                return self - nums[~j]
        n = len(nums)
        return self.kthSmallest(map(Row, nums), k + n*(n+1)/2)

# https://leetcode.com/problems/find-k-th-smallest-pair-distance

class Solution:
    def smallestDistancePair(self, a: List[int], k: int) -> int:
        a.sort()
        def f(g):
            c = l = 0
            for r,x in enumerate(a):
                while x - a[l] > g:
                    l += 1
                c += r - l
            return c>=k
        l = 0
        r = a[-1] - a[0]
        while l < r:
            m = (l + r) // 2
            if f(m):
                r = m
            else:
                l = m + 1
        return l

class Solution:
    def smallestDistancePair(self, a: List[int], k: int) -> int:
        a.sort();return bisect_right(range(a[-1]-a[0]),0,key=lambda g,l=0:sum(r-(l:=(t:=lambda l:g<x-a[l]and t(l+1)or l)(l))for r,x in enumerate(a))>=k)

class Solution:
    def smallestDistancePair(self, a: List[int], k: int) -> int:
        a.sort();b=bisect_left;return b(range(a[-1]),k,key=lambda d:sum(r-b(range(r),-d,key=lambda l:a[l]-x)for r,x in enumerate(a)))

test('''
719. Find K-th Smallest Pair Distance
Hard

2988

99

Add to List

Share
The distance of a pair of integers a and b is defined as the absolute difference between a and b.

Given an integer array nums and an integer k, return the kth smallest distance among all the pairs nums[i] and nums[j] where 0 <= i < j < nums.length.

 

Example 1:

Input: nums = [1,3,1], k = 1
Output: 0
Explanation: Here are all the pairs:
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
Then the 1st smallest distance pair is (1,1), and its distance is 0.
Example 2:

Input: nums = [1,1,1], k = 2
Output: 0
Example 3:

Input: nums = [1,6,1], k = 3
Output: 5
 

Constraints:

n == nums.length
2 <= n <= 104
0 <= nums[i] <= 106
1 <= k <= n * (n - 1) / 2
Accepted
93,805
Submissions
244,072
''')