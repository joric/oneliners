from lc import *

# https://leetcode.com/problems/next-greater-numerically-balanced-number/solutions/7295574/one-line-solution/?envType=daily-question&envId=2025-10-24

class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        q = [1,22,122,333,1333,4444,14444,22333,55555,122333,155555,224444,666666,1224444]
        return next(v for v in sorted(int(''.join(p)) for s in map(str,q)
            for p in permutations(s)) if v>n)

class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        return next(v for v in count(n+1)if all(starmap(eq,Counter(map(int,str(v))).items())))

test('''
2048. Next Greater Numerically Balanced Number
Solved
Medium
Topics
premium lock icon
Companies
Hint
An integer x is numerically balanced if for every digit d in the number x, there are exactly d occurrences of that digit in x.

Given an integer n, return the smallest numerically balanced number strictly greater than n.

 

Example 1:

Input: n = 1
Output: 22
Explanation: 
22 is numerically balanced since:
- The digit 2 occurs 2 times. 
It is also the smallest numerically balanced number strictly greater than 1.
Example 2:

Input: n = 1000
Output: 1333
Explanation: 
1333 is numerically balanced since:
- The digit 1 occurs 1 time.
- The digit 3 occurs 3 times. 
It is also the smallest numerically balanced number strictly greater than 1000.
Note that 1022 cannot be the answer because 0 appeared more than 0 times.
Example 3:

Input: n = 3000
Output: 3133
Explanation: 
3133 is numerically balanced since:
- The digit 1 occurs 1 time.
- The digit 3 occurs 3 times.
It is also the smallest numerically balanced number strictly greater than 3000.
 

Constraints:

0 <= n <= 106
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
38,856/67.2K
Acceptance Rate
57.8%
Topics
Hash Table
Math
Backtracking
Counting
Enumeration
Weekly Contest 264
icon
Companies
Hint 1
How far away can the next greater numerically balanced number be from n?
Hint 2
With the given constraints, what is the largest numerically balanced number?
Similar Questions
Find the Width of Columns of a Grid
Easy
''')
