from lc import *

# POTD july 12, 2024
# POTD july 23, 2025

# https://leetcode.com/problems/maximum-score-from-removing-substrings/discuss/1009040/Linear-time-solution-using-stack

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def f(t,p):
            nonlocal s
            q = ''
            r = 0
            for c in s:
                if q=='' or q[-1]!=t[0] or c!=t[1]:
                    q += c
                else:
                    q = q[:-1]
                    r += p
            s = q
            return r
        return f('ab',x)+f('ba',y)if x>y else f('ba',y)+f('ab',x)

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        d=[s];f=lambda t,p,q='',r=0:all((q==''or q[-1]!=t[0]or c!=t[1])and(q:=q+c)or(q:=q[:-1],r:=r+p)for c in d[0])and setitem(d,0,q)or r;return f('ab',x)+f('ba',y)if x>y else f('ba',y)+f('ab',x)

# https://leetcode.com/problems/maximum-score-from-removing-substrings/discuss/1009489/PythonC%2B%2B-Clean-Linear-Scan-O(1)-Space

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x < y:
            x, y, s = y, x, s[::-1]
        a = b = r = 0
        for c in s:
            if c == 'a':
                a += 1
            elif c == 'b':
                if a:
                    a -= 1
                    r += x
                else:
                    b += 1
            else:
                r += min(a,b)*y
                a = b = 0
        return r + min(a,b)*y

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        a=b=r=0;x,y,s=((x,y,s),(y,x,s[::-1]))[x<y]
        f=lambda a,b,r,c:c=='a'and(a+1,b,r)or c=='b' and(a and(a-1,b,r+x)or(a,b+1,r))or(0,0,r+min(a,b)*y)
        for c in s:
            a,b,r = f(a,b,r,c)
        return r + min(a,b)*y

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        a=b=r=0;x,y,s=((x,y,s),(y,x,s[::-1]))[x<y]
        def f(a,b,r,c):
            return map(sum,zip((a,b,r),c=='a'and(1,0,0)or c=='b'and(a and(-1,0,x)or(0,1,0))or(-a,-b,min(a,b)*y)))
        for c in s:
            a,b,r = f(a,b,r,c)
        return r + min(a,b)*y

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        x,y,s=((x,y,s),(y,x,s[::-1]))[x<y];return(t:=lambda a,b,r:r+min(a,b)*y)(*reduce(lambda p,c:(lambda a,b,r,c:c=='a'and(a+1,b,r)or c=='b'and(a and(a-1,b,r+x)or(a,b+1,r))or(0,0,r+min(a,b)*y))(*p,c),s,[0]*3))

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        x,y,s=((x,y,s),(y,x,s[::-1]))[x<y];return(t:=lambda p:p[2]+min(p[:2])*y)(reduce(lambda p,c:c=='a'and(p[0]+1,*p[1:3])or c=='b'and(p[0] and(p[0]-1,p[1],p[2]+x)or(p[0],p[1]+1,p[2]))or(0,0,t(p)),s,[0]*3))

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        z=1-2*(x<y);x,y=(x,y)[::z];return(t:=lambda p:p[2]+y*min(p[:2]))(reduce(lambda p,c:[*map(sum,zip(p,{'b':p[0]and(-1,0,x)or(0,1,0),'a':(1,0,0)}.get(c,(-p[0],-p[1],t(p)-p[2]))))],s[::z],[0]*3))

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        z=1-2*(x<y);x,y=(x,y)[::z];return(t:=lambda p:p[2]+y*min(p[:2]))(reduce(lambda p,c:{'b':((w:=p[0],p[1]+1,p[2]),(w-1,p[1],p[2]+x))[w>0],'a':(w+1,*p[1:3])}.get(c,(0,0,t(p))),s[::z],[0]*3))


test('''
1717. Maximum Score From Removing Substrings
Medium

715

49

Add to List

Share
You are given a string s and two integers x and y. You can perform two types of operations any number of times.

Remove substring "ab" and gain x points.
For example, when removing "ab" from "cabxbae" it becomes "cxbae".
Remove substring "ba" and gain y points.
For example, when removing "ba" from "cabxbae" it becomes "cabxe".
Return the maximum points you can gain after applying the above operations on s.

 

Example 1:

Input: s = "cdbcbbaaabab", x = 4, y = 5
Output: 19
Explanation:
- Remove the "ba" underlined in "cdbcbbaaabab". Now, s = "cdbcbbaaab" and 5 points are added to the score.
- Remove the "ab" underlined in "cdbcbbaaab". Now, s = "cdbcbbaa" and 4 points are added to the score.
- Remove the "ba" underlined in "cdbcbbaa". Now, s = "cdbcba" and 5 points are added to the score.
- Remove the "ba" underlined in "cdbcba". Now, s = "cdbc" and 5 points are added to the score.
Total score = 5 + 4 + 5 + 5 = 19.
Example 2:

Input: s = "aabbaaxybbaabb", x = 5, y = 4
Output: 20
 

Constraints:

1 <= s.length <= 105
1 <= x, y <= 104
s consists of lowercase English letters.
Accepted
23,528
Submissions
45,067
''')