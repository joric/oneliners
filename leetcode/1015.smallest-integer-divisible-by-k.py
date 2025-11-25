from lc import *

# https://leetcode.com/problems/smallest-integer-divisible-by-k/solutions/1656261/python3-one-liner-by-pknoe3lh-ihtx/?envType=daily-question&envId=2025-11-25

class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
         return min((i+1 for i,r in enumerate(accumulate(range(1,k+3),lambda a,b: (a*10+1)%k)) if r%k == 0),default=-1)


# https://leetcode.com/problems/smallest-integer-divisible-by-k/solutions/1657500/python3-performant-and-streamlined-codep-ik54/?envType=daily-question&envId=2025-11-25

class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if math.gcd(k,10) != 1: return -1 # intuitative after some observation: any number divisable by 2 or 5 will never be a divisor of preunit.
        reminder = 0
        for length in range(1, k+1):
            if (reminder := (1+reminder*10) % k) == 0: return length
        # return -1 # with some recreational math knowledge, this line is actually unnecessary.

class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        r=0;return-1 if 1!=gcd(k,10)else next(n for n in range(1,k+1)if(r:=(r*10+1)%k)<1)

class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        r=0;return next((n for n in range(1,k+1)if(r:=(r*10+1)%k)<1),-1)

class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        n=0;return-next((~i for i in range(k)if(n:=n*10+1)%k<1),1)

test('''
1015. Smallest Integer Divisible by K
Solved
Medium
Topics
premium lock icon
Companies
Hint
Given a positive integer k, you need to find the length of the smallest positive integer n such that n is divisible by k, and n only contains the digit 1.

Return the length of n. If there is no such n, return -1.

Note: n may not fit in a 64-bit signed integer.

 

Example 1:

Input: k = 1
Output: 1
Explanation: The smallest answer is n = 1, which has length 1.
Example 2:

Input: k = 2
Output: -1
Explanation: There is no such positive integer n divisible by 2.
Example 3:

Input: k = 3
Output: 3
Explanation: The smallest answer is n = 111, which has length 3.
 

Constraints:

1 <= k <= 105
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
71,227/152.3K
Acceptance Rate
46.8%
Topics
Hash Table
Math
Weekly Contest 129
icon
Companies
Hint 1
11111 = 1111 * 10 + 1 We only need to store remainders modulo K.
Hint 2
If we never get a remainder of 0, why would that happen, and how would we know that?
''')
