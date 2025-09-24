from lc import *

# https://leetcode.com/problems/fraction-to-recurring-decimal/

# not enough precision
class Solution:
    def fractionToDecimal(self, n: int, d: int) -> str:
        t=f"{n/d:.17f}"[:-1].rstrip('0').rstrip('.')
        if'.'not in t:return t
        a,b=t.split('.')
        return f'{a}.{m.group(1)}({m.group(2)})'if(m:=re.match(r'(.*?)(.+?)\2+$',b))else f'{a}.{b}'

# last digit is wrong
from decimal import Decimal, getcontext
class Solution:
    def fractionToDecimal(self, n: int, d: int) -> str:
        getcontext().prec=34
        t=str(Decimal(n)/Decimal(d)).rstrip('0').rstrip('.')
        print(t)
        if'.'not in t:return t
        a,b=t.split('.')
        return f'{a}.{m.group(1)}({m.group(2)})'if(m:=re.match(r'(.*?)(.+?)\2+$',b))else f'{a}.{b}'

# still fails large tests

class Solution:
    def fractionToDecimal(self, n: int, d: int) -> str:
        if n == 0:
            return "0"

        getcontext().prec = 800  # give enough room
        val = Decimal(n) / Decimal(d)

        # force fixed-point, then strip trailing zeroes
        s = format(val, 'f').rstrip('0').rstrip('.')

        if '.' not in s:
            return s

        print(s)

        a, b = s.split('.')

        m = re.search(r'(.+?)\1{2,}', b)
        if m:
            prefix = b[:m.start()]
            repeat = m.group(1)
            return f'{a}.{prefix}({repeat})'
        return f'{a}.{b}'

# https://leetcode.com/problems/fraction-to-recurring-decimal/solutions/51138/3-line-python-solution-using-dictionary-with-explanation/?envType=daily-question&envId=2025-09-24

class Solution:
    def fractionToDecimal(self, n: int, d: int) -> str:
        sign, p_int, point, p_frac, d, n, dic = "-"*(n*d<0), str(abs(n)//abs(d)), "."*(n%d!=0), "", abs(d), abs(n)%abs(d), []
        while n not in dic and n!=0: dic, p_frac, n = dic+[n], p_frac+str(n*10//d), n*10%d
        return sign+p_int+point+p_frac if n==0 else sign+p_int+point+p_frac[:dic.index(n)]+"("+p_frac[dic.index(n):]+")"

class Solution:
    def fractionToDecimal(self, n: int, d: int) -> str:
        s,p,q,r,m='-'*(n*d<0),str(abs(n)//abs(d)),'.'*(n%d!=0),'',[];n=abs(n)%abs(d);all(n and n not in m and(m:=m+[n],r:=r+str(n*10//abs(d)),n:=n*10%abs(d))for _ in count());return s+p+q+r if not n else s+p+q+r[:m.index(n)]+'('+r[m.index(n):]+')'

test('''
166. Fraction to Recurring Decimal
Medium
Topics
premium lock icon
Companies
Hint
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

If multiple answers are possible, return any of them.

It is guaranteed that the length of the answer string is less than 104 for all the given inputs.

 

Example 1:

Input: numerator = 1, denominator = 2
Output: "0.5"
Example 2:

Input: numerator = 2, denominator = 1
Output: "2"
Example 3:

Input: numerator = 4, denominator = 333
Output: "0.(012)"

Other examples:

Input: numerator = 2, denominator = 3
Output: "0.(6)"

Input: numerator = 1, denominator = 17
Output: "0.(0588235294117647)"

Input: numerator = 1, denominator = 6
Output: "0.1(6)"

Input: numerator = 0, denominator = 3
Output: "0"

Input: numerator = 0, denominator = -5
Output: "0"

Input: numerator = 1, denominator = 214748364
Output: "0.00(000000465661289042462740251655654056577585848337359161441621040707904997124914069194026549138227660723878669455195477065427143370461252966751355553982241280310754777158628319049732085502639731402098131932683780538602845887105337854867197032523144157689601770377165713821223802198558308923834223016478952081795603341592860749337303449725)"


Constraints:

-231 <= numerator, denominator <= 231 - 1
denominator != 0
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
265,868/1M
Acceptance Rate
26.6%
Topics
Hash Table
Math
String
icon
Companies
Hint 1
No scary math, just apply elementary math knowledge. Still remember how to perform a long division?
Hint 2
Try a long division on 4/9, the repeating part is obvious. Now try 4/333. Do you see a pattern?
Hint 3
Notice that once the remainder starts repeating, so does the divided result.
Hint 4
Be wary of edge cases! List out as many test cases as you can think of and test your code thoroughly.
''')
