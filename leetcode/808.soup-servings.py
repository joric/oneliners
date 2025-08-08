from lc import *

# https://leetcode.com/problems/soup-servings/solutions/3834232/no-explanation-real-theta-1-rust-solution/?envType=daily-question&envId=2025-08-08

class Solution:
    def soupServings(self, n: int) -> float:
        N = 194
        r = [[0.5 if i==0==j else 1.0 if i==0 else 0.0 for j in range(N)]for i in range(N)]
        for i in range(1, N):
            for j in range(1, N):
                r[i][j] = sum(r[i-d if i>=d else 0][j-(4-d) if j>=(4-d) else 0]for d in range(1,5))/4
        n = ceil(n/25)
        return 1.0 if n>4800 or n>N else r[n][n]

# https://leetcode.com/problems/soup-servings/discuss/121711/C%2B%2BJavaPython-When-N-greater-4800-just-return-1

class Solution:
    def soupServings(self, n: int) -> float:
        return n>1e4or(f:=cache(lambda a,b:mean(f(a-4+x,b-x)for x in range(4))if a>0<b else((1,2)[b>0],0)[a>0]/2))(n:=ceil(n/25),n)

# POTD 2025-08-08

class Solution:
    def soupServings(self, n: int) -> float:
        return n>1e4or(f:=cache(lambda a,b:a>0<b and mean(f(a-4+x,b-x)for x in range(4))or(a<1)*(1+(b>0))/2))(n:=-(-n//25),n)

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

Other examples:

Input: n = 1
Output: 0.62500

Constraints:

0 <= n <= 10^9
''')
