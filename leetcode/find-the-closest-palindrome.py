from lc import *

# https://leetcode.com/problems/find-the-closest-palindrome/discuss/3416727/Python-3-lines-with-comments-oror-Case-by-Case

class Solution:
    def nearestPalindromic(self, n: str) -> str:
        if(len(n)==1):
            return str(int(n)-1)
        def build(x): return x[:(len(x)+1)//2] + x[:len(x)//2][::-1]
        cands = [build(n),
            str(10**(len(n)-1)-1),
            str(10**(len(n)-1)+1),
            str(10**(len(n))-1), 
            str(10**(len(n))+1),
            build(str(int(n)-(10**((len(n))//2 )))),
            build(str(int(n)+(10**((len(n))//2 ))))]
        vals = [(abs(int(n)-int(x)),int(x)) for x in cands if x!=n]
        return str(min(vals)[1])

# https://leetcode.com/problems/find-the-closest-palindrome/discuss/102391/Python-Simple-with-Explanation

class Solution:
    def nearestPalindromic(self, S):
        K = len(S)
        candidates = [str(10**k + d) for k in (K-1, K) for d in (-1, 1)]
        prefix = S[:(K+1)//2]
        P = int(prefix)
        for start in map(str, (P-1, P, P+1)):
            candidates.append(start + (start[:-1] if K%2 else start)[::-1])
        def delta(x):
            return abs(int(S) - int(x))
        ans = None
        for cand in candidates:
            if cand != S and not cand.startswith('00'):
                if (ans is None or delta(cand) < delta(ans) or
                        delta(cand) == delta(ans) and int(cand) < int(ans)):
                    ans = cand
        return ans

class Solution:
    def nearestPalindromic(self, s: str) -> str:
        n = len(s)
        p = int(s[:-~n//2])
        f = lambda x:abs(int(s)-int(x))
        d = [str(10**k+d)for k in(n-1,n)for d in(-1,1)]+[x+(x[:-1]if n%2 else x)[::-1]for x in map(str,(p-1,p,p+1))]
        r=0
        [c!=s and not c.startswith('00')and(not r or f(c)<f(r)or f(c)==f(r)and int(c)<int(r))and(r:=c)for c in d]
        return r

class Solution:
    def nearestPalindromic(self, s: str) -> str:
        n,r,f=len(s),0,lambda x:abs(int(s)-int(x));p=int(s[:-~n//2]);d=[str(10**k+d)for k in(n-1,n)for d in(-1,1)]+[x+(x[:-1]if n%2 else x)[::-1]for x in map(str,(p-1,p,p+1))];[c!=s and not c.startswith('00')and(not r or f(c)<f(r)or f(c)==f(r)and int(c)<int(r))and(r:=c)for c in d];return r

test('''
564. Find the Closest Palindrome
Hard

900

1519

Add to List

Share
Given a string n representing an integer, return the closest integer (not including itself), which is a palindrome. If there is a tie, return the smaller one.

The closest is defined as the absolute difference minimized between two integers.

 

Example 1:

Input: n = "123"
Output: "121"
Example 2:

Input: n = "1"
Output: "0"
Explanation: 0 and 2 are the closest palindromes but we return the smallest which is 0.
 

Constraints:

1 <= n.length <= 18
n consists of only digits.
n does not have leading zeros.
n is representing an integer in the range [1, 1018 - 1].
Accepted
62,899
Submissions
249,013
Seen this question in a real interview before?

Yes

No
Find Palindrome With Fixed Length
Medium
Next Palindrome Using Same Digits
Hard
Find the Largest Palindrome Divisible by K
Hard
Will brute force work for this problem? Think of something else.
Take some examples like 1234, 999,1000, etc and check their closest palindromes. How many different cases are possible?
Do we have to consider only left half or right half of the string or both?
Try to find the closest palindrome of these numbers- 12932, 99800, 12120. Did you observe something?
''')
