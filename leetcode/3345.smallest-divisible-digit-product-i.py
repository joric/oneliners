from lc import *

# https://leetcode.com/problems/smallest-divisible-digit-product-i/solutions/8441710/one-line-solution-by-mikposp-7crq/?envType=daily-question&envId=2026-08-06

class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        return next(v for v in count(n)if prod(map(int,str(v)))%t<1)

test('''
3345. Smallest Divisible Digit Product I
Easy
Topics
premium lock icon
Companies
Hint
You are given two integers n and t. Return the smallest number greater than or equal to n such that the product of its digits is divisible by t.

 

Example 1:

Input: n = 10, t = 2

Output: 10

Explanation:

The digit product of 10 is 0, which is divisible by 2, making it the smallest number greater than or equal to 10 that satisfies the condition.

Example 2:

Input: n = 15, t = 3

Output: 16

Explanation:

The digit product of 16 is 6, which is divisible by 3, making it the smallest number greater than or equal to 15 that satisfies the condition.

 

Constraints:

1 <= n <= 100
1 <= t <= 10
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
41,137/63.6K
Acceptance Rate
64.7%
Topics
Mid Level
Math
Enumeration
Biweekly Contest 143
icon
Companies
Hint 1
You have to check at most 10 numbers.
Hint 2
Apply a brute-force approach by checking each possible number.
Similar Questions
Smallest Number With Given Digit Product
Medium
''')
