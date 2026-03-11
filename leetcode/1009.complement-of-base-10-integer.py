from lc import *

# https://leetcode.com/problems/complement-of-base-10-integer/solutions/612724/idiots-solution-for-python-3-100-no-loop-dwxd/

class Solution:
    def bitwiseComplement(self, n: int) -> int:
        return int(''.join('10'[c>'0']for c in bin(n)[2:]),2)

class Solution:
    def bitwiseComplement(self, n: int) -> int:
        return~-2**(n.bit_length()or 1)^n

class Solution:
    def bitwiseComplement(self, n: int) -> int:
        return n^~-(1<<len(bin(n))-2)

class Solution:
    def bitwiseComplement(self, n: int) -> int:
        return~-(1<<len(bin(n))-2)^n

class Solution:
    def bitwiseComplement(self, n: int) -> int:
        return n^((1<<len(bin(n))-2)-1)

class Solution:
    def bitwiseComplement(self, n: int) -> int:
        return~n+2**len(bin(n))//4

class Solution:
    def bitwiseComplement(self, n: int) -> int:
        return~-2**len(f'{n:b}')^n

# POTD 2026-03-11

class Solution:
    def bitwiseComplement(self, n: int, m: int = 2) -> int:
        return m-n-1 if m>n else self.bitwiseComplement(n, 2*m)

class Solution:
    def bitwiseComplement(self, n: int) -> int:
        return~n+2**len(f'{n:b}')

test('''
1009. Complement of Base 10 Integer
Solved
Easy
Topics
premium lock icon
Companies
Hint
The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.

For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
Given an integer n, return its complement.

 

Example 1:

Input: n = 5
Output: 2
Explanation: 5 is "101" in binary, with complement "010" in binary, which is 2 in base-10.
Example 2:

Input: n = 7
Output: 0
Explanation: 7 is "111" in binary, with complement "000" in binary, which is 0 in base-10.
Example 3:

Input: n = 10
Output: 5
Explanation: 10 is "1010" in binary, with complement "0101" in binary, which is 5 in base-10.

Other examples:

Input: n = 0
Output: 1

Constraints:

0 <= n < 109
 

Note: This question is the same as 476: https://leetcode.com/problems/number-complement/

 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
320,879/529.2K
Acceptance Rate
60.6%
Topics
Junior
Bit Manipulation
Weekly Contest 128
icon
Companies
Hint 1
A binary number plus its complement will equal 111....111 in binary. Also, N = 0 is a corner case.
''')
