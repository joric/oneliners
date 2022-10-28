from lc import *

class Solution1:
    def countPrimes(self, n: int) -> int:
        nums = [False, False] + [True] * (n - 2)
        for i in range(2, int(sqrt(n))+1):
            if nums[i]:
                for j in range(i*i, n, i):
                    nums[j] = False
        return sum(nums)

class Solution:
    def countPrimes(self, n: int) -> int:
        return sum(reduce(lambda a,i:([a.__setitem__(j,0) for j in range(i*i,n,i) if a[i]],a)[-1], range(2,int(sqrt(n))+1),[0,0]+[1]*(n-2)))

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