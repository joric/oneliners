from lc import *

# https://leetcode.com/problems/lexicographically-smallest-string-after-applying-operations/solutions/7279679/six-simple-lines-of-code/?envType=daily-question&envId=2025-10-19

class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        r,q=set(),deque([tuple(map(int,s))])
        while q:
            t = q.pop()
            for t in tuple((d+a)%10 for d,a in zip(t,cycle((0,a)))),t[-b:]+t[:-b]:
                if t not in r:
                    r.add(t)
                    q.append(t)
        return ''.join(map(str,min(r)))

class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        r=set();f=lambda t:[t not in r and(r.add(t),q.append(t))for t in(tuple((d+a)%10 for d,a in zip(t,cycle((0,a)))),t[-b:]+t[:-b])]and q and f(q.pop());f((q:=deque([tuple(map(int,s))])).pop());return ''.join(map(str,min(r)))

# https://leetcode.com/problems/lexicographically-smallest-string-after-applying-operations/solutions/3436071/python-3-12-lines-recursion-dfs-t-s-90-20/?envType=daily-question&envId=2025-10-19

class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        d,v = {c:str((int(c)+a)%10)for c in digits},set()
        def f(s: str) -> str:
            if s in v:
                return
            v.add(s)
            r = ''
            o = 1
            for c in s:
                o^= 1
                r+= d[c] if o else c
            f(r)
            f(s[b:]+s[:b])
        f(s)
        return min(v)

class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        d,v={c:str((int(c)+a)%10)for c in digits},set();f=lambda s:s not in v and(v.add(s),o:=1,f(''.join(d[c]if(o:=o^1)else c for c in s)),f(s[b:]+s[:b]))and v;return min(f(s))

test('''
1625. Lexicographically Smallest String After Applying Operations
Solved
Medium
Topics
premium lock icon
Companies
Hint
You are given a string s of even length consisting of digits from 0 to 9, and two integers a and b.

You can apply either of the following two operations any number of times and in any order on s:

Add a to all odd indices of s (0-indexed). Digits post 9 are cycled back to 0. For example, if s = "3456" and a = 5, s becomes "3951".
Rotate s to the right by b positions. For example, if s = "3456" and b = 1, s becomes "6345".
Return the lexicographically smallest string you can obtain by applying the above operations any number of times on s.

A string a is lexicographically smaller than a string b (of the same length) if in the first position where a and b differ, string a has a letter that appears earlier in the alphabet than the corresponding letter in b. For example, "0158" is lexicographically smaller than "0190" because the first position they differ is at the third letter, and '5' comes before '9'.

 

Example 1:

Input: s = "5525", a = 9, b = 2
Output: "2050"
Explanation: We can apply the following operations:
Start:  "5525"
Rotate: "2555"
Add:    "2454"
Add:    "2353"
Rotate: "5323"
Add:    "5222"
Add:    "5121"
Rotate: "2151"
Add:    "2050"​​​​​
There is no way to obtain a string that is lexicographically smaller than "2050".
Example 2:

Input: s = "74", a = 5, b = 1
Output: "24"
Explanation: We can apply the following operations:
Start:  "74"
Rotate: "47"
​​​​​​​Add:    "42"
​​​​​​​Rotate: "24"​​​​​​​​​​​​
There is no way to obtain a string that is lexicographically smaller than "24".
Example 3:

Input: s = "0011", a = 4, b = 2
Output: "0011"
Explanation: There are no sequence of operations that will give us a lexicographically smaller string than "0011".
 

Constraints:

2 <= s.length <= 100
s.length is even.
s consists of digits from 0 to 9 only.
1 <= a <= 9
1 <= b <= s.length - 1
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
34,663/47.4K
Acceptance Rate
73.2%
Topics
String
Depth-First Search
Breadth-First Search
Enumeration
Weekly Contest 211
icon
Companies
Hint 1
Since the length of s is even, the total number of possible sequences is at most 10 * 10 * s.length.
Hint 2
You can generate all possible sequences and take their minimum.
Hint 3
Keep track of already generated sequences so they are not processed again.
Similar Questions
Lexicographically Smallest String After Substring Operation
Medium
Lexicographically Smallest String After a Swap
Easy
''')
