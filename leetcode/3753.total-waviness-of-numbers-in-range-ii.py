from lc import *

# https://leetcode.com/problems/total-waviness-of-numbers-in-range-ii/solutions/7369013/python-digit-dp-by-ravinder_codes-ulzb/?envType=daily-question&envId=2026-06-05

class Solution:
    def totalWaviness(self, a: int, b: int) -> int:
        a = str(a)
        b = str(b)
        a = "0"*(len(b) - len(a)) + a
        @cache
        def d(i, n, t, c, p, q, v):
            if i == len(a): 
                return v
            r = 0
            l = int(b[i]) if t else 9
            s = 0 if not c else int(a[i])
            n = n or q > 0
            for j in range(s, l + 1):
                u = t and j == int(b[i])
                w = c and j == int(a[i])
                e = 0
                if (q != -1 or p == -1) and n:
                    e = 1 if j > p < q or j < p > q else 0
                r += d(i + 1, n, u, w, j, p, v + e)
            return r
        return d(0, 0, 1, 1, -1, -1, 0)

class Solution:
    def totalWaviness(self, a: int, b: int) -> int:
        a=str(a).zfill(k:=len(b:=str(b)));return(f:=cache(lambda i,n,t,c,p,q,v:i<k and(l:=[9,int(b[i])][t],s:=c*int(a[i]),n:=n or q>0)and sum(f(i+1,n,t*j==l,c*(j==s),j,p,v+(n*(j-p)*(q-p)>0<=q))for j in range(s,l+1))or v))(0,0,1,1,-1,-1,0)

class Solution:
    def totalWaviness(self, a: int, b: int) -> int:
        a=str(a).zfill(k:=len(b:=str(b)));return(d:=cache(lambda i,n,t,c,p,q,v:i<k and(lambda s,l,m:sum(d(i+1,m,t*j==l,c*(j==s),j,p,v+(m*(j-p)*(q-p)>0<=q))for j in range(s,l+1)))(c*int(a[i]),[9,int(b[i])][t],n|q>0)or v))(0,0,1,1,-1,-1,0)

test('''
3753. Total Waviness of Numbers in Range II
Hard
Topics
premium lock icon
Companies
Hint
You are given two integers num1 and num2 representing an inclusive range [num1, num2].

The waviness of a number is defined as the total count of its peaks and valleys:

A digit is a peak if it is strictly greater than both of its immediate neighbors.
A digit is a valley if it is strictly less than both of its immediate neighbors.
The first and last digits of a number cannot be peaks or valleys.
Any number with fewer than 3 digits has a waviness of 0.
Return the total sum of waviness for all numbers in the range [num1, num2].
 

Example 1:

Input: num1 = 120, num2 = 130

Output: 3

Explanation:

In the range [120, 130]:

120: middle digit 2 is a peak, waviness = 1.
121: middle digit 2 is a peak, waviness = 1.
130: middle digit 3 is a peak, waviness = 1.
All other numbers in the range have a waviness of 0.
Thus, total waviness is 1 + 1 + 1 = 3.

Example 2:

Input: num1 = 198, num2 = 202

Output: 3

Explanation:

In the range [198, 202]:

198: middle digit 9 is a peak, waviness = 1.
201: middle digit 0 is a valley, waviness = 1.
202: middle digit 0 is a valley, waviness = 1.
All other numbers in the range have a waviness of 0.
Thus, total waviness is 1 + 1 + 1 = 3.

Example 3:

Input: num1 = 4848, num2 = 4848

Output: 2

Explanation:

Number 4848: the second digit 8 is a peak, and the third digit 4 is a valley, giving a waviness of 2.

 

Constraints:

1 <= num1 <= num2 <= 1015​​​​​​​
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
5,060/17.9K
Acceptance Rate
28.2%
Topics
Senior Staff
Math
Dynamic Programming
Biweekly Contest 170
icon
Companies
Hint 1
Use digit dynamic programming
Hint 2
Build a digit-DP state (position, tight, lastDigit, secondLastDigit)
''')
