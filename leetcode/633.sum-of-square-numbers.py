from lc import *

# https://leetcode.com/problems/sum-of-square-numbers/discuss/1424957/Python-3-solutions%3A-Sqrt-HashSet-Two-Pointers-Clean-and-Concise-O(sqrt(c))

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        guess1 = 0
        n = 1
        while guess1 <= c/2:
            guess2 = c - guess1
            if (guess2**0.5)%1 == 0:
                return True
            guess1 += n
            n += 2
        return False

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for a in range(int(sqrt(c))+1):
            b = sqrt(c - a*a)
            if b == int(b):
                return True
        return False

# https://leetcode.com/problems/sum-of-square-numbers/discuss/104973/Python-Straightforward-with-Explanation

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        return any((b:=(c-a*a)**.5)==int(b)for a in range(isqrt(c)+1))

# https://leetcode.com/problems/sum-of-square-numbers/discuss/2991689/Python-oror-one-line

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        return any(sqrt(c-x*x)%1==0 for x in range(isqrt(c//2)+1))

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        return any(sqrt(c-x*x)%1==0 for x in range(isqrt(c)+1))

test('''
633. Sum of Square Numbers
Medium

2630

553

Add to List

Share
Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.

 

Example 1:

Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5
Example 2:

Input: c = 3
Output: false


Other examples:

Input: c = 8
Output: true

Input: c = 2
Output: true

Constraints:

0 <= c <= 231 - 1
Accepted
221,892
Submissions
641,540
''')