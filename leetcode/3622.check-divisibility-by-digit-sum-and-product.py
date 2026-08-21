from lc import *

# https://leetcode.com/problems/check-divisibility-by-digit-sum-and-product/solutions/8462311/one-line-solution-by-mikposp-enlf/?envType=daily-question&envId=2026-08-22

class Solution:
    def checkDivisibility(self, n: int) -> bool:
        return n%(sum(q:=[*map(int,str(n))])+prod(q))<1

test('''
3622. Check Divisibility by Digit Sum and Product
Easy
Topics
premium lock icon
Companies
Hint
You are given a positive integer n. Determine whether n is divisible by the sum of the following two values:

The digit sum of n (the sum of its digits).

The digit product of n (the product of its digits).

Return true if n is divisible by this sum; otherwise, return false.

 

Example 1:

Input: n = 99

Output: true

Explanation:

Since 99 is divisible by the sum (9 + 9 = 18) plus product (9 * 9 = 81) of its digits (total 99), the output is true.

Example 2:

Input: n = 23

Output: false

Explanation:

Since 23 is not divisible by the sum (2 + 3 = 5) plus product (2 * 3 = 6) of its digits (total 11), the output is false.

 

Constraints:

1 <= n <= 106
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
77,282/111K
Acceptance Rate
69.6%
Topics
Mid Level
Math
Weekly Contest 459
icon
Companies
Hint 1
Compute the digits' sum and product, then check if n % (sum + product) == 0.
''')
