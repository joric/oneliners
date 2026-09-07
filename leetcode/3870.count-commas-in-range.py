from lc import *

# https://leetcode.com/problems/count-commas-in-range/solutions/8297091/one-line-answer-by-pervzlo83s-y87m/?envType=daily-question&envId=2026-09-08

class Solution:
    def countCommas(self, n: int) -> int:
        return max(0,n-999)

test('''
3870. Count Commas in Range
Easy
Topics
premium lock icon
Companies
Hint
You are given an integer n.

Return the total number of commas used when writing all integers from [1, n] (inclusive) in standard number formatting.

In standard formatting:

A comma is inserted after every three digits from the right.
Numbers with fewer than 4 digits contain no commas.
 

Example 1:

Input: n = 1002

Output: 3

Explanation:

The numbers "1,000", "1,001", and "1,002" each contain one comma, giving a total of 3.

Example 2:

Input: n = 998

Output: 0

Explanation:

All numbers from 1 to 998 have fewer than four digits. Therefore, no commas are used.

 

Constraints:

1 <= n <= 105
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
62,106/89.5K
Acceptance Rate
69.4%
Topics
Mid Level
Math
Weekly Contest 493
icon
Companies
Hint 1
Numbers in the range [1000, 100000] have one comma.
''')
