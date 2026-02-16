from lc import *

# https://leetcode.com/problems/reverse-bits/solutions/6342241/one-line-solution-by-minh_hung-6zfa/?envType=daily-question&envId=2026-02-16

class Solution:
    def reverseBits(self, n: int) -> int:
        res = n
        res = (res >> 16) | (res << 16) & 0xFFFFFFFF
        res = ((res & 0xff00ff00) >> 8) | ((res & 0x00ff00ff) << 8)
        res = ((res & 0xf0f0f0f0) >> 4) | ((res & 0x0f0f0f0f) << 4)
        res = ((res & 0xcccccccc) >> 2) | ((res & 0x33333333) << 2)
        res = ((res & 0xaaaaaaaa) >> 1) | ((res & 0x55555555) << 1)
        return res & 0xFFFFFFFF

# https://leetcode.com/problems/reverse-bits/solutions/5009425/one-line-solution-by-mikposp-11sv/?envType=daily-question&envId=2026-02-16

class Solution:
    def reverseBits(self, n: int) -> int:
        return sum((n>>i&1)<<(31-i)for i in range(32))

class Solution:
    def reverseBits(self, n: int) -> int:
        return int(bin(n)[2:].zfill(32)[::-1],2)

class Solution:
    def reverseBits(self, n: int) -> int:
        return int(f'{n:032b}'[::-1],2)

test('''
190. Reverse Bits
Solved
Easy
Topics
premium lock icon
Companies
Reverse bits of a given 32 bits signed integer.

 

Example 1:

Input: n = 43261596

Output: 964176192

Explanation:

Integer Binary
43261596    00000010100101000001111010011100
964176192   00111001011110000010100101000000
Example 2:

Input: n = 2147483644

Output: 1073741822

Explanation:

Integer Binary
2147483644  01111111111111111111111111111100
1073741822  00111111111111111111111111111110
 

Constraints:

0 <= n <= 231 - 2
n is even.
 

Follow up: If this function is called many times, how would you optimize it?

 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
1,184,552/1.8M
Acceptance Rate
66.0%
Topics
Divide and Conquer
Bit Manipulation
icon
Companies
Similar Questions
Reverse Integer
Medium
Number of 1 Bits
Easy
A Number After a Double Reversal
Easy
''')
