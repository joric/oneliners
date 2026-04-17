from lc import *

# https://leetcode.com/problems/mirror-distance-of-an-integer/solutions/7555288/one-line-by-khaled-alomari-yref/?envType=daily-question&envId=2026-04-18

class Solution:
    def mirrorDistance(self, n: int) -> int:
        return abs(n-int(str(n)[::-1]))

test('''
3783. Mirror Distance of an Integer
Easy
Topics
premium lock icon
Companies
Hint
You are given an integer n.

Define its mirror distance as: abs(n - reverse(n))​​​​​​​ where reverse(n) is the integer formed by reversing the digits of n.

Return an integer denoting the mirror distance of n​​​​​​​.

abs(x) denotes the absolute value of x.

 

Example 1:

Input: n = 25

Output: 27

Explanation:

reverse(25) = 52.
Thus, the answer is abs(25 - 52) = 27.
Example 2:

Input: n = 10

Output: 9

Explanation:

reverse(10) = 01 which is 1.
Thus, the answer is abs(10 - 1) = 9.
Example 3:

Input: n = 7

Output: 0

Explanation:

reverse(7) = 7.
Thus, the answer is abs(7 - 7) = 0.
 

Constraints:

1 <= n <= 109
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
56,283/64.1K
Acceptance Rate
87.8%
Topics
Mid Level
Math
Weekly Contest 481
icon
Companies
Hint 1
Simulate as described
''')
