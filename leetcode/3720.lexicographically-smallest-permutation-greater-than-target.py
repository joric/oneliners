from lc import *

# https://leetcode.com/problems/lexicographically-smallest-permutation-greater-than-target/solutions/7285200/5-lines-codeeasiest-explanation-by-c_pra-cxmf/?envType=daily-question&envId=2026-08-27

class Solution: # TLE
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        return next((p for p in sorted(''.join(c) for c in permutations(s)) if p > target), "")

class Solution:
    def lexGreaterPermutation(self, s: str, t: str) -> str:
        return(f:=lambda a,b:(x:=b[:1])and x in a and(r:=f(a.replace(x,'',1),b[1:]))and x+r or next((c+a.replace(c,'',1)for c in a if c>x),''))(''.join(sorted(s)),t)

class Solution:
    def lexGreaterPermutation(self, s: str, t: str) -> str:
        return(f:=lambda a,b:next((y for c in sorted({*a})if c>=b[:1]and(y:=c+f(a.replace(c,'',1),b[1:]*(c==b[:1])))>b),''))(s,t)

class Solution:
    def lexGreaterPermutation(self, s: str, t: str) -> str:
        return(f:=lambda a,b:next((y for c in sorted({*a})if c>=b[:1]and(y:=c+f(a.replace(c,'',1),b[1:]*(c==b[:1])))>b),''))(s,t)

test('''
3720. Lexicographically Smallest Permutation Greater Than Target
Medium
Topics
premium lock icon
Companies
Hint
You are given two strings s and target, both having length n, consisting of lowercase English letters.

Return the lexicographically smallest permutation of s that is strictly greater than target. If no permutation of s is lexicographically strictly greater than target, return an empty string.

A string a is lexicographically strictly greater than a string b (of the same length) if in the first position where a and b differ, string a has a letter that appears later in the alphabet than the corresponding letter in b.

 

Example 1:

Input: s = "abc", target = "bba"

Output: "bca"

Explanation:

The permutations of s (in lexicographical order) are "abc", "acb", "bac", "bca", "cab", and "cba".
The lexicographically smallest permutation that is strictly greater than target is "bca".
Example 2:

Input: s = "leet", target = "code"

Output: "eelt"

Explanation:

The permutations of s (in lexicographical order) are "eelt", "eetl", "elet", "elte", "etel", "etle", "leet", "lete", "ltee", "teel", "tele", and "tlee".
The lexicographically smallest permutation that is strictly greater than target is "eelt".
Example 3:

Input: s = "baba", target = "bbaa"

Output: ""

Explanation:

The permutations of s (in lexicographical order) are "aabb", "abab", "abba", "baab", "baba", and "bbaa".
None of them is lexicographically strictly greater than target. Therefore, the answer is "".
 

Constraints:

1 <= s.length == target.length <= 300
s and target consist of only lowercase English letters.
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
13,581/50.8K
Acceptance Rate
26.8%
Topics
Staff
Hash Table
String
Greedy
Counting
Enumeration
Weekly Contest 472
icon
Companies
Hint 1
Maintain frequency counts of s.
Hint 2
Walk left-to-right; if equal to target[i] is possible, take it and continue.
Hint 3
If not, try the smallest letter strictly greater than target[i].
Hint 4
If neither, backtrack left to the most recent index where you matched target and try to bump there.
''')
