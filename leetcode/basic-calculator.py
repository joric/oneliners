from lc import *

class Solution:
    def calculate(self, s):
        def calc(i):
            x, q, r = 0, [], "+"
            def update(op, v):
                if op == "+":
                    q.append(v)
                elif op == "-":
                    q.append(-v)
                elif op == "*":
                    q.append(q.pop() * v)
                elif op == "/":
                    q.append(int(q.pop() / v))
            while i < len(s):
                if s[i].isdigit():
                    x = x * 10 + int(s[i])
                elif s[i] in "+-*/":
                    update(r, x)
                    x, r = 0, s[i]
                elif s[i] == "(":
                    x, j = calc(i + 1)
                    i = j - 1
                elif s[i] == ")":
                    update(r, x)
                    return sum(q), i + 1
                i += 1
            update(r, x)
            return sum(q)
        return calc(0)


test('''
224. Basic Calculator
Hard

Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

Example 1:

Input: s = "1 + 1"
Output: 2

Example 2:

Input: s = " 2-1 + 2 "
Output: 3

Example 3:

Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23

Constraints:

1 <= s.length <= 3 * 10^5
s consists of digits, '+', '-', '(', ')', and ' '.
s represents a valid expression.
'+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
'-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
There will be no two consecutive operators in the input.
Every number and running calculation will fit in a signed 32-bit integer.

''')


