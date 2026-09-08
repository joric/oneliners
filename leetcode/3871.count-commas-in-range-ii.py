from lc import *

# https://leetcode.com/problems/count-commas-in-range-ii/solutions/7655779/one-liner-o1-solution-python3-by-smrespo-7al6/?envType=daily-question&envId=2026-09-09

class Solution:
    def countCommas(self, n: int) -> int:
        return (n - 999) * int(n > 999) + (n - 999999) * int(n > 999999) + (n - 999999999) * int(n > 999999999)+ (n - 999999999999) * int(n > 999999999999) + (n - 999999999999999) * int(n > 999999999999999)

class Solution:
    def countCommas(self, n: int) -> int:
        return sum(max(0,n-1000**i+1)for i in range(1,6))

test('''
3871. Count Commas in Range II
Medium
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

​​​​​​​All numbers from 1 to 998 have fewer than four digits. Therefore, no commas are used.

 

Constraints:

1 <= n <= 1015
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
45,199/109.3K
Acceptance Rate
41.4%
Topics
Senior
Math
Weekly Contest 493
icon
Companies
Hint 1
Count the numbers in each comma group (1-3 digits, 4-6 digits, 7-9 digits, ...) and multiply by how many commas each number in that group has.
''')
