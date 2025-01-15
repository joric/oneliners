from lc import *

# https://leetcode.com/problems/minimize-xor/description/?envType=daily-question&envId=2025-01-15

class Solution:
    def minimizeXor(self, a: int, b: int) -> int:
        if a.bit_length() <= (target := b.bit_count()):
            return 2 ** target - 1
        if target < (source := a.bit_count()):
            return int(bin(a)[2:][::-1].replace("1", "0", source-target)[::-1], 2)
        if target > source:
            return int(bin(a)[2:][::-1].replace("0", "1", target-source)[::-1], 2)
        return a

class Solution:
    def minimizeXor(self, a: int, b: int) -> int:
        return 2**x-1 if a.bit_length()<=(x:=b.bit_count())else int(bin(a)[2:][::-1].replace(*('10' if (d:=a.bit_count()-x)>0 else '01'),abs(d))[::-1],2)

class Solution:
    def minimizeXor(self, a: int, b: int) -> int:
        return 2**x-1 if a.bit_length()<=(x:=b.bit_count())else int(bin(a)[2:][::-1].replace(*('01','10')[(d:=a.bit_count()-x)>0],abs(d))[::-1],2)

class Solution:
    def minimizeXor(self, x: int, y: int) -> int:
        b=int.bit_count;x=(x,~x)[(d:=b(x)-b(y))<0];[x:=x&x-1for _ in range(abs(d))];return(x,~x)[d<0]

test('''
2429. Minimize XOR
Medium
Topics
Companies
Hint
Given two positive integers num1 and num2, find the positive integer x such that:

x has the same number of set bits as num2, and
The value x XOR num1 is minimal.
Note that XOR is the bitwise XOR operation.

Return the integer x. The test cases are generated such that x is uniquely determined.

The number of set bits of an integer is the number of 1's in its binary representation.

 

Example 1:

Input: num1 = 3, num2 = 5
Output: 3
Explanation:
The binary representations of num1 and num2 are 0011 and 0101, respectively.
The integer 3 has the same number of set bits as num2, and the value 3 XOR 3 = 0 is minimal.
Example 2:

Input: num1 = 1, num2 = 12
Output: 3
Explanation:
The binary representations of num1 and num2 are 0001 and 1100, respectively.
The integer 3 has the same number of set bits as num2, and the value 3 XOR 1 = 2 is minimal.
 

Constraints:

1 <= num1, num2 <= 109
''')
