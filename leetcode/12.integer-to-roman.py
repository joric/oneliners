from lc import *

# https://leetcode.com/problems/integer-to-roman

class Solution:
    def intToRoman(self, num: int) -> str:
        return ''.join((('','M','MM','MMM','MMMM')[num//1000],
            ('','C','CC','CCC','CD','D','DC','DCC','DCCC','CM')[(num//100)%10],
            ('','X','XX','XXX','XL','L','LX','LXX','LXXX','XC')[(num//10)%10],
            ('','I','II','III','IV','V','VI','VII','VIII','IX')[num%10]))

class Solution:
    def intToRoman(self, num: int) -> str:
        return (r := ('','I','II','III','IV','V','VI','VII','VIII','IX','','X','XX','XXX','XL','L','LX',
            'LXX','LXXX','XC','','C','CC','CCC','CD','D','DC','DCC','DCCC','CM','','M','MM','MMM',
            'MMMM')) and (r[num//1000+30]+r[(num//100)%10+20]+r[(num//10)%10+10]+r[num%10])

class Solution:
    def intToRoman(self, n: int) -> str:
        return "M"*(n//1000)+"".join([[[r[0]*d,r[0]+r[1]][d>3],[r[1]+r[0]*(d-5),r[0]+r[2]][d>8]][d>4] for d,r in ((n%1000//100,"CDM"),(n%100//10,"XLC"),(n%10,"IVX"))])

class Solution:
    def intToRoman(self, num: int) -> str:
        v = ('M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I')
        k = (1000,900,500,400,100,90,50,40,10,9,5,4,1)
        i,x,r = 0,num,''
        while x:
            while x >= k[i]:
                x -= k[i]
                r += v[i]
            i += 1
        return r

class Solution:
    def intToRoman(self, num: int) -> str:
        return (v:=('M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I'),
            k:=(1000,900,500,400,100,90,50,40,10,9,5,4,1),
            a:=lambda i,x,r: a(i,x-k[i],r+v[i]) if x>=k[i] else (i+1,x,r)) and (f:=
            lambda i,x,r: f(*a(i,x,r)) if x else (i,x,r))(0,num,'')[-1]

class Solution:
    def intToRoman(self, num: int) -> str:
        v,k,a,f=('M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I'),(1000,900,500,400,100,90,50,40,10,9,5,4,1),lambda i,x,r:a(i,x-k[i],r+v[i])if x>=k[i]else(i+1,x,r),lambda i,x,r: f(*a(i,x,r))if x else(i,x,r);return f(0,num,'')[-1]

class Solution:
    def intToRoman(self, n: int) -> str:
        return 'M'*(n//1000)+''.join([[[r[0]*d,r[0]+r[1]][d>3],[r[1]+r[0]*(d-5),r[0]+r[2]][d>8]][d>4]for d,r in((n%1000//100,'CDM'),(n%100//10,'XLC'),(n%10,'IVX'))])

class Solution:
    def intToRoman(self, n: int) -> str:
        return'M'*(n//1000)+''.join([[a*d,a+b][d>3],[b+a*(d-5),a+c][d>8]][d>4]for d,(a,b,c)in((n%1000//100,'CDM'),(n%100//10,'XLC'),(n%10,'IVX')))

class Solution:
    def intToRoman(self, n: int) -> str:
        return'M'*(n//1000)+''.join([[a*d,a+b][d>3],[b+a*(d-5),a+c][d>8]][d>4]for d,(a,b,c)in((n%1000//100,'CDM'),(n%100//10,'XLC'),(n%10,'IVX')))

class Solution:
    def intToRoman(self, n: int) -> str:
        return'M'*(n//1000)+''.join([[a*d,a+b][d>3],[b+a*(d-5),a+c][d>8]][d>4]for d,(a,b,c)in((n//100%10,'CDM'),(n//10%10,'XLC'),(n%10,'IVX')))

test('''
12. Integer to Roman
Medium

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.

Example 1:

Input: num = 3
Output: "III"
Explanation: 3 is represented as 3 ones.

Example 2:

Input: num = 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.

Example 3:

Input: num = 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

Constraints:

1 <= num <= 3999

''')

