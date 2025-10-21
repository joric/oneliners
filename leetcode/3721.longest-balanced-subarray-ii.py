from lc import *

# https://leetcode.com/problems/longest-balanced-subarray-ii/

# same as https://leetcode.com/problems/longest-balanced-subarray-i but with 10^5 limit instead of 1500

# TODO

class Solution:
    def longestBalanced(self, nums: list[int]) -> int:
        max_len = 0
        n = len(nums)
        for i in range(n):
            even_set = set()
            odd_set = set()
            for j in range(i, n):
                num = nums[j]
                if num % 2 == 0:
                    even_set.add(num)
                else:
                    odd_set.add(num)
                
                if len(even_set) == len(odd_set):
                    max_len = max(max_len, j - i + 1)
        return max_len

# FatalError (top 18) https://leetcode.com/contest/weekly-contest-472/ranking/?region=global_v2

import numpy as np
class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        last = {}
        n = len(nums)
        pres = np.zeros(n+1, dtype=np.int32)
        ans = np.array(0)
        for i, x in enumerate(nums):
            if x in last:
                pres[last[x]+1:i+1] -= 1 if x % 2 else -1
            pres[i+1] = pres[i] + (1 if x % 2 else -1)
            ma = np.flatnonzero(pres[:i+1] == pres[i+1])
            if ma.size:
                ans = max(ans, i+1 - ma[0])
            last[x] = i
        return ans.item()

class Solution:
    def longestBalanced(self, n: List[int]) -> int:
        p,m=__import__('numpy'),len(n)
        l,a,s,r={},0,p.zeros(m+1, dtype=p.int32),p.array(0)
        for i, x in enumerate(n):
            if x in l:
                s[l[x]+1:i+1] -= 1 if x%2 else -1
            s[i+1] = s[i] + (1 if x%2 else -1)
            l[x] = i
            if (f:=p.flatnonzero(s[:i+1] == s[i+1])).size:
                r = max(r, i+1 - f[0])
        return r.item()


test('''
3721. Longest Balanced Subarray II
Hard
premium lock icon
Companies
Hint
You are given an integer array nums.

A subarray is called balanced if the number of distinct even numbers in the subarray is equal to the number of distinct odd numbers.

Return the length of the longest balanced subarray.

 

Example 1:

Input: nums = [2,5,4,3]

Output: 4

Explanation:

The longest balanced subarray is [2, 5, 4, 3].
It has 2 distinct even numbers [2, 4] and 2 distinct odd numbers [5, 3]. Thus, the answer is 4.
Example 2:

Input: nums = [3,2,2,5,4]

Output: 5

Explanation:

The longest balanced subarray is [3, 2, 2, 5, 4].
It has 2 distinct even numbers [2, 4] and 2 distinct odd numbers [3, 5]. Thus, the answer is 5.
Example 3:

Input: nums = [1,2,3,2]

Output: 3

Explanation:

The longest balanced subarray is [2, 3, 2].
It has 1 distinct even number [2] and 1 distinct odd number [3]. Thus, the answer is 3.
 

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^5
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
1,224/18.4K
Acceptance Rate
6.7%
Topics
Weekly Contest 472
icon
Companies
Hint 1
Store the first (or all) occurrences for each value in pos[val].
Hint 2
Build a lazy segment tree over start indices l in [0..n-1] that supports range add and can tell if any index has value 0 (keep mn/mx).
Hint 3
Use sign = +1 for odd values and sign = -1 for even values.
Hint 4
Initialize by adding each value's contribution with update(p, n-1, sign) where p is its current first occurrence.
Hint 5
Slide left l: pop pos[nums[l]], let next = next occurrence or n, do update(0, next-1, -sign), then query for any r >= l with value 0 and update ans = max(ans, r-l+1).
''')
