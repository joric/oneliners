from lc import *

# https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        d = {"a":0, "e":1,"i":2,"o":3,"u":4}
        mask=0
        pos={0:-1}
        best=0
        for i,c in enumerate(s):
            if c in d:
                mask ^= (1<<d[c])
            if mask not in pos:
                pos[mask]=i
            else:
                best=max(best, i-pos[mask])
        return best

# https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/discuss/531840/JavaC%2B%2BPython-One-Pass

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        r=x=0
        v={0:-1}
        for i,c in enumerate(s):
            x ^= 1<<('aeiou'.find(c)+1)>>1
            v.setdefault(x, i)
            r = max(r,i-v[x])
        return r

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        x,v=0,{0:-1};return max((x:=x^1<<('aeiou'.find(c)+1)>>1,v.setdefault(x,i))and i-v[x]for i,c in enumerate(s))

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        x=i=0;v={0:0};return max((x:=x^1<<('aeiou'.find(c)+1)>>1,v.setdefault(x,i:=i+1))and i-v[x]for c in s)

test('''
1371. Find the Longest Substring Containing Vowels in Even Counts
Medium

1634

60

Add to List

Share
Given the string s, return the size of the longest substring containing each vowel an even number of times. That is, 'a', 'e', 'i', 'o', and 'u' must appear an even number of times.

 

Example 1:

Input: s = "eleetminicoworoep"
Output: 13
Explanation: The longest substring is "leetminicowor" which contains two each of the vowels: e, i and o and zero of the vowels: a and u.
Example 2:

Input: s = "leetcodeisgreat"
Output: 5
Explanation: The longest substring is "leetc" which contains two e's.
Example 3:

Input: s = "bcbcbc"
Output: 6
Explanation: In this case, the given string "bcbcbc" is the longest because all vowels: a, e, i, o and u appear zero times.
 

Constraints:

1 <= s.length <= 5 x 10^5
s contains only lowercase English letters.
Accepted
28,805
Submissions
44,730
''')
