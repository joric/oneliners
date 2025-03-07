from lc import *

# https://leetcode.com/problems/closest-prime-numbers-in-range/solutions/2982421/python-3-8-lines-w-example-xx/?envType=daily-question&envId=2025-03-07

class Solution:
    def closestPrimes(self, a: int, b: int) -> List[int]:
        s = [0,0]+[1]*b
        [setitem(s,j,0)for i in range(2,isqrt(b)+1)for j in range(i*i,b+1,i)]
        p = [i for i,p in enumerate(s)if p and a<=i<=b]
        return min(zip(p,p[1:]),key=lambda x:x[1]-x[0],default=[-1,-1])

class Solution:
    def closestPrimes(self, a: int, b: int) -> list[int]:
        s=[0,0]+[1]*(n:=b+1)
        any(setitem(s,slice(i*i,n,i),[0]*len(s[i*i:n:i]))for i in range(2,isqrt(n)+1))
        p=sorted(i for i,x in enumerate(s)if x and a<=i<=b)
        return min(zip(p,p[1:]),key=lambda x:x[1]-x[0],default=[-1,-1])

# https://leetcode.com/problems/closest-prime-numbers-in-range/solutions/2979147/python-twin-primes-no-sieve/?envType=daily-question&envId=2025-03-07

class Solution:
    def closestPrimes(self, a: int, b: int) -> list[int]:
        p = []
        for x in range(max(2,a),b+1):
            if all(x%i for i in range(2,isqrt(x)+1)):
                p.append(x)
                if p[2:]and p[-1]<=p[-2]+2:
                    break
        return min(zip(p,p[1:]),key=lambda x:x[1]-x[0],default=[-1,-1])

# 13 ms
class Solution:
    def closestPrimes(self, a: int, b: int) -> list[int]:
        p=[];any(all(x%i for i in range(2,isqrt(x)+1))and[p.append(x)]and p[2:]and p[-1]<=2+p[-2]for x in range(max(2,a),b+1));return min(zip(p,p[1:]),key=lambda x:x[1]-x[0],default=[-1,-1])

# 5000 ms (isqrt(x)+1 replaced with x)
class Solution:
    def closestPrimes(self, a: int, b: int) -> list[int]:
        p,t=[],-1;any(all(x%i for i in range(2,x))and[p.append(x)]and t+3>(t:=x)for x in range(max(2,a),b+1));return min(zip(p,p[1:]),key=lambda x:x[1]-x[0],default=[-1,-1])

test('''
2523. Closest Prime Numbers in Range
Medium
Topics
Companies
Hint
Given two positive integers left and right, find the two integers num1 and num2 such that:

left <= num1 < num2 <= right .
Both num1 and num2 are prime numbers.
num2 - num1 is the minimum amongst all other pairs satisfying the above conditions.
Return the positive integer array ans = [num1, num2]. If there are multiple pairs satisfying these conditions, return the one with the smallest num1 value. If no such numbers exist, return [-1, -1].

 

Example 1:

Input: left = 10, right = 19
Output: [11,13]
Explanation: The prime numbers between 10 and 19 are 11, 13, 17, and 19.
The closest gap between any pair is 2, which can be achieved by [11,13] or [17,19].
Since 11 is smaller than 17, we return the first pair.
Example 2:

Input: left = 4, right = 6
Output: [-1,-1]
Explanation: There exists only one prime number in the given range, so the conditions cannot be satisfied.
 

Other examples:

Input: left = 19, right = 31
Output: [29, 31]

Input: left = 1087, right = 4441
Output: [1091,1093]

Input: left = 1, right = 1000000
Output: [2,3]

Constraints:

1 <= left <= right <= 106
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
28.8K
Submissions
72.9K
Acceptance Rate
39.5%
Topics
Math
Number Theory
Companies
Hint 1
Use Sieve of Eratosthenes to mark numbers that are primes.
Hint 2
Iterate from right to left and find pair with the minimum distance between marked numbers.
Similar Questions
Count Ways to Make Array With Product
Hard
''')
