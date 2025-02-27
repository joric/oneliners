from lc import *

# https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/solutions/1092218/one-line-recursive-solution-back-tracking-python/

# TLE
class Solution:
    def maximumScore(self, a: List[int], m: List[int]) -> int:
        return m and max(a[0]*m[0]+self.maximumScore(a[1:],m[1:]),a[-1]*m[0]+self.maximumScore(a[0:-1],m[1:]))or 0

# https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/

class Solution:
    def maximumScore(self, n: List[int], m: List[int]) -> int:
        a = [0] * (len(m) + 1)
        for i in range(len(m) - 1, -1, -1):
            r = a.copy()
            for j in range(i, -1, -1):
                a[j] = max(m[i] * n[j] + r[j + 1], m[i] * n[len(n)- 1 - i + j] + r[j])
        return a[0]

class Solution:
    def maximumScore(self, n: List[int], m: List[int]) -> int:
        @cache
        def f(i,l):
            if(i == len(m)):
                return 0;
            return max(m[i]*n[l]+f(i+1, l+1), m[i]*n[len(n)-1-(i-l)]+f(i+1, l))
        return f(0,0)

class Solution:
    def maximumScore(self, n: List[int], m: List[int]) -> int:
        return (f:=cache(lambda i,j: i<len(m) and max(m[i]*n[j]+f(i+1, j+1), m[i]*n[len(n)-1-(i-j)]+f(i+1, j))))(0,0)

# updated 2025-02-27

class Solution:
    def maximumScore(self, n: List[int], m: List[int]) -> int:
        return(f:=cache(lambda i,j:i<len(m)and max(m[i]*n[j]+f(i+1,j+1),m[i]*n[~i+j]+f(i+1,j))))(0,0)

test('''
1770. Maximum Score from Performing Multiplication Operations
Hard

You are given two 0-indexed integer arrays nums and multipliers of size n and m respectively, where n >= m.

You begin with a score of 0. You want to perform exactly m operations. On the ith operation (0-indexed) you will:

Choose one integer x from either the start or the end of the array nums.
Add multipliers[i] * x to your score.
Note that multipliers[0] corresponds to the first operation, multipliers[1] to the second operation, and so on.
Remove x from nums.
Return the maximum score after performing m operations.
Example 1:

Input: nums = [1,2,3], multipliers = [3,2,1]
Output: 14
Explanation: An optimal solution is as follows:
- Choose from the end, [1,2,3], adding 3 * 3 = 9 to the score.
- Choose from the end, [1,2], adding 2 * 2 = 4 to the score.
- Choose from the end, [1], adding 1 * 1 = 1 to the score.
The total score is 9 + 4 + 1 = 14.

Example 2:

Input: nums = [-5,-3,-3,-2,7,1], multipliers = [-10,-5,3,4,6]
Output: 102
Explanation: An optimal solution is as follows:
- Choose from the start, [-5,-3,-3,-2,7,1], adding -5 * -10 = 50 to the score.
- Choose from the start, [-3,-3,-2,7,1], adding -3 * -5 = 15 to the score.
- Choose from the start, [-3,-2,7,1], adding -3 * 3 = -9 to the score.
- Choose from the end, [-2,7,1], adding 1 * 4 = 4 to the score.
- Choose from the end, [-2,7], adding 7 * 6 = 42 to the score. 
The total score is 50 + 15 - 9 + 4 + 42 = 102.

Constraints:

n == nums.length
m == multipliers.length
1 <= m <= 300
m <= n <= 10**5
-1000 <= nums[i], multipliers[i] <= 1000

''')