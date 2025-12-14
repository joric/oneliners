from lc import *

# https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/solutions/1709725/javacpython-two-solutions-with-explanati-qpnl/?envType=daily-question&envId=2025-12-14

class Solution:
    def numberOfWays(self, s: str) -> int:
        a = [i for i,c in enumerate(s) if c == 'S']
        r = 1
        for i in range(1,len(a) - 1,2):
            r *= a[i+1] - a[i]
        return r%(10**9+7)*(len(a)%2==0 and len(a)>=2)

class Solution:
    def numberOfWays(self, s: str) -> int:
        a=[i for i,c in enumerate(s)if c=='S']
        n=len(a)
        r = prod(a[i+1]-a[i]for i in range(1,len(a)-1,2))
        return r%(10**9+7)*(2<=n and n%2==0)

class Solution:
    def numberOfWays(self, s: str) -> int:
        return prod(y-x for x,y in pairwise([i for i,c in enumerate(s)if c=='S'][1:-1]))%(10**9+7)*(s.count('S')%2==0)

# https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/solutions/4338588/one-line-solution-by-mikposp-u0k1/?envType=daily-question&envId=2025-12-14

class Solution:
    def numberOfWays(self, c: str) -> int:
        return prod(1+len(m.group(1))for m in re.finditer(r'S(P*)S',c[c.find('S')+1:]))%(10**9+7)if(s:=c.count('S'))and s%2==0 else 0

# https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/discuss/1709725/JavaC%2B%2BPython-Two-Solutions-with-Explanation

class Solution:
    def numberOfWays(self, s: str) -> int:
        a = [i for i,c in enumerate(s) if c=='S']
        r = 1
        for i in range(1,len(a)-1,2):
            r *= a[i+1] - a[i]
        return r % (10**9+7) * (len(a) % 2 == 0 and len(a) >= 2)

class Solution:
    def numberOfWays(self, s: str) -> int:
        n=len(a:=[i for i,c in enumerate(s)if c>'P']);return(n>1,0)[n&1]*reduce(mul,(a[i+1]-a[i]for i in range(1,n-1,2)),1)%(10**9+7)

# another solution

class Solution:
    def numberOfWays(self, s: str) -> int:
        def f(p,i):
            a,b,c,d = p
            return c|b*(i-d),a&c-1,0,i
        return reduce(f,(i for i,c in enumerate(s)if c>'P'),(1,0)*2)[1]%(10**9+7)

class Solution:
    def numberOfWays(self, s: str) -> int:
        return reduce(lambda p,i:(lambda a,b,c,d,i:(c|b*(i-d),a&c-1,0,i))(*p,i),(i for i,c in enumerate(s)if c>'P'),(1,0)*2)[1]%(10**9+7)

class Solution:
    def numberOfWays(self, s: str) -> int:
        return reduce(lambda p,i:(p[2]|p[1]*(i-p[3])%(10**9+7),p[0]&p[2]-1,0,i),(i for i,c in enumerate(s)if c>'P'),(1,0)*2)[1]

class Solution:
    def numberOfWays(self, s: str) -> int:
        a,b,c,d=(1,0)*2
        for i,x in enumerate(s):
            if x>'P':
                a,b,c,d=c|b*(i-d)%(10**9+7),a&c-1,0,i
        return b

# POTD 2025-12-14

class Solution:
    def numberOfWays(self, s: str) -> int:
        p=(1,0)*2;[p:=(p[2]|p[1]*(i-p[3])%(10**9+7),p[0]&p[2]-1,0,i)for i,c in enumerate(s)if c>'P'];return p[1]

test('''
2147. Number of Ways to Divide a Long Corridor
Hard

381

34

Add to List

Share
Along a long library corridor, there is a line of seats and decorative plants. You are given a 0-indexed string corridor of length n consisting of letters 'S' and 'P' where each 'S' represents a seat and each 'P' represents a plant.

One room divider has already been installed to the left of index 0, and another to the right of index n - 1. Additional room dividers can be installed. For each position between indices i - 1 and i (1 <= i <= n - 1), at most one divider can be installed.

Divide the corridor into non-overlapping sections, where each section has exactly two seats with any number of plants. There may be multiple ways to perform the division. Two ways are different if there is a position with a room divider installed in the first way but not in the second way.

Return the number of ways to divide the corridor. Since the answer may be very large, return it modulo 109 + 7. If there is no way, return 0.

 

Example 1:


Input: corridor = "SSPPSPS"
Output: 3
Explanation: There are 3 different ways to divide the corridor.
The black bars in the above image indicate the two room dividers already installed.
Note that in each of the ways, each section has exactly two seats.
Example 2:


Input: corridor = "PPSPSP"
Output: 1
Explanation: There is only 1 way to divide the corridor, by not installing any additional dividers.
Installing any would create some section that does not have exactly two seats.
Example 3:


Input: corridor = "S"
Output: 0
Explanation: There is no way to divide the corridor because there will always be a section that does not have exactly two seats.
 

Constraints:

n == corridor.length
1 <= n <= 10^5
corridor[i] is either 'S' or 'P'.
Accepted
11,652
Submissions
29,346
''')
