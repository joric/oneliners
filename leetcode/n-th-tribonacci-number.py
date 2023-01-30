from lc import *

class Solution:
    def tribonacci(self, n: int) -> int:
        return (f:=cache(lambda n:f(n-1)+f(n-2)+f(n-3) if n>2 else 1 if n==2 else n))(n)

# https://leetcode.com/problems/n-th-tribonacci-number/discuss/2775508/Python3-One-Line-Solution-with-no-Recursion-that-looks-really-weird

class Solution:
    def tribonacci(self, n: int) -> int:
        return round((1.83928675521**n)*0.33622811699)

# https://leetcode.com/problems/n-th-tribonacci-number/discuss/1427626/Python-2-Line-DP

class Solution:
    def tribonacci(self, n: int) -> int:
        return (f:=cache(lambda n:max(n,0) if n<2 else f(n-1)+f(n-2)+f(n-3)))(n)

# 3 vars

class Solution:
    def tribonacci(self, n: int) -> int:
        a,b,c = 0,1,1
        for i in range(3, n+1):
            a,b,c = b,c,a+b+c
        return max(n,0) if n<2 else c

test('''

1137. N-th Tribonacci Number
Easy

2590

135

Add to List

Share
The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

 

Example 1:

Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
Example 2:

Input: n = 25
Output: 1389537
 

Example 2:

Input: n = 0
Output: 0

Example 3:

Input: n = 1
Output: 1

Example 4:

Input: n = 2
Output: 1

Constraints:

0 <= n <= 37
The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.

''')


