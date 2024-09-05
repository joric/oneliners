from lc import *

# related to basic calculator

# amazing chart/state machine here https://leetcode.com/problems/valid-number/discuss/360781/Python-with-state-machine-36ms

class Solution:
    def isNumber(self, s: str) -> bool:
        start, int_sign, integer, point, frac, exp, exp_sign, exp_int = range(8)
        digit, sign, dot, e = range(1,5)

        def classify(c):
            if c in '0123456789': return digit
            if c == '.'         : return dot
            if c in '+-'        : return sign
            if c == 'e'         : return e
            return False

        machine = {
            start   : {sign:int_sign, digit:integer, dot:point},
            int_sign: {digit:integer, dot:point},
            integer : {digit:integer, dot:frac, e:exp},
            point   : {digit:frac},
            frac    : {digit:frac, e:exp},
            exp     : {digit:exp_int, sign:exp_sign},
            exp_sign: {digit:exp_int},
            exp_int : {digit:exp_int},
        }

        state = start
        for c in s.lower().strip():
            if not (state := machine[state].get(classify(c), False)):
                return False
        return state in [integer, frac, exp_int]

class Solution:
    def isNumber(self, s: str) -> bool:
        err, start, int_sign, integer, point, frac, exp, exp_sign, exp_int = range(9)
        digit, sign, dot, e = range(1, 5)
        machine = {
            err     : {},
            start   : {sign:int_sign, digit:integer, dot:point},
            int_sign: {digit:integer, dot:point},
            integer : {digit:integer, dot:frac, e:exp},
            point   : {digit:frac},
            frac    : {digit:frac, e:exp},
            exp     : {digit:exp_int, sign:exp_sign},
            exp_sign: {digit:exp_int},
            exp_int : {digit:exp_int},
        }
        tokens = {c: v for k, v in (('0123456789', digit), ('.', dot), ('+-', sign), ('eE', e)) for c in k}
        return reduce(lambda a, c: machine[a].get(tokens.get(c, None), err), s.strip(), start) in [integer, frac, exp_int]


class Solution:
    def isNumber(self, s: str) -> bool:
        return re.match('(\\+|-|)(\\d+|\\.\\d+|\\d+\\.\\d*)(e(\\+|-|)\\d+|)',s)!=None

test('''

65. Valid Number
Hard

788

1364

Add to List

Share
A valid number can be split up into these components (in order):

A decimal number or an integer.
(Optional) An 'e' or 'E', followed by an integer.
A decimal number can be split up into these components (in order):

(Optional) A sign character (either '+' or '-').
One of the following formats:
One or more digits, followed by a dot '.'.
One or more digits, followed by a dot '.', followed by one or more digits.
A dot '.', followed by one or more digits.
An integer can be split up into these components (in order):

(Optional) A sign character (either '+' or '-').
One or more digits.
For example, all the following are valid numbers: ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"], while the following are not valid numbers: ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].

Given a string s, return true if s is a valid number.

 

Example 1:

Input: s = "0"
Output: true
Example 2:

Input: s = "e"
Output: false
Example 3:

Input: s = "."
Output: false
 

Constraints:

1 <= s.length <= 20
s consists of only English letters (both uppercase and lowercase), digits (0-9), plus '+', minus '-', or dot '.'.
''')