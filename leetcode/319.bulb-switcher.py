from lc import *

class Solution(object):
    def bulbSwitch(self, n: int) -> int:
        b = [0]*n
        for s in range(1, n+1):
            for s in range(s-1, n, s):
                b[s] ^= 1
        return sum(b)

class Solution:
    def bulbSwitch(self, n: int) -> int:
        z = 1
        e = 0.0001
        while abs(z**2 - n)>= e:
            z -= (z*z - n) / (2*z)
        return int(z)

class Solution:
    def bulbSwitch(self, n: int) -> int:
        return isqrt(n)

class Solution:bulbSwitch=isqrt

test('''
319. Bulb Switcher
Medium

1207

1876

Add to List

Share
There are n bulbs that are initially off. You first turn on all the bulbs, then you turn off every second bulb.

On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the ith round, you toggle every i bulb. For the nth round, you only toggle the last bulb.

Return the number of bulbs that are on after n rounds.

 

Example 1:


Input: n = 3
Output: 1
Explanation: At first, the three bulbs are [off, off, off].
After the first round, the three bulbs are [on, on, on].
After the second round, the three bulbs are [on, off, on].
After the third round, the three bulbs are [on, off, off]. 
So you should return 1 because there is only one bulb is on.
Example 2:

Input: n = 0
Output: 0
Example 3:

Input: n = 1
Output: 1
 

Constraints:

0 <= n <= 10^9
Accepted
130,968
Submissions
270,736
''')
