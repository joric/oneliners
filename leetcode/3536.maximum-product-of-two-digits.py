from lc import *

# https://leetcode.com/problems/maximum-product-of-two-digits/solutions/7212093/one-line-beats-100-by-alphaglaze-gfwo/?envType=daily-question&envId=2026-07-25

class Solution:
    def maxProduct(self, n: int) -> int:
        return(d:=sorted(map(int,str(n))))and d[-1]*d[-2]

# https://leetcode.com/problems/maximum-product-of-two-digits/solutions/6713558/python-one-line-by-ante-fi2u/?envType=daily-question&envId=2026-07-25

class Solution:
    def maxProduct(self, n: int) -> int:
        return reduce(mul, map(int, sorted(str(n))[-2:]))

# https://leetcode.com/problems/maximum-product-of-two-digits/solutions/6715208/one-line-solution-by-xxxxkav-oeix/?envType=daily-question&envId=2026-07-25

class Solution:
    def maxProduct(self, n: int) -> int:
        return mul(*map(int,nlargest(2,str(n))))

test('''
3536. Maximum Product of Two Digits
Easy
Topics
premium lock icon
Companies
Hint
You are given a positive integer n.

Return the maximum product of any two digits in n.

Note: You may use the same digit twice if it appears more than once in n.

 

Example 1:

Input: n = 31

Output: 3

Explanation:

The digits of n are [3, 1].
The possible products of any two digits are: 3 * 1 = 3.
The maximum product is 3.
Example 2:

Input: n = 22

Output: 4

Explanation:

The digits of n are [2, 2].
The possible products of any two digits are: 2 * 2 = 4.
The maximum product is 4.
Example 3:

Input: n = 124

Output: 8

Explanation:

The digits of n are [1, 2, 4].
The possible products of any two digits are: 1 * 2 = 2, 1 * 4 = 4, 2 * 4 = 8.
The maximum product is 8.
 

Constraints:

10 <= n <= 109
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
52,866/76.3K
Acceptance Rate
69.3%
Topics
Mid Level
Math
Sorting
Weekly Contest 448
icon
Companies
Hint 1
Use brute force
''')
