from lc import *

# https://leetcode.com/problems/count-numbers-with-unique-digits/discuss/1619039/Python3-One-liner

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        return sum((i and 9 or 1)*reduce(mul,range(9,10-i,-1),1)for i in range(n+1))

# https://leetcode.com/problems/count-numbers-with-unique-digits/discuss/215482/Python-One-line-Solution

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        return 1+sum(9*reduce(mul,range(9,9-i+1,-1),1)for i in range(1,n+1))

# https://leetcode.com/problems/count-numbers-with-unique-digits/discuss/374777/Python-O(1)-99.80-math-with-explanation

class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        return n and(f:=lambda k:k!=max(10-n,0)and(1+f(k-1))*k)(9)*9+10or 1

# https://leetcode.com/problems/count-numbers-with-unique-digits/discuss/5068102/one-line-js-solution

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        return[1,10,91,739,5275,32491,168571,712891,2345851][n]

test('''
357. Count Numbers with Unique Digits
Medium

1515

1490

Add to List

Share
Given an integer n, return the count of all numbers with unique digits, x, where 0 <= x < 10n.

 

Example 1:

Input: n = 2
Output: 91
Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100, excluding 11,22,33,44,55,66,77,88,99
Example 2:

Input: n = 0
Output: 1
 

Constraints:

0 <= n <= 8
Accepted
140,323
Submissions
264,103
''')
