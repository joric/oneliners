from lc import *

# https://leetcode.com/problems/count-square-sum-triples/solutions/7388165/one-line-solution-by-mikposp-ojy5/?envType=daily-question&envId=2025-12-08

class Solution:
    def countTriples(self, n: int) -> int:
        return sum(a*a+b*b==c*c for a,b,c in combinations(range(n+1),3))*2

test('''
1925. Count Square Sum Triples
Solved
Easy
Topics
premium lock icon
Companies
Hint
A square triple (a,b,c) is a triple where a, b, and c are integers and a2 + b2 = c2.

Given an integer n, return the number of square triples such that 1 <= a, b, c <= n.

 

Example 1:

Input: n = 5
Output: 2
Explanation: The square triples are (3,4,5) and (4,3,5).
Example 2:

Input: n = 10
Output: 4
Explanation: The square triples are (3,4,5), (4,3,5), (6,8,10), and (8,6,10).
 

Constraints:

1 <= n <= 250
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
61,305/88K
Acceptance Rate
69.7%
Topics
Math
Enumeration
Biweekly Contest 56
icon
Companies
Hint 1
Iterate over all possible pairs (a,b) and check that the square root of a * a + b * b is an integers less than or equal n
Hint 2
You can check that the square root of an integer is an integer using binary seach or a builtin function like sqrt
Similar Questions
Number of Unequal Triplets in Array
Easy
''')
