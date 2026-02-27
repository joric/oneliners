from lc import *

# https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/solutions/4988332/one-line-solution-by-mikposp-ec4k/?envType=daily-question&envId=2026-02-28

class Solution:
    def concatenatedBinary(self, n: int) -> int:
        return reduce(lambda q,k:(q<<k.bit_length()|k)%(10**9+7),range(n+1))

class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10**9 + 7
        q = 0
        for k in range(1, n+1):
            q = (q << k.bit_length() | k)%MOD
        return q

class Solution:
    def concatenatedBinary(self, n: int) -> int:
        q=0;[q:=(q<<k.bit_length()|k)%(10**9+7)for k in range(1,n+1)];return q

class Solution:
    def concatenatedBinary(self, n: int) -> int:
        return int(''.join(bin(x)[2:]for x in range(1,n+1)),2)%(10**9+7)

# https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/solutions/2612301/python-one-liner-solution-by-jkpangilina-ourk/?envType=daily-question&envId=2026-02-28

class Solution:
    def concatenatedBinary(self, n: int) -> int:
        return int(''.join(f'{i:b}'for i in range(1,n+1)),2)%(10**9+7)

class Solution:
    def concatenatedBinary(self, n: int) -> int:
        return int(''.join(f'{i+1:b}'for i in range(n)),2)%(10**9+7)

test('''
1680. Concatenation of Consecutive Binary Numbers
Solved
Medium
Topics
premium lock icon
Companies
Hint
Given an integer n, return the decimal value of the binary string formed by concatenating the binary representations of 1 to n in order, modulo 109 + 7.

 

Example 1:

Input: n = 1
Output: 1
Explanation: "1" in binary corresponds to the decimal value 1. 
Example 2:

Input: n = 3
Output: 27
Explanation: In binary, 1, 2, and 3 corresponds to "1", "10", and "11".
After concatenating them, we have "11011", which corresponds to the decimal value 27.
Example 3:

Input: n = 12
Output: 505379714
Explanation: The concatenation results in "1101110010111011110001001101010111100".
The decimal value of that is 118505380540.
After modulo 109 + 7, the result is 505379714.
 

Constraints:

1 <= n <= 105
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
95,761/168.2K
Acceptance Rate
56.9%
Topics
Staff
Math
Bit Manipulation
Simulation
Weekly Contest 218
icon
Companies
Hint 1
Express the nth number value in a recursion formula and think about how we can do a fast evaluation.
Similar Questions
Maximum Possible Number by Binary Concatenation
Medium
''')
