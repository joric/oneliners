from lc import *

# https://leetcode.com/problems/power-of-three/solutions/77977/math-1-liner-no-log-with-explanation/?envType=daily-question&envId=2025-08-13

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n and n%3==0:
            n /= 3
        return n==1

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n>0==pow(3,19,n)

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n>0==3**19%n

test('''
326. Power of Three
Solved
Easy
Topics
premium lock icon
Companies
Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.

 

Example 1:

Input: n = 27
Output: true
Explanation: 27 = 33
Example 2:

Input: n = 0
Output: false
Explanation: There is no x where 3x = 0.
Example 3:

Input: n = -1
Output: false
Explanation: There is no x where 3x = (-1).
 

Other examples:

Input: n = 1
Output: true

Input: n = 243
Output: true


Constraints:

-231 <= n <= 231 - 1
 

Follow up: Could you solve it without loops/recursion?
Seen this question in a real interview before?
1/5
Yes
No
Accepted
1,088,697/2.2M
Acceptance Rate
48.6%
Topics
Math
Recursion
icon
Companies
Similar Questions
Power of Two
Easy
Power of Four
Easy
Check if Number is a Sum of Powers of Three
Medium
''')
