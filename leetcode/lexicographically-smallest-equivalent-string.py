from lc import *

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        p = {c:c for c in set(s1+s2)}
        f = lambda c:c if c not in p or p[c]==c else f(p[c])
        for a,b in zip(s1,s2):
            p[max(f(a),f(b))] = min(f(a),f(b))
        return ''.join(f(c) for c in baseStr)

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        return (p:={c:c for c in set(s1+s2)}) and any(p.__setitem__(max((f:=lambda c:c if c not in p or p[c]==c
            else f(p[c]))(a),f(b)),min(f(a),f(b))) for a,b in zip(s1,s2)) or ''.join(f(c) for c in baseStr)


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        p = {}
        def f(x):
            p.setdefault(x,x)
            return p[x] if x==p[x] else f(p[x])
        def u(a,b):
            x = f(a)
            y = f(b)
            if x>y:
                p[x] = y
            else:
                p[y] = x
        for a,b in zip(s1,s2):
            u(a,b)
        return ''.join(f(c) for c in baseStr)

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        p = {}
        f = lambda x: p.setdefault(x,x) and (p[x] if x==p[x] else f(p[x]))
        u = lambda a,b: p.__setitem__(x if (x:=f(a))>(y:=f(b)) else y, y if x>y else x)
        any(u(a,b) for a,b in zip(s1,s2))
        return ''.join(f(c) for c in baseStr)

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        return (p:={},f:=lambda x: p.setdefault(x,x) and (p[x] if x==p[x] else f(p[x])),u:=lambda a,b:
        p.__setitem__(x if (x:=f(a))>(y:=f(b)) else y, y if x>y else x),any(u(a,b) for a,b in zip(s1,s2))) and ''.join(f(c) for c in baseStr)


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        return (p:={},f:=lambda x:p.setdefault(x,x) and (p[x] if x==p[x] else f(p[x])),[p.__setitem__(max(f(a),f(b)),min(f(a),f(b))) for a,b in zip(s1,s2)]) and ''.join(f(c) for c in baseStr)

test('''

1061. Lexicographically Smallest Equivalent String
Medium

925

67

Add to List

Share
You are given two strings of the same length s1 and s2 and a string baseStr.

We say s1[i] and s2[i] are equivalent characters.

For example, if s1 = "abc" and s2 = "cde", then we have 'a' == 'c', 'b' == 'd', and 'c' == 'e'.
Equivalent characters follow the usual rules of any equivalence relation:

Reflexivity: 'a' == 'a'.
Symmetry: 'a' == 'b' implies 'b' == 'a'.
Transitivity: 'a' == 'b' and 'b' == 'c' implies 'a' == 'c'.
For example, given the equivalency information from s1 = "abc" and s2 = "cde", "acd" and "aab" are equivalent strings of baseStr = "eed", and "aab" is the lexicographically smallest equivalent string of baseStr.

Return the lexicographically smallest equivalent string of baseStr by using the equivalency information from s1 and s2.

 

Example 1:

Input: s1 = "parker", s2 = "morris", baseStr = "parser"
Output: "makkek"
Explanation: Based on the equivalency information in s1 and s2, we can group their characters as [m,p], [a,o], [k,r,s], [e,i].
The characters in each group are equivalent and sorted in lexicographical order.
So the answer is "makkek".
Example 2:

Input: s1 = "hello", s2 = "world", baseStr = "hold"
Output: "hdld"
Explanation: Based on the equivalency information in s1 and s2, we can group their characters as [h,w], [d,e,o], [l,r].
So only the second letter 'o' in baseStr is changed to 'd', the answer is "hdld".
Example 3:

Input: s1 = "leetcode", s2 = "programs", baseStr = "sourcecode"
Output: "aauaaaaada"
Explanation: We group the equivalent characters in s1 and s2 as [a,o,e,r,s,c], [l,p], [g,t] and [d,m], thus all letters in baseStr except 'u' and 'd' are transformed to 'a', the answer is "aauaaaaada".
 

Constraints:

1 <= s1.length, s2.length, baseStr <= 1000
s1.length == s2.length
s1, s2, and baseStr consist of lowercase English letters.

''')


