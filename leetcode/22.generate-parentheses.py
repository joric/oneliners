from lc import *

# https://leetcode.com/problems/generate-parentheses/submissions/

class Solution:
    def generateParenthesis(self, n):
        return(g:=lambda l,r:["("+s for s in g(l-1,r)]+[")"+s for s in g(l,r-1)]if r>=l>0else[")"*r]*(l==0))(n,n)

test('''
22. Generate Parentheses
Medium

21290

971

Add to List

Share
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8
Accepted
1,977,648
Submissions
2,622,505
''')
