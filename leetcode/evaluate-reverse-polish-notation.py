from lc import *

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        def f(a, b, c):
            if c == "+": return a+b
            if c == "-": return b-a
            if c == "*": return a*b
            if c == "/": return int(b/a)
        for token in tokens:
            if token in "*/+-":
                stack.append(f(stack.pop(), stack.pop(), token))
            else:
                stack.append(int(token))
        return stack[-1]

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        return (s:=[]) or any(s.append((lambda a,b,c:{'+':a+b,'-':b-a,'*':a*b,'/':a and int(b/a)}[c])(s.pop(),s.pop(),t) if t in '*/+-' else int(t)) for t in tokens) or s[-1]

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        return reduce(lambda s,t:s+[(lambda a,b,c:{'+':a+b,'-':b-a,'*':a*b,'/':a and int(b/a)}[c])(s.pop(),s.pop(),t) if t in '*/+-' else int(t)],tokens,[])[-1]

# not me

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        return reduce(lambda s,t:s[:-2]+[(lambda b,a:{'+':a+b,'-':b-a,'*':a*b,'/':a and int(b/a)}[t])(*s[-2:])] if t in '*/+-' else s+[int(t)],tokens,[])[-1]

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        return reduce(lambda s,t:s[:-2]+[int(eval(f'{s[-2]}{t}{s[-1]}'))]if t in'*/+-'else s+[int(t)],tokens,[])[-1]

class Solution:
    def evalRPN(self, T: List[str]) -> int:
        t=T.pop();r=self.evalRPN;return int((lambda b,a:eval(f'{a}{t}{b}'))(r(T),r(T)))if t in'*/+-'else int(t)

# me

class Solution:
    def evalRPN(self, T: List[str]) -> int:
        t=T.pop();r=self.evalRPN;return int(eval('{2}{1}{0}'.format(r(T),t,r(T)))if t in'*/+-'else t)

test('''

150. Evaluate Reverse Polish Notation
Medium

4384

763

Add to List

Share
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

Note that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.

 

Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
 

Constraints:

1 <= tokens.length <= 10^4
tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].

''')


