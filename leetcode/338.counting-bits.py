from lc import *

class Solution:
    def countBits(self, n: int) -> List[int]:
        r=[0]*(n+1)
        for i in range(1,n+1):
            r[i] = r[i&(i-1)]+1
        return r

class Solution:
    def countBits(self, n: int) -> List[int]:
        r=[0]
        for i in range(1,n+1):
            r.append(r[i//2]+i%2)
        return r

class Solution:
    def countBits(self, n: int) -> List[int]:
        r=[0];[r.append(r[i//2]+i%2)for i in range(1,n+1)];return r

class Solution:
    def countBits(self, n: int) -> List[int]:
        return[bin(x).count('1')for x in range(n+1)]

class Solution:
    def countBits(self, n: int) -> List[int]:
        return map(int.bit_count,range(n+1)) # stopped working since Aug 2023 (expected return type integer[])

class Solution:
    def countBits(self, n: int) -> List[int]:
        return[x.bit_count()for x in range(n+1)]

test('''
338. Counting Bits
Easy

9374

448

Add to List

Share
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

 

Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
 

Constraints:

0 <= n <= 10^5
''')