from lc import *

# https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/solutions/4974961/magic-one-line-solution-by-charnavoki-6dm5/?envType=daily-question&envId=2026-09-30
# maxDepthAfterSplit = (s, arr = s.split(''), c = 0) => arr.map(($, i) => (s[i] === "(" ? ++c : c--) % 2);

# https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/solutions/6525508/c-one-liner-by-ilya-a-f-t4ep/?envType=daily-question&envId=2026-09-30
# public int[] MaxDepthAfterSplit(string seq) => seq.Select((c, i) => (c + i) % 2).ToArray();

def check(a, _, s) -> bool:
    d, c, D, M = [0, 0], 0, 0, 0
    for x, i in zip(s, a):
        v = 1 if x == '(' else -1
        d[i] += v; c += v
        if d[i] < 0: return False
        D, M = max(D, c), max(M, d[i])
    return len(a) == len(s) and d == [0, 0] and M == (D + 1) // 2

class Solution:
    def maxDepthAfterSplit(self, s: str) -> List[int]:
        return[i+ord(c)&1for i,c in enumerate(s)]

class Solution:
    def maxDepthAfterSplit(self, s: str) -> List[int]:
        i=0;return[(i:=i+1)+ord(c)&1for c in s]

test('''
1111. Maximum Nesting Depth of Two Valid Parentheses Strings
Medium
Topics
premium lock icon
Companies
A string is a valid parentheses string (denoted VPS) if and only if it consists of "(" and ")" characters only, and:

It is the empty string, or
It can be written as AB (A concatenated with B), where A and B are VPS's, or
It can be written as (A), where A is a VPS.
We can similarly define the nesting depth depth(S) of any VPS S as follows:

depth("") = 0
depth(A + B) = max(depth(A), depth(B)), where A and B are VPS's
depth("(" + A + ")") = 1 + depth(A), where A is a VPS.
For example, "", "()()", and "()(()())" are VPS's (with nesting depths 0, 1, and 2), and ")(" and "(()" are not VPS's.

Given a VPS seq, split it into two disjoint subsequences A and B, such that A and B are VPS's (and A.length + B.length = seq.length). The subsequences may not necessarily be contiguous.

For example, for the sequence 123456789, one possible split is:

A = {1, 3, 5, 7, 9},

B = {2, 4, 6, 8}.

This corresponds to the output [0, 1, 0, 1, 0, 1, 0, 1, 0]  where 0 indicates membership in A and 1 indicates membership in B.

Now choose any such A and B such that max(depth(A), depth(B)) is the minimum possible value.

Return an answer array (of length seq.length) that encodes such a choice of A and B:  answer[i] = 0 if seq[i] is part of A, else answer[i] = 1.  Note that even though multiple answers may exist, you may return any of them.

 

Example 1:

Input: seq = "(()())"
Output: [0,1,1,1,1,0]
Example 2:

Input: seq = "()(())()"
Output: [0,0,0,1,1,0,1,1]
 

Constraints:

1 <= seq.size <= 10000
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
36,481/50.3K
Acceptance Rate
72.5%
Topics
Senior Staff
String
Stack
Bracket Sequences
Weekly Contest 144
icon
Companies
Similar Questions
Maximum Nesting Depth of the Parentheses
Easy
''')
