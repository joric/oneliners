from lc import *

# https://leetcode.com/problems/integer-to-english-words/discuss/70632/Recursive-Python

class Solution:
    def numberToWords(self, num: int) -> str:
        to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
            'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
        def words(n):
            if n < 20:
                return to19[n-1:n]
            if n < 100:
                return [tens[n//10-2]] + words(n%10)
            if n < 1000:
                return [to19[n//100-1]] + ['Hundred'] + words(n%100)
            for p, w in enumerate(('Thousand', 'Million', 'Billion'), 1):
                if n < 1000**(p+1):
                    return words(n//1000**p) + [w] + words(n%1000**p)
        return ' '.join(words(num)) or 'Zero'

class Solution:
    def numberToWords(self, num: int) -> str:
        return ' '.join([w:='One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen '\
            'Fifteen Sixteen Seventeen Eighteen Nineteen Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split(),
            (t:=lambda n:w[:19][n-1:n] if n<20
            else [w[19:][n//10-2]] + t(n%10) if n<100
            else [w[:19][n//100-1]] +['Hundred'] + t(n%100) if n<1000
            else t(n//1000)+['Thousand']+t(n%1000) if n<1000**2
            else t(n//1000**2)+['Million']+t(n%1000**2) if n<1000**3
            else t(n//1000**3)+['Billion']+t(n%1000**3))(num)][1]) or 'Zero'

class Solution:
    def numberToWords(self, num):
        return' '.join([w:='One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split(),(t:=lambda n:w[:19][n-1:n] if n<20 else [w[19:][n//10-2]] + t(n%10) if n<100 else [w[:19][n//100-1]] +['Hundred'] + t(n%100) if n<1000 else t(n//1000)+['Thousand']+t(n%1000) if n<1000**2 else t(n//1000**2)+['Million']+t(n%1000**2) if n<1000**3 else t(n//1000**3)+['Billion']+t(n%1000**3))(num)][1]) or 'Zero'

class Solution:
    def numberToWords(self, n: int) -> str:
        return' '.join([w:='One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split(),(t:=lambda n,d=1000:w[:19][n-1:n]if n<20 else[w[19:][n//10-2]]+t(n%10)if n<100 else[w[:19][n//100-1]]+['Hundred']+t(n%100)if n<d else t(n//d)+['Thousand']+t(n%d)if n<d**2 else t(n//d**2)+['Million']+t(n%d**2)if n<d**3 else t(n//d**3)+['Billion']+t(n%d**3))(n)][1])or'Zero'

test('''
273. Integer to English Words
Hard

2444

5582

Add to List

Share
Convert a non-negative integer num to its English words representation.

 

Example 1:

Input: num = 123
Output: "One Hundred Twenty Three"
Example 2:

Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
 

Constraints:

0 <= num <= 2^31 - 1
''')
