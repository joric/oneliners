from lc import *

# https://leetcode.com/problems/count-the-number-of-fair-pairs/discuss/3174030/C%2B%2B-oror-Python3-sorting-lower-and-upper

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        ans=0
        for i in range(len(nums)-1, -1, -1):
            v = nums[i]
            a = bisect_left(nums, lower - v, lo=0, hi=i)
            b = bisect_right(nums, upper - v, lo=0, hi=i)
            ans += b - a
        return ans

# https://leetcode.com/problems/count-the-number-of-fair-pairs/discuss/3189582/Python-Elegant-and-Short-or-Two-lines-or-Bisect-or-In-place

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        return sum(bisect_right(nums, upper - num, hi=i) - bisect_left(nums, lower - num, hi=i)for i, num in enumerate(nums))

class Solution:
    def countFairPairs(self, a: List[int], l: int, u: int) -> int:
        a.sort();return sum(bisect_right(a,u-x,hi=i)-bisect_left(a,l-x, hi=i)for i,x in enumerate(a))

# https://leetcode.com/problems/count-the-number-of-fair-pairs/discuss/3174148/Python3-Sort-and-Bilinear-Search-3-lines

class Solution:
    def countFairPairs(self, a: List[int], l: int, u: int) -> int:
        a.sort();return sum(abs(bisect_left(a,l-a[k])-bisect_right(a,u-a[k])) -(l-a[k]<=a[k]<=u-a[k])for k in range(len(a)))//2

# https://leetcode.com/problems/count-the-number-of-fair-pairs/discuss/3177505/Python3-oror-3-lines-sort-and-bisect-oror-TS%3A-68-71

class Solution:
    def countFairPairs(self, nums: list[int], lower: int, upper: int) -> int:
        f = lambda x: sum(bisect_right(nums, x - num, hi = i) for i, num in enumerate(nums))
        nums.sort()
        return f(upper) - f(lower - 1)

class Solution:
    def countFairPairs(self, a: list[int], l: int, u: int) -> int:
        a.sort();return sub(*(sum(bisect_right(a,p-x,hi=i)for i,x in enumerate(a))for p in(u,l-1)))

test('''
2563. Count the Number of Fair Pairs
Medium

892

49

Add to List

Share
Given a 0-indexed integer array nums of size n and two integers lower and upper, return the number of fair pairs.

A pair (i, j) is fair if:

0 <= i < j < n, and
lower <= nums[i] + nums[j] <= upper
 

Example 1:

Input: nums = [0,1,7,4,4,5], lower = 3, upper = 6
Output: 6
Explanation: There are 6 fair pairs: (0,3), (0,4), (0,5), (1,3), (1,4), and (1,5).
Example 2:

Input: nums = [1,7,9,2,5], lower = 11, upper = 11
Output: 1
Explanation: There is a single fair pair: (2,3).
 

Constraints:

1 <= nums.length <= 105
nums.length == n
-109 <= nums[i] <= 109
-109 <= lower <= upper <= 109
Accepted
34,603
Submissions
94,929
''')
