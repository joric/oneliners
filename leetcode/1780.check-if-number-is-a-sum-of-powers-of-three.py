from lc import *

# https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/solutions/?envType=daily-question&envId=2025-03-04

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        return all(2 - x % 3 for x in takewhile(lambda x:x, accumulate(repeat(n), lambda z,_: z//3)))

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        return all(2 - x % 3 for x in accumulate([n]*15, lambda z,_: z//3))

# https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/solutions/1118135/ruby-1-liner-short/?envType=daily-question&envId=2025-03-04

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        return False if n%3==2 else self.checkPowersOfThree(n//3) if n>3 else True

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        return next(n%3<1 for _ in[0]*n if n%3>1 or(n:=n//3)<1)

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        return n<1 or n%3<2 and self.checkPowersOfThree(n//3)

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        return'2'not in __import__('numpy').base_repr(n,3)

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        return(f:=lambda n:n<1 or n%3<2 and f(n//3))(n)

test('''
1780. Check if Number is a Sum of Powers of Three
Medium
Topics
Companies
Hint
Given an integer n, return true if it is possible to represent n as the sum of distinct powers of three. Otherwise, return false.

An integer y is a power of three if there exists an integer x such that y == 3x.

 

Example 1:

Input: n = 12
Output: true
Explanation: 12 = 31 + 32
Example 2:

Input: n = 91
Output: true
Explanation: 91 = 30 + 32 + 34
Example 3:

Input: n = 21
Output: false
 

Constraints:

1 <= n <= 107
Seen this question in a real interview before?
1/5
Yes
No
Accepted
47.8K
Submissions
69.7K
Acceptance Rate
68.6%
Topics
Math
Companies
Hint 1
Let's note that the maximum power of 3 you'll use in your soln is 3^16
Hint 2
The number can not be represented as a sum of powers of 3 if it's ternary presentation has a 2 in it
Similar Questions
Power of Three
Easy
''')
