from lc import *

# https://leetcode.com/problems/generate-parentheses/submissions/

class Solution:
    def generateParenthesis(self, n):
        return(g:=lambda l,r:["("+s for s in g(l-1,r)]+[")"+s for s in g(l,r-1)]if r>=l>0else[")"*r]*(l==0))(n,n)

# https://leetcode.com/problems/generate-parentheses/solutions/5047546/one-line-solution-by-mikposp-od1x/?envType=daily-question&envId=2026-10-02

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return (f:=lambda p,l,r:l==r==n and [p] or r<=l<=n and f(p+'(',l+1,r)+f(p+')',l,r+1) or [])('',0,0)

# https://leetcode.com/problems/generate-parentheses/solutions/10273/one-line-python-solution-by-cgsv-bg5a/?envType=daily-question&envId=2026-10-02

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return ['('+litem+')' + ritem for i in range(n) for litem in self.generateParenthesis(i) for ritem in self.generateParenthesis(n-1-i)] or ['']

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return(f:=lambda n:[f'({l}){r}'for i in range(n)for l in f(i)for r in f(~i+n)]or[''])(n)

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        s={''};[s:={x[:i]+'()'+x[i:]for x in s for i in range(len(x)+1)}for _ in[0]*n];return[*s]

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        s={''};[s:={x[:i]+'()'+x[i:]for x in s for i in range(99)}for _ in[0]*n];return[*s]

# POTD 2026-10-03

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return[*eval('{x[:i]+"()"+x[i:]for x in'*n+"{''}"+'for i in range(99)}'*n)]

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
''',sort=True)
