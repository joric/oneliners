from lc import *

class Solution:
    def calculate(self, s):
        def calc(i):
            x, q, r = 0, [], "+"
            def update(op, v):
                if op == "+": q.append(v)
                if op == "-": q.append(-v)
                if op == "*": q.append(q.pop() * v)
                if op == "/": q.append(int(q.pop() / v))
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

Description
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators , open ( and closing parentheses ) and empty spaces . The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-2147483648, 2147483647]

Wechat reply 【Google】 get the latest requent Interview questions. (wechat id : jiuzhang0607)


Do not use the eval built-in library function.

Example 1:

Input: s = "1 + 1"
Output: 2
Explanation:1 + 1 = 2

Example 2:

Input: s = "6-4 / 2"
Output: 4
Explanation:4/2=2，6-2=4

Example 3:

Input: s = "(2+4)*2"
Output: 12

''')


