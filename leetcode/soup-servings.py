from lc import *

# https://leetcode.com/problems/soup-servings/discuss/121711/C%2B%2BJavaPython-When-N-greater-4800-just-return-1

class Solution:
    def soupServings(self, n: int) -> float:
        f=cache(lambda a,b:0.5 if a<=0 and b<=0 else 1 if a<=0 else 0 if b<=0 else (f(a-4,b)+f(a-3,b-1)+f(a-2,b-2)+f(a-1,b-3))/4);return n>4800 or f(n:=ceil(n/25.0),n)

class Solution:
    def soupServings(self, n: int) -> float:
        f=cache(lambda a,b:(f(a-4,b)+f(a-3,b-1)+f(a-2,b-2)+f(a-1,b-3))/4if a>0<b else(0,(1,0.5)[b<=0])[a<=0]);return n>4800or f(n:=ceil(n/25),n)

class Solution:
    def soupServings(self, n: int) -> float:
        f=cache(lambda a,b:(f(a-4,b)+f(a-3,b-1)+f(a-2,b-2)+f(a-1,b-3))/4if a>0<b else((0.5,1)[b>0],0)[a>0]);return n>4800or f(n:=ceil(n/25),n)

class Solution:
    def soupServings(self, n: int) -> float:
        f=cache(lambda a,b:mean(f(a-4+x,b-x)for x in range(4))if a>0<b else((1,2)[b>0],0)[a>0]/2);return n>1e4or f(n:=ceil(n/25),n)

test('''
808. Soup Servings
Medium

338

912

Add to List

Share
There are two types of soup: type A and type B. Initially, we have n ml of each type of soup. There are four kinds of operations:

Serve 100 ml of soup A and 0 ml of soup B,
Serve 75 ml of soup A and 25 ml of soup B,
Serve 50 ml of soup A and 50 ml of soup B, and
Serve 25 ml of soup A and 75 ml of soup B.
When we serve some soup, we give it to someone, and we no longer have it. Each turn, we will choose from the four operations with an equal probability 0.25. If the remaining volume of soup is not enough to complete the operation, we will serve as much as possible. We stop once we no longer have some quantity of both types of soup.

Note that we do not have an operation where all 100 ml's of soup B are used first.

Return the probability that soup A will be empty first, plus half the probability that A and B become empty at the same time. Answers within 10-5 of the actual answer will be accepted.

 

Example 1:

Input: n = 50
Output: 0.62500
Explanation: If we choose the first two operations, A will become empty first.
For the third operation, A and B will become empty at the same time.
For the fourth operation, B will become empty first.
So the total probability of A becoming empty first plus half the probability that A and B become empty at the same time, is 0.25 * (1 + 1 + 0.5 + 0) = 0.625.
Example 2:

Input: n = 100
Output: 0.71875
 

Example 3:

Input: n = 51
Output: 0.65625

Constraints:

0 <= n <= 10^9
''')

