from lc import *

# https://leetcode.com/problems/greatest-sum-divisible-by-three/solutions/5864437/one-line-solution-by-mikposp-2hsf/?envType=daily-question&envId=2025-11-23

class Solution:
    def maxSumDivThree(self, a: List[int]) -> int:
        w = sum(a)
        if w%3 == 0:
            return w
        q = defaultdict(lambda:[inf]*2)
        for v in a:
            q[v%3] = sorted(q[v%3]+[v])[:2]
        return w - min(q[w%3][0], sum(q[w%3%2+1]))

class Solution:
    def maxSumDivThree(self, a: List[int]) -> int:
        @cache
        def f(i, r):
            if i < len(a):
                return max(f(i+1, r), a[i] + f(i+1, (r + a[i])%3))
            return r and -inf
        return f(0, 0)

class Solution:
    def maxSumDivThree(self, a: List[int]) -> int:
        return(f:=cache(lambda i,r:i<len(a)and max(f(i+1,r),a[i]+f(i+1,(r+a[i])%3))or r and-inf))(0,0)

class Solution:
    def maxSumDivThree(self, a: List[int]) -> int:
        return(f:=cache(lambda i,r:i<len(a)and max(f(i+1,r),a[i]+f(i+1,(r+a[i])%3))or r and-99))(0,0)

test('''
1262. Greatest Sum Divisible by Three
Solved
Medium
Topics
premium lock icon
Companies
Hint
Given an integer array nums, return the maximum possible sum of elements of the array such that it is divisible by three.

 

Example 1:

Input: nums = [3,6,5,1,8]
Output: 18
Explanation: Pick numbers 3, 6, 1 and 8 their sum is 18 (maximum sum divisible by 3).
Example 2:

Input: nums = [4]
Output: 0
Explanation: Since 4 is not divisible by 3, do not pick any number.
Example 3:

Input: nums = [1,2,3,4,4]
Output: 12
Explanation: Pick numbers 1, 3, 4 and 4 their sum is 12 (maximum sum divisible by 3).
 

Constraints:

1 <= nums.length <= 4 * 104
1 <= nums[i] <= 104
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
83,229/157K
Acceptance Rate
53.0%
Topics
Array
Dynamic Programming
Greedy
Sorting
Weekly Contest 163
icon
Companies
Hint 1
Represent the state as DP[pos][mod]: maximum possible sum starting in the position "pos" in the array where the current sum modulo 3 is equal to mod.
''')
