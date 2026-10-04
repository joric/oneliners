from lc import *

# https://leetcode.com/problems/valid-parenthesis-string/discuss/107570/JavaC%2B%2BPython-One-Pass-Count-the-Open-Parenthesis

class Solution:
    def checkValidString(self, s: str) -> bool:
        i=j=0
        for c in s:
            i += 1 if c=='(' else -1
            j += 1 if c!=')' else -1
            if j < 0:
                break
            i=max(i,0)
        return i==0

class Solution:
    def checkValidString(self, s: str) -> bool:
        i=j=0;all((i:=i+(c=='(')*2-1,j:=j+(c!=')')*2-1)and j>=0 and[i:=max(i,0)]for c in s);return i==0

class Solution:
    def checkValidString(self, s: str) -> bool:
        i=j=0
        for c in s:
            i=max(0,i+(c=='(')*2-1)
            if(j:=j+(c!=')')*2-1)<0:
                return 0
        return i<1

# can't do next() because the StopIteration value is initialized first
#class Solution:
#    def checkValidString(self, s: str) -> bool:
#        i=j=0;return next((0 for c in s if(i:=max(0,i+(c=='(')*2-1),(j:=j+(c!=')')*2-1)<0)[1]),i<1)

class Solution:
    def checkValidString(self, s: str) -> bool:
        f=lambda s,r,i=1:all((i:=i+(c!=r)*2-1)>0for c in s);return f(s,')')*f(s[::-1],'(')

class Solution:
    def checkValidString(self, s: str) -> bool:
        return all(0<=min(accumulate(2*(c!=r)-1for c in s))and(s:=s[::-1])for r in')(')

# POTD 2026-10-04

class Solution:
    def checkValidString(self, s: str) -> bool:
        return[s:=re.sub(r,r'\1',s)for r in('\((\**)\)','()\*\)|\(\*')for _ in s]and{*s}<={'*'}

class Solution:
    def checkValidString(self, s: str) -> bool:
        return all(0<=min(accumulate((c!=r)-.5for c in s))and(s:=s[::-1])for r in')(')

class Solution:
    def checkValidString(self, s: str) -> bool:
        return all((t:=0)<=min(t:=~-t+2*(c!=r)for c in s)and(s:=s[::-1])for r in')(')

class Solution:
    def checkValidString(self, s: str) -> bool:
        return all((t:=0)<=min(t:=t+(c!=r)-.5for c in s)and(s:=s[::-1])for r in')(')

class Solution:
    def checkValidString(self, s: str) -> bool:
        return all((t:=0)<=min(t:=t-.5+(c!=r)for c in s)and(s:=s[::-1])for r in')(')

'''
# https://leetcode.com/problems/valid-parenthesis-string/solutions/8554397/bitset-dp-approach-brute-force-optimal-a-l50g/?envType=daily-question&envId=2026-10-04
class Solution {
public:
    bool checkValidString(string s) {
        __int128 m=1;for(char c:s)m=c<41?m*2:c<42?m/2:m|m*2|m/2;return m&1;
    }
};
'''

class Solution:
    def checkValidString(self, s: str) -> bool:
        b=1;[b:=(b*2,b//2,b|b*2|b//2)[ord(c)%5]for c in s];return b%2>0

test('''
678. Valid Parenthesis String
Medium

5168

141

Add to List

Share
Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "(*)"
Output: true
Example 3:

Input: s = "(*))"
Output: true
 

Other examples:

Input: s = "(((((()*)(*)*))())())(()())())))((**)))))(()())()"
Output: false

Input: s = "("
Output: false

Constraints:

1 <= s.length <= 100
s[i] is '(', ')' or '*'.
Accepted
255,272
Submissions
731,624
''')