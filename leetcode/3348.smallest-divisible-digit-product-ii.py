from lc import *

# https://leetcode.com/problems/smallest-divisible-digit-product-ii/solutions/6028394/python-brute-force-by-awice-v5qx/?envType=daily-question&envId=2026-08-07

def fill(req, length):
    # smallest zf atleast this length divisible by req
    ans = []
    for d in range(9, 1, -1):
        while req % d == 0:
            ans.append(d)
            req //= d
    
    ans.extend([1] * max(0, length - len(ans)))
    return "".join(map(str, reversed(ans)))

class Solution:
    def smallestNumber(self, S: str, T: int) -> str:
        N = len(S)
        t = T
        for p in [2, 3, 5, 7]:
            while t % p == 0:
                t //= p
        if t != 1:
            return "-1"

        P = [T] * (N + 1)
        for i, x in enumerate(map(int, S)):
            if x == 0: break
            P[i + 1] = P[i] // gcd(P[i], x)
        if P[-1] == 1:
            return S

        zero = S.find("0") % N
        for i in range(zero, -1, -1):
            req = P[i]
            digits = N - 1 - i
            for d in range(int(S[i]) + 1, 10):
                ending = fill(req // gcd(req, d), digits)
                if len(ending) <= digits:
                    return S[:i] + str(d) + ending

        return fill(T, len(S) + 1)

class Solution:
    def smallestNumber(self, n: str, t: int) -> str:
        c=len(n);f=lambda x,y,z=9:'1'*y if z<2 else f(x,y,z-1)if x%z else f(x//z,y-1,z)+str(z);h=[t];[h.append(h[-1]//gcd(h[-1],int(x)))for x in n.split('0')[0]];return'-1'if prod(map(int,f(t,0)or'1'))!=t else n if len(h)>c and h[-1]==1 else next((n[:i]+str(j)+k for i in range(n.find('0')%c,-1,-1)for j in range(int(n[i])+1,10)if len(k:=f(h[i]//gcd(h[i],j),c-i-1))==c-i-1),f(t,c+1))

test('''
3348. Smallest Divisible Digit Product II
Hard
Topics
premium lock icon
Companies
Hint
You are given a string num which represents a positive integer, and an integer t.

A number is called zero-free if none of its digits are 0.

Return a string representing the smallest zero-free number greater than or equal to num such that the product of its digits is divisible by t. If no such number exists, return "-1".

 

Example 1:

Input: num = "1234", t = 256

Output: "1488"

Explanation:

The smallest zero-free number that is greater than 1234 and has the product of its digits divisible by 256 is 1488, with the product of its digits equal to 256.

Example 2:

Input: num = "12355", t = 50

Output: "12355"

Explanation:

12355 is already zero-free and has the product of its digits divisible by 50, with the product of its digits equal to 150.

Example 3:

Input: num = "11111", t = 26

Output: "-1"

Explanation:

No number greater than 11111 has the product of its digits divisible by 26.

 

Constraints:

2 <= num.length <= 2 * 105
num consists only of digits in the range ['0', '9'].
num does not contain leading zeros.
1 <= t <= 1014
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
5,446/34.9K
Acceptance Rate
15.6%
Topics
Principal
Math
String
Backtracking
Greedy
Number Theory
Biweekly Contest 143
icon
Companies
Hint 1
t should only have 2, 3, 5 and 7 as prime factors.
Hint 2
Find the shortest suffix that must be changed.
Hint 3
Try to form the string greedily.
Similar Questions
Smallest Number With Given Digit Product
Medium
''')
