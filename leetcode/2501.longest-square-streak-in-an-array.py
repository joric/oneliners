from lc import *

# https://leetcode.com/problems/longest-square-streak-in-an-array/discuss/2919210/Video-Walkthrough-oror-Python-oror-3-Line-Solution

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        D,_ = defaultdict(lambda: 0), nums.sort()
        for num in nums: D[num/1] = 1 + D[num ** (1/2)]
        return max((v for v in D.values() if v > 1), default=-1)

# https://leetcode.com/problems/longest-square-streak-in-an-array/discuss/2900114/6-lines-with-hashmap

class Solution:
    def longestSquareStreak(self, n: List[int]) -> int:
        r,c = -1, {}
        for x in reversed(sorted(n)):
            c[x] = c.get(x*x,0)+1
            if c[x] > 1:
                r = max(r,c[x])
        return r

class Solution:
    def longestSquareStreak(self, n: List[int]) -> int:
        return(t:=max(reduce(lambda c,x:setitem(c,x,1+c.get(x*x,0))or c,sorted(n)[::-1],{}).values()),-1)[t<2]

class Solution:
    def longestSquareStreak(self, n: List[int]) -> int:
        c=Counter();[setitem(c,x,c[x*x]+1)for x in reversed(sorted(n))];return(t:=max(c.values()),-1)[t<2]

class Solution:
    def longestSquareStreak(self, n: List[int]) -> int:
        c=Counter();return max(setitem(c,x,t:=c[x*x]+1)or(t,-1)[t<2]for x in sorted(n)[::-1])

class Solution:
    def longestSquareStreak(self, n: List[int]) -> int:
        c={};return max(setitem(c,x,t:=1+c.get(x*x,0))or(t,-1)[t<2]for x in sorted(n)[::-1])

# https://leetcode.com/problems/longest-square-streak-in-an-array/discuss/5977715/One-Line-Solution

class Solution:
    def longestSquareStreak(self, a: List[int]) -> int:
        return (-1,r:=max(map(f:=cache(lambda v:1+(v*v in a and f(v*v))),a:={*a})))[r>1]

class Solution:
    def longestSquareStreak(self, a: List[int]) -> int:
        return(-1,r:=max(map(f:=lambda v:1+(v*v in a and f(v*v)),a:={*a})))[r>1]

test('''
2501. Longest Square Streak in an Array
Medium

469

10

Add to List

Share
You are given an integer array nums. A subsequence of nums is called a square streak if:

The length of the subsequence is at least 2, and
after sorting the subsequence, each element (except the first element) is the square of the previous number.
Return the length of the longest square streak in nums, or return -1 if there is no square streak.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: nums = [4,3,6,16,8,2]
Output: 3
Explanation: Choose the subsequence [4,16,2]. After sorting it, it becomes [2,4,16].
- 4 = 2 * 2.
- 16 = 4 * 4.
Therefore, [4,16,2] is a square streak.
It can be shown that every subsequence of length 4 is not a square streak.
Example 2:

Input: nums = [2,3,5,6,7]
Output: -1
Explanation: There is no square streak in nums so return -1.

Other examples:

Input: nums = [2,2]
Output: -1


Constraints:

2 <= nums.length <= 105
2 <= nums[i] <= 105
Accepted
27,757
Submissions
68,821
''')
