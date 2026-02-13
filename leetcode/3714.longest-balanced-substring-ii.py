from lc import *

# https://leetcode.com/problems/longest-balanced-substring-ii/solutions/7268494/python-prefix-sum-by-lee215-gram/?envType=daily-question&envId=2026-02-13

class Solution:
    def longestBalanced(self, s: str) -> int:
        def test(s):
            def diff():
                return tuple(count[c] - count[chs[0]] for c in chs)
            chs = list(set(s))
            count = Counter()
            pos = {diff(): -1}
            res = 0
            for i, c in enumerate(s):
                count[c] += 1
                d = diff()
                if d in pos:
                    res = max(res, i - pos[d])
                else:
                    pos[d] = i
            return res

        res1 = max(len(list(it)) for c, it in groupby(s))
        res2 = max(test(s2) for c in 'abc' for s2 in s.split(c))
        res3 = test(s)
        return max(res1, res2, res3)


class Solution:
    def longestBalanced(self, s: str) -> int:
        def f(s):
            g = lambda:tuple(c[x]-c[t[0]] for x in t)
            t = [*{*s}]
            c = Counter()
            p = {g(): -1}
            r = 0
            for i,x in enumerate(s):
                c.update([x])
                d = g()
                if d in p:
                    r = max(r, i - p[d])
                else:
                    p[d] = i
            return r
        return max(max(len([*g])for c,g in groupby(s)),max(f(y)for x in 'abc' for y in s.split(x)),f(s))

# https://leetcode.com/problems/longest-balanced-substring-ii/solutions/7268216/python-prefix-sum-by-awice-tcso/?envType=daily-question&envId=2026-02-13

class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        p = [[0, 0, 0]]
        for c in s:
            p.append(p[-1][:])
            p[-1]["abc".index(c)] += 1
        r = 0
        d = {}
        for i,(a,b,c) in enumerate(p):
            for k in [("abc",a-b,a-c),("ab",a-b,c),("bc",b-c,a),("ca",c-a,b),("a",b,c),("b",c,a),("c",a,b)]:
                r = max(r,i-d.get(k,i))
                d.setdefault(k,i)
        return r


# https://leetcode.com/problems/longest-balanced-substring-ii/solutions/7574739/python-simple-approach-prefix-sum-by-yas-75bv/?envType=daily-question&envId=2026-02-13

class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        p = [[0, 0, 0]]
        for c in s:
            p.append(p[-1][:])
            p[-1]["abc".index(c)] += 1

        ans = 0
        m = {}
        for i, (a, b, c) in enumerate(p):
            for k in [
                (-1, a - b, a - c), # a,b,c
                (-2, a - b, c),     # a,b
                (-3, b - c, a),     # b,c
                (-4, c - a, b),     # a,c
                (-5, b, c),         # a
                (-6, c, a),         # b
                (-7, a, b),         # c
            ]:
                if not k in m: m[k] = i
                else: ans = max(ans, i - m[k])
        return ans

class Solution:
    def longestBalanced(self, s: str) -> int:
        p,d=[[0,0,0]],{};[p.append(p[-1][:])or setitem(p[-1],t:='abc'.index(c),p[-1][t]+1)for c in s];return max(i-d[k]for i,(a,b,c) in enumerate(p)for j,p in enumerate([(a-b,a-c),(a-b,c),(b-c,a),(c-a,b),(b,c),(c,a),(a,b)])if[d.setdefault(k:=(~j,*p),i)])

class Solution:
    def longestBalanced(self, s: str) -> int:
        p,d=[[0,0,0]],{};[p.append(t:=p[-1][:])or setitem(t,k:=ord(c)%3-1,t[k]+1)for c in s];return max(i-d.setdefault((j,u),i)for i,(a,b,c)in enumerate(p)for j,u in enumerate([(a-b,b-c),(a-b,c),(b-c,a),(c-a,b),(b,c),(c,a),(a,b)]))

class Solution:
    def longestBalanced(self, s: str) -> int:
        p,d,e=[[0]*3],{},enumerate;[p.append(t:=p[-1][:])or setitem(t,k:=ord(c)%3,t[k]+1)for c in s];return max(i-d.setdefault((j,u),i)for i,(a,b,c)in e(p)for j,u in e(((a-b,b-c),(a-b,c),(b-c,a),(c-a,b),(b,c),(c,a),(a,b))))

class Solution:
    def longestBalanced(self, s: str) -> int:
        p,d,e=[0]*3,{},enumerate;return max(i-d.setdefault((j,u),i)for i,x in e('#'+s)if i<1 or[setitem(p,k:=ord(x)%3,p[k]+1)]for a,b,c in[p]for j,u in e(((a-b,b-c),(a-b,c),(b-c,a),(c-a,b),(b,c),(c,a),(a,b))))

class Solution:
    def longestBalanced(self, s: str) -> int:
        p,d,e=[0]*3,{},enumerate;return max(i-d.setdefault((j,u),i)for i,x in e('#'+s)if[setitem(p,k:=ord(x)%3,p[k]+1)]for a,b,c in[p]for j,u in e(((a-b,b-c),(a-b,c),(b-c,a),(c-a,b),(b,c),(c,a),(a,b))))


test('''
3714. Longest Balanced Substring II
Medium
Topics
premium lock icon
Companies
Hint
You are given a string s consisting only of the characters 'a', 'b', and 'c'.

A substring of s is called balanced if all distinct characters in the substring appear the same number of times.

Return the length of the longest balanced substring of s.

 

Example 1:

Input: s = "abbac"

Output: 4

Explanation:

The longest balanced substring is "abba" because both distinct characters 'a' and 'b' each appear exactly 2 times.

Example 2:

Input: s = "aabcc"

Output: 3

Explanation:

The longest balanced substring is "abc" because all distinct characters 'a', 'b' and 'c' each appear exactly 1 time.

Example 3:

Input: s = "aba"

Output: 2

Explanation:

One of the longest balanced substrings is "ab" because both distinct characters 'a' and 'b' each appear exactly 1 time. Another longest balanced substring is "ba".

 

Constraints:

1 <= s.length <= 105
s contains only the characters 'a', 'b', and 'c'.
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
11,088/48.6K
Acceptance Rate
22.8%
Topics
Staff
Hash Table
String
Prefix Sum
Weekly Contest 471
icon
Companies
Hint 1
Solve for three cases: all-equal characters, exactly two distinct characters, and all three characters present. Treat each case separately and take the maximum length.
Hint 2
Case 1: single character: the longest balanced substring is the longest run of the same character; report its length.
Hint 3
Case 2: two distinct characters: reduce to that pair (ignore the third character) and use prefix differences of their counts; equal counts between two indices mean the substring between them is balanced for those two chars.
Hint 4
Case 3: all three characters: use prefix counts and hash the pair (count_b - count_a, count_c - count_a) for each prefix; if the same pair appears at two indices the substring between them has equal counts for a, b, and c. Store earliest index per pair to get maximal length.
''')
