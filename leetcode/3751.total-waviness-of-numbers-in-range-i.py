from lc import *

# https://leetcode.com/problems/total-waviness-of-numbers-in-range-i/solutions/7367907/python3-compare-digit-characters-ts-301-sjw0l/?envType=daily-question&envId=2026-06-04

class Solution:
    def totalWaviness(self, a: int, b: int) -> int:
        return sum(x<y>z or x>y<z for d in map(str,range(a,b+1))for x,y,z in zip(d,d[1:],d[2:]))

test('''
3751. Total Waviness of Numbers in Range I
Medium
Topics
premium lock icon
Companies
Hint
You are given two integers num1 and num2 representing an inclusive range [num1, num2].

The waviness of a number is defined as the total count of its peaks and valleys:

A digit is a peak if it is strictly greater than both of its immediate neighbors.
A digit is a valley if it is strictly less than both of its immediate neighbors.
The first and last digits of a number cannot be peaks or valleys.
Any number with fewer than 3 digits has a waviness of 0.
Return the total sum of waviness for all numbers in the range [num1, num2].
 

Example 1:

Input: num1 = 120, num2 = 130

Output: 3

Explanation:

In the range [120, 130]:
120: middle digit 2 is a peak, waviness = 1.
121: middle digit 2 is a peak, waviness = 1.
130: middle digit 3 is a peak, waviness = 1.
All other numbers in the range have a waviness of 0.
Thus, total waviness is 1 + 1 + 1 = 3.

Example 2:

Input: num1 = 198, num2 = 202

Output: 3

Explanation:

In the range [198, 202]:
198: middle digit 9 is a peak, waviness = 1.
201: middle digit 0 is a valley, waviness = 1.
202: middle digit 0 is a valley, waviness = 1.
All other numbers in the range have a waviness of 0.
Thus, total waviness is 1 + 1 + 1 = 3.

Example 3:

Input: num1 = 4848, num2 = 4848

Output: 2

Explanation:

Number 4848: the second digit 8 is a peak, and the third digit 4 is a valley, giving a waviness of 2.

 

Constraints:

1 <= num1 <= num2 <= 105
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
27,614/34.1K
Acceptance Rate
80.9%
Topics
Senior
Math
Dynamic Programming
Enumeration
Biweekly Contest 170
icon
Companies
Hint 1
Use bruteforce
''')
