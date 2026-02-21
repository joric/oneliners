from lc import *

# https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/solutions/7594481/0ms-beats100-by-pankajgajpalla-r0cp/

class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        c=0
        for i in range(left,right+1):
            a=bin(i).count('1')
            if a in [2,3,5,7,11,13,17,19]:
                c+=1
        return c

class Solution:
    def countPrimeSetBits(self,l:int,r:int)->int:
        return sum(1<(k:=i.bit_count())and all(k%j for j in range(2,k))for i in range(l,r+1))

class Solution:
    def countPrimeSetBits(self,l:int,r:int)->int:
        return sum(map({2,3,5,7,11,13,17,19}.__contains__,map(int.bit_count,range(l,r+1))))

class Solution:
    def countPrimeSetBits(self, l: int, r: int) -> int:
        return sum([1 for i in range(l,r+1)if bin(i).count('1')in[2,3,5,7,11,13,17,19]])

class Solution:
    def countPrimeSetBits(self, l: int, r: int) -> int:
        return sum(map(lambda i:i.bit_count()in(2,3,5,7,11,13,17,19),range(l,r+1)))

class Solution:
    def countPrimeSetBits(self, l: int, r: int) -> int:
        return sum(i.bit_count()in{2,3,5,7,11,13,17,19}for i in range(l,r+1))

# https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/solutions/113232/665772-by-stefanpochmann-sli1/

class Solution:
    def countPrimeSetBits(self, l: int, r: int) -> int:
        return sum(665772>>i.bit_count()&1for i in range(l,r+1))

test('''
762. Prime Number of Set Bits in Binary Representation
Easy
Topics
premium lock icon
Companies
Hint
Given two integers left and right, return the count of numbers in the inclusive range [left, right] having a prime number of set bits in their binary representation.

Recall that the number of set bits an integer has is the number of 1's present when written in binary.

For example, 21 written in binary is 10101, which has 3 set bits.
 

Example 1:

Input: left = 6, right = 10
Output: 4
Explanation:
6  -> 110 (2 set bits, 2 is prime)
7  -> 111 (3 set bits, 3 is prime)
8  -> 1000 (1 set bit, 1 is not prime)
9  -> 1001 (2 set bits, 2 is prime)
10 -> 1010 (2 set bits, 2 is prime)
4 numbers have a prime number of set bits.
Example 2:

Input: left = 10, right = 15
Output: 5
Explanation:
10 -> 1010 (2 set bits, 2 is prime)
11 -> 1011 (3 set bits, 3 is prime)
12 -> 1100 (2 set bits, 2 is prime)
13 -> 1101 (3 set bits, 3 is prime)
14 -> 1110 (3 set bits, 3 is prime)
15 -> 1111 (4 set bits, 4 is not prime)
5 numbers have a prime number of set bits.
 

Constraints:

1 <= left <= right <= 106
0 <= right - left <= 104
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
136,257/188.2K
Acceptance Rate
72.4%
Topics
Junior
Math
Bit Manipulation
Weekly Contest 67
icon
Companies
Hint 1
Write a helper function to count the number of set bits in a number, then check whether the number of set bits is 2, 3, 5, 7, 11, 13, 17 or 19.
Similar Questions
Number of 1 Bits
Easy
''')
