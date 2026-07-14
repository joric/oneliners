from lc import *

# https://leetcode.com/problems/gcd-of-odd-and-even-sums/description/?envType=daily-question&envId=2026-07-15

class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        return n

test('''
3658. GCD of Odd and Even Sums
Easy
Topics
premium lock icon
Companies
Hint
You are given an integer n. Your task is to compute the GCD (greatest common divisor) of two values:

sumOdd: the sum of the smallest n positive odd numbers.

sumEven: the sum of the smallest n positive even numbers.

Return the GCD of sumOdd and sumEven.

 

Example 1:

Input: n = 4

Output: 4

Explanation:

Sum of the first 4 odd numbers sumOdd = 1 + 3 + 5 + 7 = 16
Sum of the first 4 even numbers sumEven = 2 + 4 + 6 + 8 = 20
Hence, GCD(sumOdd, sumEven) = GCD(16, 20) = 4.

Example 2:

Input: n = 5

Output: 5

Explanation:

Sum of the first 5 odd numbers sumOdd = 1 + 3 + 5 + 7 + 9 = 25
Sum of the first 5 even numbers sumEven = 2 + 4 + 6 + 8 + 10 = 30
Hence, GCD(sumOdd, sumEven) = GCD(25, 30) = 5.

 

Constraints:

1 <= n <= 10​​​​​​​00
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
101,267/118.9K
Acceptance Rate
85.2%
Topics
Mid Level
Math
Number Theory
Weekly Contest 464
icon
Companies
Hint 1
The first n odd numbers sum to n * n
Hint 2
First n even numbers sum to n * (n + 1)
Hint 3
gcd(n, n + 1) = 1, so the answer is n
''')
