from lc import *

# https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/discuss/2657075/Python-dp-recursion-8-lines

class Solution:
    def numWays(self, s: int, a: int) -> int:
        @cache
        def f(p,s):
            if not s:
                return p==0
            if p<0 or p>=a or p>s:
                return 0
            return sum(f(p+i,s-1)for i in(-1,0,1))
        return f(0,s)%(10**9+7)

class Solution:
    def numWays(self, s: int, a: int) -> int:
        return(f:=cache(lambda p,s:s>0<=p<a and sum(f(p+i,s-1)for i in(-1,0,1))or p==0))(0,s)%(10**9+7)

test('''
1269. Number of Ways to Stay in the Same Place After Some Steps
Hard

750

39

Add to List

Share
You have a pointer at index 0 in an array of size arrLen. At each step, you can move 1 position to the left, 1 position to the right in the array, or stay in the same place (The pointer should not be placed outside the array at any time).

Given two integers steps and arrLen, return the number of ways such that your pointer is still at index 0 after exactly steps steps. Since the answer may be too large, return it modulo 109 + 7.

 

Example 1:

Input: steps = 3, arrLen = 2
Output: 4
Explanation: There are 4 differents ways to stay at index 0 after 3 steps.
Right, Left, Stay
Stay, Right, Left
Right, Stay, Left
Stay, Stay, Stay
Example 2:

Input: steps = 2, arrLen = 4
Output: 2
Explanation: There are 2 differents ways to stay at index 0 after 2 steps
Right, Left
Stay, Stay
Example 3:

Input: steps = 4, arrLen = 2
Output: 8
 

Constraints:

1 <= steps <= 500
1 <= arrLen <= 10^6
''')
