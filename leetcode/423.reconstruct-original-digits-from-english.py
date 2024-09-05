from lc import *

class Solution:
    def originalDigits(self, s: str) -> str:
        res = ""
        res += "0"*s.count('z')
        res += "1"*(s.count('o')-s.count('z')-s.count('w')-s.count('u'))
        res += "2"*s.count('w')
        res += "3"*(s.count('h') - s.count('g'))
        res += "4"*s.count('u')
        res += "5"*(s.count('f') - s.count('u'))
        res += "6"*s.count('x')
        res += "7"*(s.count('s')-s.count('x'))
        res += "8"*s.count("g")
        res += "9"*(s.count('i') - s.count('x') - s.count("g") - s.count('f') + s.count('u'))
        return res

class Solution:
    def originalDigits(self, s: str) -> str:
        return ''.join(str(i)*(s.count(v[0])-sum(s.count(c.lower())*[1,-1][c<'a'] for c in v[1:])) for i,v in enumerate('z ozwu w hg u fu x sx g ixgfU'.split()))

test('''

423. Reconstruct Original Digits from English
Medium

688

2323

Add to List

Share
Given a string s containing an out-of-order English representation of digits 0-9, return the digits in ascending order.

 

Example 1:

Input: s = "owoztneoer"
Output: "012"
Example 2:

Input: s = "fviefuro"
Output: "45"
 

Constraints:

1 <= s.length <= 105
s[i] is one of the characters ["e","g","f","i","h","o","n","s","r","u","t","w","v","x","z"].
s is guaranteed to be valid.

''')