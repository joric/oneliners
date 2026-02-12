from lc import *

# https://leetcode.com/problems/longest-balanced-substring-i/solutions/7268243/longest-balanced-substring-by-pramit_sam-6cmg/?envType=daily-question&envId=2026-02-12

class Solution:
    def longestBalanced(self, s: str) -> int:
        pt = s
        ml = 0
        n = len(pt)
        for left in range(n):
            freq = Counter()
            for right in range(left,n):
                freq[pt[right]]+=1
                counts = list(freq.values())
                if len(set(counts)) == 1:
                    ml = max(ml,right-left+1)
        return ml

# https://leetcode.com/problems/longest-balanced-substring-i/solutions/7572443/easy-python-solution-by-sb012-71hh/?envType=daily-question&envId=2026-02-12

class Solution:
    def longestBalanced(self, s: str) -> int:
        s = list(s)
        a = 0
        for i in range(len(s)):
            c = {}
            for j in range(i, len(s)):
                c[s[j]] = c.get(s[j], 0) + 1
                e = c[s[j]]
                if all(c[k] == e for k in c):
                    a = max(a, j - i + 1)
        return a

class Solution:
    def longestBalanced(self, s: str) -> int:
        return max(max(j-i+1 for j in range(i,len(s))if(setitem(c,s[j],c.get(s[j],0)+1)or all(c[k]==c[s[j]]for k in c)))for i in range(len(s))if[c:={}])

class Solution:
    def longestBalanced(self, s: str) -> int:
        return max(max(j+1 for j,x in enumerate(s[i:])if(setitem(c,x,c.get(x,0)+1)or all(c[k]==c[x]for k in c)))for i in range(len(s))if[c:={}])

class Solution:
    def longestBalanced(self, s: str) -> int:
        return max(max(j+1 for j,x in enumerate(s[i:])if c.update([x])or len({*c.values()})<2)for i in range(len(s))if[c:=Counter()])

test('''
3713. Longest Balanced Substring I
Medium
Topics
premium lock icon
Companies
Hint
You are given a string s consisting of lowercase English letters.

A substring of s is called balanced if all distinct characters in the substring appear the same number of times.

Return the length of the longest balanced substring of s.

 

Example 1:

Input: s = "abbac"

Output: 4

Explanation:

The longest balanced substring is "abba" because both distinct characters 'a' and 'b' each appear exactly 2 times.

Example 2:

Input: s = "zzabccy"

Output: 4

Explanation:

The longest balanced substring is "zabc" because the distinct characters 'z', 'a', 'b', and 'c' each appear exactly 1 time.​​​​​​​

Example 3:

Input: s = "aba"

Output: 2

Explanation:

​​​​​​​One of the longest balanced substrings is "ab" because both distinct characters 'a' and 'b' each appear exactly 1 time. Another longest balanced substring is "ba".

 

Constraints:

1 <= s.length <= 1000
s consists of lowercase English letters.
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
36,736/66K
Acceptance Rate
55.7%
Topics
Senior
Hash Table
String
Counting
Enumeration
Weekly Contest 471
icon
Companies
Hint 1
Use bruteforce over all substrings
''')
