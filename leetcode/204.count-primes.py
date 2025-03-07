from lc import *

# based on this https://stackoverflow.com/questions/10639861/python-prime-generator-in-one-line
# also see https://blog.finxter.com/10-python-one-liners/

# MLE
class Solution:
    def countPrimes(self, n: int) -> int:
        g=range(2,n);return len(reduce(lambda r,x:r-set(range(x**2,n,x))if x in r else r,g,set(g)))

# https://leetcode.com/problems/count-primes/discuss/111420/Python3-solution-using-Sieve-of-Eratosthenes-time-is-O(n)

class Solution:
    def countPrimes(self, n: int) -> int:
        s = [0,0]+[1]*(n-2)
        for i in range(2,int(n**0.5)+1):
            if s[i]:
                s[i*i:n:i] = [0]*len(s[i*i:n:i])
        return sum(s)

class Solution:
    def countPrimes(self, n: int) -> int:
        return sum(reduce(lambda s,i:setitem(s,slice(i*i,n,i),[0]*len(s[i*i:n:i]))or s,range(2,isqrt(n)+1),[0,0]+[1]*(n-2)))

class Solution:
    def countPrimes(self, n: int) -> int:
        s=[0,0]+[1]*(n-2);[setitem(s,j,0)for i in range(2,isqrt(n)+1)for j in range(i*i,n,i)];return sum(s)

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