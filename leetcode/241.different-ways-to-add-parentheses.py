from lc import *

# https://leetcode.com/problems/different-ways-to-add-parentheses/

class Solution:
    def diffWaysToCompute(self, s: str) -> List[int]:
        return [a+b if c == '+' else a-b if c == '-' else a*b
                for i, c in enumerate(s) if c in '+-*'
                for a in self.diffWaysToCompute(s[:i])
                for b in self.diffWaysToCompute(s[i+1:])] or [int(s)]

class Solution:
    def diffWaysToCompute(self, s: str) -> List[int]:
        return(f:=lambda s:[a+b if c=='+' else a-b if c=='-' else a*b for i,c in enumerate(s)if c in '+-*'for a in f(s[:i])for b in f(s[i+1:])]or[int(s)])(s)

class Solution:
    def diffWaysToCompute(self, s: str) -> List[int]:
        return(f:=lambda s:[{'+':a+b,'-':a-b}.get(c,a*b)for i,c in enumerate(s)if c in'+-*'for a in f(s[:i])for b in f(s[i+1:])]or[int(s)])(s)

test('''
241. Different Ways to Add Parentheses
Medium

5403

284

Add to List

Share
Given a string expression of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. You may return the answer in any order.

The test cases are generated such that the output values fit in a 32-bit integer and the number of different results does not exceed 104.

 

Example 1:

Input: expression = "2-1-1"
Output: [0,2]
Explanation:
((2-1)-1) = 0 
(2-(1-1)) = 2
Example 2:

Input: expression = "2*3-4*5"
Output: [-34,-14,-10,-10,10]
Explanation:
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10
 

Constraints:

1 <= expression.length <= 20
expression consists of digits and the operator '+', '-', and '*'.
All the integer values in the input expression are in the range [0, 99].
Accepted
228,772
Submissions
346,582
''', sort=True)
