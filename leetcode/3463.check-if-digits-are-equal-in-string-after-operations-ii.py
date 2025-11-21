from lc import *

# https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-ii/solutions/6457845/python-check-mod2-and-mod5/

# TODO

class Solution:
    def hasSameDigits(self, s: str) -> bool:
        def cal(a, mod):
            count = 0
            while a > 0 and a % mod == 0:
                count += 1
                a //= mod
            return a % mod, count

        def test(mod):
            n = len(s)
            res = 0
            r = 1
            c = 0
            for i in range(n - 1):
                if c == 0:
                    res += r * (int(s[i]) - int(s[i + 1]))

                rr, cc = cal(n - 2 - i, mod)
                r = r * rr % mod
                c += cc

                rr, cc = cal(i + 1, mod)
                r = r * pow(rr, mod - 2, mod) % mod
                c -= cc
            return res % mod == 0

        return test(2) and test(5)

# https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-ii/solutions/6457566/hack-just-for-fun/

class Solution:
    def hasSameDigits(self, s: str) -> bool:
        n = len(s) - 2
        first, second = 0, 0
        c = [1]
        coeff = 1 
        for k in range(n + 1):
            mod_coeff = coeff % 10
            first = (first + mod_coeff * (ord(s[k]) - ord('0'))) % 10
            second = (second + mod_coeff * (ord(s[k + 1]) - ord('0'))) % 10
            if k < n//2 :
                if coeff % 10000000 == 0:
                    coeff = 0
                else:
                    coeff = coeff * (n - k) // (k + 1) if k < n else 1 
                c.append(coeff)
            else:
                coeff = c[n - 1 - k]
                c.append(coeff)
        return first == second

# TLE
class Solution:
    def hasSameDigits(self, s: str) -> bool:
        d=map(int,s);[d:=[sum(p)%10 for p in pairwise(d)]for _ in s[2:]];return eq(*d[:2])

test('''
3463. Check If Digits Are Equal in String After Operations II
Attempted
Hard
Topics
premium lock icon
Companies
Hint
You are given a string s consisting of digits. Perform the following operation repeatedly until the string has exactly two digits:

For each pair of consecutive digits in s, starting from the first digit, calculate a new digit as the sum of the two digits modulo 10.
Replace s with the sequence of newly calculated digits, maintaining the order in which they are computed.
Return true if the final two digits in s are the same; otherwise, return false.

 

Example 1:

Input: s = "3902"

Output: true

Explanation:

Initially, s = "3902"
First operation:
(s[0] + s[1]) % 10 = (3 + 9) % 10 = 2
(s[1] + s[2]) % 10 = (9 + 0) % 10 = 9
(s[2] + s[3]) % 10 = (0 + 2) % 10 = 2
s becomes "292"
Second operation:
(s[0] + s[1]) % 10 = (2 + 9) % 10 = 1
(s[1] + s[2]) % 10 = (9 + 2) % 10 = 1
s becomes "11"
Since the digits in "11" are the same, the output is true.
Example 2:

Input: s = "34789"

Output: false

Explanation:

Initially, s = "34789".
After the first operation, s = "7157".
After the second operation, s = "862".
After the third operation, s = "48".
Since '4' != '8', the output is false.
 

Constraints:

3 <= s.length <= 105
s consists of only digits.
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
10,744/87.3K
Acceptance Rate
12.3%
Topics
icon
Companies
Hint 1
Can we use nCr and use Pascal's triangle values here?
Hint 2
nCr mod 10 can be uniquely determined from nCr mod 2 and nCr mod 5.
Hint 3
Use Lucas's theorem.
Similar Questions
Pascal's Triangle
Easy
''')
