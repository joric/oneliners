from lc import *

# https://leetcode.com/problems/substring-with-largest-variance/discuss/2551276/Python-super-clean-solution

class Solution:
    def largestVariance(self, s: str) -> int:
        r = 0
        q = Counter(s)
        for x,y in permutations(set(s), 2):
            if q[x]==1:
                continue
            p = 0
            d = -len(s)
            for c in s:
                if c==x:
                    p += 1
                    d += 1
                elif c==y:
                    p -= 1
                    d = p 
                    if p<0:
                        p = 0
                if r<d:
                    r = d
        return r

class Solution:
    def largestVariance(self, s: str) -> int:
        r,q=0,Counter(s);[(p:=0,d:=-len(s),[(c==x and(p:=p+1,d:=d+1)or c==y and(p:=p-1,d:=p,p<0 and(p:=0)),r<d and(r:=d))for c in s])for x,y in permutations(set(s),2)if q[x]!=1];return r

# faster but 182 chars longer
class Solution:
    def largestVariance(self, s: str) -> int:
        q = defaultdict(lambda:[])
        for i,c in enumerate(s):
            q[c].append(i)
        r = 0
        for a,b in itertools.combinations(q,2):
            x,y = -1,-1
            m,g = Counter(),Counter()
            c = 0
            for i,j in enumerate(sorted(q[a]+q[b])):
                if s[j]==a:
                    x=i
                    c+=1
                elif s[j]==b:
                    y=i
                    c-=1
                k = min(x,y)
                if k>=0:
                    r = max(r, c-m[k-1], g[k-1]-c)
                m[i]=min(m[i-1],c)
                g[i]=max(g[i-1],c)
        return r

class Solution:
    def largestVariance(self, s: str) -> int:
        r,q=0,defaultdict(lambda:[]);[q[c].append(i)for i,c in enumerate(s)];[(x:=--1,y:=-1,m:=Counter(),g:=Counter(),c:=0,[(s[j]==a and(x:=i,c:=c+1)or(s[j]==b and(y:=i,c:=c-1)),(k:=min(x,y))>=0 and(r:=max(r,c-m[k-1],g[k-1]-c)),setitem(m,i,min(m[i-1],c)),setitem(g,i,max(g[i-1],c)))for i,j in enumerate(sorted(q[a]+q[b]))])for a,b in itertools.combinations(q,2)];return r

test('''
2272. Substring With Largest Variance
Hard

789

94

Add to List

Share
The variance of a string is defined as the largest difference between the number of occurrences of any 2 characters present in the string. Note the two characters may or may not be the same.

Given a string s consisting of lowercase English letters only, return the largest variance possible among all substrings of s.

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: s = "aababbb"
Output: 3
Explanation:
All possible variances along with their respective substrings are listed below:
- Variance 0 for substrings "a", "aa", "ab", "abab", "aababb", "ba", "b", "bb", and "bbb".
- Variance 1 for substrings "aab", "aba", "abb", "aabab", "ababb", "aababbb", and "bab".
- Variance 2 for substrings "aaba", "ababbb", "abbb", and "babb".
- Variance 3 for substring "babbb".
Since the largest possible variance is 3, we return it.
Example 2:

Input: s = "abcde"
Output: 0
Explanation:
No letter occurs more than once in s, so the variance of every substring is 0.

Example 3:

Input: s = "icexiahccknibwuwgi"
Output: 3

Example 4:
Input: s = "lripaa"
Output: 1

Constraints:

1 <= s.length <= 10^4
s consists of lowercase English letters.
''')

