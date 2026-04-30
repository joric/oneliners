from lc import *


# https://leetcode.com/problems/rotate-function/solutions/4367642/one-line-solution-by-xxxxkav-hums/?envType=daily-question&envId=2026-05-01

class Solution:
    def maxRotateFunction(self, a: List[int]) -> int:
        return(s:=sum(a),max(accumulate(reversed(a),lambda t,n:t+s-len(a)*n,initial=sum(i*n for i, n in enumerate(a)))))[1]


# https://leetcode.com/problems/rotate-function/solutions/7795196/two-simple-lines-of-code-by-mikposp-559j/?envType=daily-question&envId=2026-05-01

class Solution:
    def maxRotateFunction(self, a: List[int]) -> int:
        return max(accumulate(reversed(a),lambda F,v,q=sum(a):F+q-v*len(a),initial=sum(map(mul,a,count()))))

class Solution:
    def maxRotateFunction(self, a: List[int]) -> int:
        s=sum(a);f=sum(map(mul,a,count()));return max(f,*(f:=f+s-v*len(a)for v in a[::-1]))

test('''
396. Rotate Function
Medium
Topics
premium lock icon
Companies
You are given an integer array nums of length n.

Assume arrk to be an array obtained by rotating nums by k positions clock-wise. We define the rotation function F on nums as follow:

F(k) = 0 * arrk[0] + 1 * arrk[1] + ... + (n - 1) * arrk[n - 1].
Return the maximum value of F(0), F(1), ..., F(n-1).

The test cases are generated so that the answer fits in a 32-bit integer.

 

Example 1:

Input: nums = [4,3,2,6]
Output: 26
Explanation:
F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16
F(2) = (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3) = 0 + 6 + 8 + 9 = 23
F(3) = (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4) = 0 + 2 + 12 + 12 = 26
So the maximum value of F(0), F(1), F(2), F(3) is F(3) = 26.
Example 2:

Input: nums = [100]
Output: 0
 

Constraints:

n == nums.length
1 <= n <= 105
-100 <= nums[i] <= 100
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
114,301/249.8K
Acceptance Rate
45.8%
Topics
Junior
Array
Math
Dynamic Programming
''')
