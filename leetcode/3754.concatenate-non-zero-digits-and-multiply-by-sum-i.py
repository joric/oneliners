from lc import *

# https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-i/solutions/8373949/one-line-solution-by-mikposp-5s4j/?envType=daily-question&envId=2026-07-07

class Solution:
    def sumAndMultiply(self, n: int) -> int:
        return n and int(x:=str(n).replace('0',''))*sum(map(int,x))

class Solution:
    def sumAndMultiply(self, n: int) -> int:
        return int(x:=str(n).replace('0','')or'0')*sum(map(int,x))

test('''
3754. Concatenate Non-Zero Digits and Multiply by Sum I
Easy
Topics
premium lock icon
Companies
Hint
You are given an integer n.

Form a new integer x by concatenating all the non-zero digits of n in their original order. If there are no non-zero digits, x = 0.

Let sum be the sum of digits in x.

Return an integer representing the value of x * sum.

 

Example 1:

Input: n = 10203004

Output: 12340

Explanation:

The non-zero digits are 1, 2, 3, and 4. Thus, x = 1234.
The sum of digits is sum = 1 + 2 + 3 + 4 = 10.
Therefore, the answer is x * sum = 1234 * 10 = 12340.
Example 2:

Input: n = 1000

Output: 1

Explanation:

The non-zero digit is 1, so x = 1 and sum = 1.
Therefore, the answer is x * sum = 1 * 1 = 1.

Other examples:

Input: n = 0
Output: 0

Constraints:

0 <= n <= 109
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
42,553/75.9K
Acceptance Rate
56.1%
Topics
Mid Level
Math
Weekly Contest 477
icon
Companies
Hint 1
Simulate as described
''')
