from lc import *

# https://leetcode.com/problems/jump-game-ix/solutions/?envType=daily-question&envId=2026-05-07

class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        pre_max = [nums[0]] * n
        for i in range(1, n):
            pre_max[i] = max(pre_max[i - 1], nums[i])
        suf_min = inf
        for i in range(n - 1, -1, -1):
            ans[i] = ans[i + 1] if pre_max[i] > suf_min else pre_max[i]
            suf_min = min(suf_min, nums[i])
        return ans

class Solution:
    def maxValue(self, n: List[int]) -> List[int]:
        p,s,a=[*accumulate(n,max)],inf,n*1;[setitem(a,i,s<p[i]and a[i+1]or p[i])or(s:=min(s,n[i]))for i in range(len(n))[::-1]];return a

test('''
3660. Jump Game IX
Medium
Topics
premium lock icon
Companies
Hint
You are given an integer array nums.

From any index i, you can jump to another index j under the following rules:

Jump to index j where j > i is allowed only if nums[j] < nums[i].
Jump to index j where j < i is allowed only if nums[j] > nums[i].
For each index i, find the maximum value in nums that can be reached by following any sequence of valid jumps starting at i.

Return an array ans where ans[i] is the maximum value reachable starting from index i.

 

Example 1:

Input: nums = [2,1,3]

Output: [2,2,3]

Explanation:

For i = 0: No jump increases the value.
For i = 1: Jump to j = 0 as nums[j] = 2 is greater than nums[i].
For i = 2: Since nums[2] = 3 is the maximum value in nums, no jump increases the value.
Thus, ans = [2, 2, 3].

Example 2:

Input: nums = [2,3,1]

Output: [3,3,3]

Explanation:

For i = 0: Jump forward to j = 2 as nums[j] = 1 is less than nums[i] = 2, then from i = 2 jump to j = 1 as nums[j] = 3 is greater than nums[2].
For i = 1: Since nums[1] = 3 is the maximum value in nums, no jump increases the value.
For i = 2: Jump to j = 1 as nums[j] = 3 is greater than nums[2] = 1.
Thus, ans = [3, 3, 3].

 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109​​​​​​​
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
17,225/71.3K
Acceptance Rate
24.2%
Topics
icon
Companies
Hint 1
Think of the array as a directed graph where edges represent valid jumps.
Hint 2
From index i, forward jumps go only to smaller values; backward jumps go only to larger values.
Hint 3
The maximum reachable value from i is the maximum value in the connected component reachable under these jump rules.
Hint 4
You can find connected ranges by looking at prefix maximums and suffix minimums, a cut happens where all values to the left are <= all values to the right.
''')
