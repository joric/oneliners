from lc import *

# https://leetcode.com/problems/powerful-integers/solutions/1184334/python-3-todays-one-liner-by-l1ne-vbzg/

class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        powers = lambda p: takewhile(lambda a: a<bound, accumulate(repeat(p), mul, initial=1)) if p > 1 else [1]
        return set(a+b for a,b in product(powers(x), powers(y)) if a+b <= bound)

class Solution:
    def powerfulIntegers(self, x: int, y: int, c: int) -> List[int]:
        f=lambda p:p>1 and takewhile(lambda a:a<c, accumulate(repeat(p),mul,initial=1))or[1];return set(a+b for a,b in product(f(x),f(y))if a+b<=c)

class Solution:
    def powerfulIntegers(self, x: int, y: int, c: int) -> List[int]:
        f=lambda p:p>1and takewhile(c.__gt__,accumulate(repeat(p),mul,initial=1))or[1];return{a+b for a,b in product(f(x),f(y))if a+b<=c}

test('''
970. Powerful Integers
Solved
Medium
Topics
premium lock icon
Companies
Given three integers x, y, and bound, return a list of all the powerful integers that have a value less than or equal to bound.

An integer is powerful if it can be represented as xi + yj for some integers i >= 0 and j >= 0.

You may return the answer in any order. In your answer, each value should occur at most once.

 

Example 1:

Input: x = 2, y = 3, bound = 10
Output: [2,3,4,5,7,9,10]
Explanation:
2 = 20 + 30
3 = 21 + 30
4 = 20 + 31
5 = 21 + 31
7 = 22 + 31
9 = 23 + 30
10 = 20 + 32
Example 2:

Input: x = 3, y = 5, bound = 15
Output: [2,4,6,8,10,14]
 

Constraints:

1 <= x, y <= 100
0 <= bound <= 106
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
63,280/142.3K
Acceptance Rate
44.5%
Topics
Mid Level
Hash Table
Math
Enumeration
Weekly Contest 118
icon
Companies
Similar Questions
Count the Number of Powerful Integers
Hard
''')
