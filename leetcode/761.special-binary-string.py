from lc import *

# https://leetcode.com/problems/special-binary-string/solutions/1217456/python-3-one-line-by-l1ne-ucp4/

class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        node = [[]]
        op = lambda n: ''.join(sorted([x[0] for x in n[0]], reverse=True))
        for c in s:
            if int(c):
                node[0].append([[], node])
                node = node[0][-1]
            else:
                node[0] = '1' + op(node) + '0'
                node = node[1]
        return op(node)

class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        return (O := lambda n: ''.join(sorted([x[0] for x in n[0]], reverse=True)))(reduce(lambda N,c: N[0].append([[], N]) or N[0][-1] if int(c) else setitem(N, 0, '1' + O(N) + '0') or N[1], s, [[]]))

# https://leetcode.com/problems/special-binary-string/solutions/113211/javacpython-easy-and-concise-recursion-b-pyib/

class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        count = i = 0
        res = []
        for j, v in enumerate(s):
            count = count + 1 if v=='1' else count - 1
            if count == 0:
                res.append('1' + self.makeLargestSpecial(s[i + 1:j]) + '0')
                i = j + 1
        return ''.join(sorted(res)[::-1])

class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        def f(s):
            c = i = 0
            r = []
            for j, v in enumerate(s):
                c = c + 1 if v == '1' else c - 1
                if c == 0:
                    r.append('1' + f(s[i + 1:j]) + '0')
                    i = j + 1
            return ''.join(sorted(r)[::-1])
        return f(s)

class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        return(f:=lambda s,c=0,i=0:''.join(sorted(f'1{f(s[i+1:(i:=j+1)-1])}0'for j,v in enumerate(s)if(c:=c+int(v)*2-1)<1)[::-1]))(s)

test('''
761. Special Binary String
Hard
Topics
premium lock icon
Companies
Hint
Special binary strings are binary strings with the following two properties:

The number of 0's is equal to the number of 1's.
Every prefix of the binary string has at least as many 1's as 0's.
You are given a special binary string s.

A move consists of choosing two consecutive, non-empty, special substrings of s, and swapping them. Two strings are consecutive if the last character of the first string is exactly one index before the first character of the second string.

Return the lexicographically largest resulting string possible after applying the mentioned operations on the string.

 

Example 1:

Input: s = "11011000"
Output: "11100100"
Explanation: The strings "10" [occuring at s[1]] and "1100" [at s[3]] are swapped.
This is the lexicographically largest string possible after some number of swaps.
Example 2:

Input: s = "10"
Output: "10"
 

Constraints:

1 <= s.length <= 50
s[i] is either '0' or '1'.
s is a special binary string.
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
30,222/45.7K
Acceptance Rate
66.2%
Topics
Principal
String
Divide and Conquer
Sorting
Weekly Contest 66
icon
Companies
Hint 1
Draw a line from (x, y) to (x+1, y+1) if we see a "1", else to (x+1, y-1). A special substring is just a line that starts and ends at the same y-coordinate, and that is the lowest y-coordinate reached. Call a mountain a special substring with no special prefixes - ie. only at the beginning and end is the lowest y-coordinate reached. If F is the answer function, and S has mountain decomposition M1,M2,M3,...,Mk, then the answer is: reverse_sorted(F(M1), F(M2), ..., F(Mk)). However, you'll also need to deal with the case that S is a mountain, such as 11011000 -> 11100100.
Similar Questions
Valid Parenthesis String
Medium
Number of Good Binary Strings
Medium
''')
