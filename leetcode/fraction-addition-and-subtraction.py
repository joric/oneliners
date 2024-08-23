from lc import *

# https://leetcode.com/problems/fraction-addition-and-subtraction/discuss/103384/Small-simple-C%2B%2BJavaPython

class Solution:
    def fractionAddition(self, expression: str) -> str:
        ints = map(int, re.findall('[+-]?\d+', expression))
        A, B = 0, 1
        for a in ints:
            b = next(ints)
            A = A * b + a * B
            B *= b
            g = math.gcd(A, B)
            A //= g
            B //= g
        return '%d/%d' % (A, B)

# https://leetcode.com/problems/fraction-addition-and-subtraction/discuss/103387/Python-easy-understood-2-line-solution

class Solution:
    def fractionAddition(self, e: str) -> str:
        f=sum(map(__import__('fractions').Fraction, re.findall('[+-]?\d+/\d+',e)));return f'{f.numerator}/{f.denominator}'

class Solution:
    def fractionAddition(self, e: str) -> str:
        return'/'.join(map(str,__import__('fractions').Fraction(eval(e)).limit_denominator().as_integer_ratio()))

class Solution:
    def fractionAddition(self, e: str) -> str:
        f=__import__('fractions').Fraction(eval(e)).limit_denominator();return f'{f.numerator}/{f.denominator}'

class Solution:
    def fractionAddition(self, e: str) -> str:
        a,b=__import__('fractions').Fraction(eval(e)).limit_denominator().as_integer_ratio();return f'{a}/{b}'

class Solution:
    def fractionAddition(self, e: str) -> str:
        return'%d/%d'%__import__('fractions').Fraction(eval(e)).limit_denominator().as_integer_ratio()

test('''
592. Fraction Addition and Subtraction
Medium

544

576

Add to List

Share
Given a string expression representing an expression of fraction addition and subtraction, return the calculation result in string format.

The final result should be an irreducible fraction. If your final result is an integer, change it to the format of a fraction that has a denominator 1. So in this case, 2 should be converted to 2/1.

 

Example 1:

Input: expression = "-1/2+1/2"
Output: "0/1"
Example 2:

Input: expression = "-1/2+1/2+1/3"
Output: "1/3"
Example 3:

Input: expression = "1/3-1/2"
Output: "-1/6"
 

Constraints:

The input string only contains '0' to '9', '/', '+' and '-'. So does the output.
Each fraction (input and output) has the format ±numerator/denominator. If the first input fraction or the output is positive, then '+' will be omitted.
The input only contains valid irreducible fractions, where the numerator and denominator of each fraction will always be in the range [1, 10]. If the denominator is 1, it means this fraction is actually an integer in a fraction format defined above.
The number of given fractions will be in the range [1, 10].
The numerator and denominator of the final result are guaranteed to be valid and in the range of 32-bit int.
Accepted
58,850
Submissions
99,068
''')
