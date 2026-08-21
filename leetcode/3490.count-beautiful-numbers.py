from lc import *

# https://leetcode.com/problems/count-beautiful-numbers/solutions/6718405/easy-4-line-dp-solution-by-9349394-2t68/

class Solution:
    def beautifulNumbers(self, l: int, r: int) -> int:
        @cache
        def f(num,idx,isLess,p,s,notZero):
            if idx == -1:return (1 if notZero and p%s == 0 and isLess else 0)
            return (1 if notZero and p%s == 0 else 0) + sum([f(num,idx-1,nd < int(num[idx]) if nd != int(num[idx]) else isLess ,p*nd,s+nd,nd!=0) for nd in range(10)])
        return f(str(r),len(str(r))-1,True,1,0,None) - f(str(l-1),len(str(l-1))-1,True,1,0,None)

class Solution:
    def beautifulNumbers(self, l: int, r: int) -> int:
        f=cache(lambda n,b=1,p=1,s=0,c=0:n and c+sum(f(n//10,(d<n%10,b)[d==n%10],p*d,s+d,d and p*d%(s+d)<1)for d in range(10))or c*b);return f(r)-f(l-1)

test('''
3490. Count Beautiful Numbers
Hard
Topics
premium lock icon
Companies
Hint
You are given two positive integers, l and r. A positive integer is called beautiful if the product of its digits is divisible by the sum of its digits.

Return the count of beautiful numbers between l and r, inclusive.

 

Example 1:

Input: l = 10, r = 20

Output: 2

Explanation:

The beautiful numbers in the range are 10 and 20.

Example 2:

Input: l = 1, r = 15

Output: 10

Explanation:

The beautiful numbers in the range are 1, 2, 3, 4, 5, 6, 7, 8, 9, and 10.

 

Constraints:

1 <= l <= r < 109
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
6,105/25.2K
Acceptance Rate
24.2%
Topics
Senior Staff
Dynamic Programming
Weekly Contest 441
icon
Companies
Hint 1
Use digit dynamic programming.
''')
