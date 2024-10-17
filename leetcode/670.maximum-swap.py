from lc import *

# https://leetcode.com/problems/maximum-swap/discuss/2114239/Intuitive-or-recursive-or-python-3

class Solution:
    def maximumSwap(self, a: int) -> int:
        def f(a):
            if not a:
                return a
            m = max(a)
            if m == a[0]:
                return [a[0]] + f(a[1:])
            else:
                i = a[::-1].index(m)
                a[0],a[~i]=a[~i],a[0]
                return a
        return int(''.join(map(str,f([*map(int,str(a))]))))

# https://leetcode.com/problems/maximum-swap/discuss/107137/3-5-lines-PythonC%2B%2BJavaRuby

# updated 2024-10-17 (POTD)

class Solution:
    def maximumSwap(self, n: int) -> int:
        d=[10**i for i in range(len(str(n)))];return max(n+n//p%10*(q-p)+n//q%10*(p-q)for p in d for q in d)

test('''
670. Maximum Swap
Medium

3415

212

Add to List

Share
You are given an integer num. You can swap two digits at most once to get the maximum valued number.

Return the maximum valued number you can get.

 

Example 1:

Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:

Input: num = 9973
Output: 9973
Explanation: No swap.
 

Constraints:

0 <= num <= 108
Accepted
272,008
Submissions
553,985
''')
