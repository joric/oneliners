from lc import *

# https://leetcode.com/problems/parsing-a-boolean-expression/discuss/323307/Python-Easy-1-line-Cheat

class Solution:
    def parseBoolExpr(self, s: str) -> bool:
        return eval([s:=s.replace(x,y)for x,y in{'t':'True','f':'False','!':'not |','&(':'all([','|(':'any([',')':'])'}.items()]and s)

class Solution:
    def parseBoolExpr(self, s: str) -> bool:
        return eval(reduce(lambda s,k:s.replace(k,d[k]),d:={'t':'True','f':'False','!':'not |','&(':'all([','|(':'any([',')':'])'},s))

class Solution:
    def parseBoolExpr(self, s: str) -> bool:
        d={'t':'True','f':'False','!':'not |','&(':'all([','|(':'any([',')':'])'};return eval([s:=s.replace(k,d[k])for k in d]and s)

test('''
1106. Parsing A Boolean Expression
Hard

1217

63

Add to List

Share
A boolean expression is an expression that evaluates to either true or false. It can be in one of the following shapes:

't' that evaluates to true.
'f' that evaluates to false.
'!(subExpr)' that evaluates to the logical NOT of the inner expression subExpr.
'&(subExpr1, subExpr2, ..., subExprn)' that evaluates to the logical AND of the inner expressions subExpr1, subExpr2, ..., subExprn where n >= 1.
'|(subExpr1, subExpr2, ..., subExprn)' that evaluates to the logical OR of the inner expressions subExpr1, subExpr2, ..., subExprn where n >= 1.
Given a string expression that represents a boolean expression, return the evaluation of that expression.

It is guaranteed that the given expression is valid and follows the given rules.

 

Example 1:

Input: expression = "&(|(f))"
Output: false
Explanation: 
First, evaluate |(f) --> f. The expression is now "&(f)".
Then, evaluate &(f) --> f. The expression is now "f".
Finally, return false.
Example 2:

Input: expression = "|(f,f,f,t)"
Output: true
Explanation: The evaluation of (false OR false OR false OR true) is true.
Example 3:

Input: expression = "!(&(f,t))"
Output: true
Explanation: 
First, evaluate &(f,t) --> (false AND true) --> false --> f. The expression is now "!(f)".
Then, evaluate !(f) --> NOT false --> true. We return true.
 

Constraints:

1 <= expression.length <= 2 * 104
expression[i] is one following characters: '(', ')', '&', '|', '!', 't', 'f', and ','.
Accepted
35,389
Submissions
58,983
''')
