from lc import *

# https://leetcode.com/problems/valid-perfect-square/discuss/151403/Python-one-liner

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l,r = 0,num
        while l<=r:
            m = (l + r) // 2
            m2 = m*m
            if m2 == num: return True
            elif m2 < num:
                l = m + 1
            else:
                r = m - 1
        return False

class Solution:
    def isPerfectSquare(self, n: int) -> bool:
        return(t:=n**0.5)==int(t)

class Solution:
    def isPerfectSquare(self, n: int) -> bool:
        return isqrt(n)==sqrt(n)

test('''
367. Valid Perfect Square
Easy

4222

305

Add to List

Share
Given a positive integer num, return true if num is a perfect square or false otherwise.

A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.

You must not use any built-in library function, such as sqrt.

 

Example 1:

Input: num = 16
Output: true
Explanation: We return true because 4 * 4 = 16 and 4 is an integer.
Example 2:

Input: num = 14
Output: false
Explanation: We return false because 3.742 * 3.742 = 14 and 3.742 is not an integer.
 

Constraints:

1 <= num <= 231 - 1
Accepted
627,778
Submissions
1,434,138
''')
