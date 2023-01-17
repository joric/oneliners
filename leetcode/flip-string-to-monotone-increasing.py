from lc import *

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        cnt0 = s.count('0')
        cnt1 = 0
        res = n - cnt0
        for i in range(n):
            if s[i] == '0': 
                cnt0 -= 1
            elif s[i] == '1':
                res = min(res, cnt1+cnt0)
                cnt1 += 1
        return res


class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        return reduce(lambda a,c: a if int(c[0]) else min(c[1],a+1),zip(s,accumulate(map(int,s))),0)

test('''
926. Flip String to Monotone Increasing
Medium

3044

125

Add to List

Share
A binary string is monotone increasing if it consists of some number of 0's (possibly none), followed by some number of 1's (also possibly none).

You are given a binary string s. You can flip s[i] changing it from 0 to 1 or from 1 to 0.

Return the minimum number of flips to make s monotone increasing.

 

Example 1:

Input: s = "00110"
Output: 1
Explanation: We flip the last digit to get 00111.
Example 2:

Input: s = "010110"
Output: 2
Explanation: We flip to get 011111, or alternatively 000111.
Example 3:

Input: s = "00011000"
Output: 2
Explanation: We flip to get 00000000.
 

Constraints:

1 <= s.length <= 105
s[i] is either '0' or '1'.
''')

