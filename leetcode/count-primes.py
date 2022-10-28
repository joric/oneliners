from lc import *

class Solution:
    def countPrimes(self, n):
        a = [0,0]+[1]*(n-2)
        for i in range(2,int(n**0.5)+1):
            if a[i]:
                a[i*i:n:i] = [0]*len(a[i*i:n:i])
        return sum(a)

test('''
204. Count Primes
Medium

5809

1131

Add to List

Share
Given an integer n, return the number of prime numbers that are strictly less than n.

 

Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
Example 2:

Input: n = 0
Output: 0
Example 3:

Input: n = 1
Output: 0
 

Constraints:

0 <= n <= 5 * 106
''')