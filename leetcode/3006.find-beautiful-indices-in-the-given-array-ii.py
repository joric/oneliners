from lc import *

# https://leetcode.com/problems/find-beautiful-indices-in-the-given-array-ii/discuss/4561875/Python-Kmp-%2B-Two-Pointers-O(n)

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        v,w=[[m.start(0)for m in finditer('(?='+w+')',s)]for w in(a,b)] # finds overlaps but too slow
        return[x for x in v if bisect_left(w,x-k)<bisect_right(w,x+k)]

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        def kmp(s):
            p = [0] * len(s)
            for i in range(1, len(s)):
                c = p[i - 1]
                while c and s[i] != s[c]:
                    c = p[c - 1]
                p[i] = c + (s[i] == s[c])
            return p
        v,w = [[i-len(w)*2 for i,x in enumerate(kmp(w+'#'+s))if x>=len(w)]for w in (a,b)]
        r = []
        j = 0
        for i in v:
            while j < len(w) and w[j] < i - k:
                j += 1
            if j < len(w) and w[j] <= i + k:
                r.append(i)
        return r

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        def kmp(s):
            p = [0] * len(s)
            for i in range(1, len(s)):
                c = p[i - 1]
                while c and s[i] != s[c]:
                    c = p[c - 1]
                p[i] = c + (s[i] == s[c])
            return p
        v,w = [[i-len(w)*2 for i,x in enumerate(kmp(w+'#'+s))if x>=len(w)]for w in (a,b)]
        p = {x:bisect_left(w,x)for x in v}
        return sorted({x for x in v for j in(p[x],p[x]-1)if 0<=j<len(w)and abs(w[j]-x)<=k})

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        v,w=[[m.start()for m in finditer(w,s)]for w in(a,b)]
        r = set()
        for x in v:
            i = bisect_left(w,x)
            for j in(i-1,i):
                if 0<=j<len(w) and abs(w[j]-x)<=k:
                    r.add(x)
        return sorted(r)

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        v,w=[[m.start()for m in finditer(w,s)]for w in(a,b)];p={x:bisect_left(w,x)for x in v};return sorted({x for x in v for j in(p[x],p[x]-1)if 0<=j<len(w)and abs(w[j]-x)<=k})

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        f=lambda s:((p:=[0]*len(s),[setitem(p,i,next((c+(s[i]==s[c])for _ in count() if not(c and s[i]!=s[c]and(c:=p[c-1]))),c:=p[i-1]))for i in range(1,len(s))])and p)
        v,w=[[i-len(w)*2 for i,x in enumerate(f(w+'#'+s))if x>=len(w)]for w in (a,b)]
        p={x:bisect_left(w,x)for x in v}
        return sorted({x for x in v for j in(p[x],p[x]-1)if 0<=j<len(w)and abs(w[j]-x)<=k})

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        f=lambda s:((p:=[0]*len(s),[setitem(p,i,next((c+(s[i]==s[c])for _ in count() if not(c and s[i]!=s[c]and(c:=p[c-1]))),c:=p[i-1]))for i in range(1,len(s))])and p);v,w=[[i-len(w)*2 for i,x in enumerate(f(w+'#'+s))if x>=len(w)]for w in (a,b)];p={x:bisect_left(w,x)for x in v};return sorted({x for x in v for j in(p[x],p[x]-1)if 0<=j<len(w)and abs(w[j]-x)<=k})

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        def kmp(s):
            p = [0] * len(s)
            for i in range(1, len(s)):
                c = p[i - 1]
                while c and s[i] != s[c]:
                    c = p[c - 1]
                p[i] = c + (s[i] == s[c])
            return p
        v,w = [[i-len(w)*2 for i,x in enumerate(kmp(w+'#'+s))if x>=len(w)]for w in(a,b)]
        return[x for x in v if bisect_left(w,x-k)!=bisect_right(w,x+k)]

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        f=lambda s:((p:=[0]*len(s),[setitem(p,i,next((c+(s[i]==s[c])for _ in s if not(c and s[i]!=s[c]and(c:=p[c-1]))),c:=p[i-1]))for i in range(1,len(s))])and p)
        v,w=[[i-len(w)*2 for i,x in enumerate(f(w+'#'+s))if x>=len(w)]for w in(a,b)]
        return[x for x in v if bisect_left(w,x-k)<bisect_right(w,x+k)]

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        f=lambda s:((p:=[0]*len(s),[setitem(p,i,next((c+(s[i]==s[c])for _ in s if not(c and s[i]!=s[c]and(c:=p[c-1]))),c:=p[i-1]))for i in range(1,len(s))])and p);v,w=[[i-len(w)*2 for i,x in enumerate(f(w+'#'+s))if x>=len(w)]for w in(a,b)];w+=[inf];return[x for x in v if w[bisect_left(w,x-k)]<=x+k]

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        def rk(s,w):
            m = 6752341
            b = 998244353
            c = 0
            n = len(w)
            h = reduce(lambda h,c:(h*b+ord(c))%m,w,0)
            return[i-n+1 for i in range(len(s))if h==(c:=((c*b+ord(s[i]))-(i>=n and ord(s[i-n])*pow(b,n,m)or 0))%m)]
        v,w = map(rk,(s,s),(a,b))
        return[x for x in v if bisect_left(w,x-k)<bisect_right(w,x+k)]

# rabin-karp

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        v,w=map(lambda s,w:(m:=6752341,b:=998244353,c:=0,n:=len(w),h:=reduce(lambda h,c:(h*b+ord(c))%m,w,0))and[i-n+1for i in range(len(s))if h==(c:=((c*b+ord(s[i]))-(i>=n and ord(s[i-n])*pow(b,n,m)or 0))%m)],(s,s),(a,b));w+=[inf];return[x for x in v if w[bisect_left(w,x-k)]<=x+k]

test('''
3006. Find Beautiful Indices in the Given Array I
Medium

29

10

Add to List

Share
You are given a 0-indexed string s, a string a, a string b, and an integer k.

An index i is beautiful if:

0 <= i <= s.length - a.length
s[i..(i + a.length - 1)] == a
There exists an index j such that:
0 <= j <= s.length - b.length
s[j..(j + b.length - 1)] == b
|j - i| <= k
Return the array that contains beautiful indices in sorted order from smallest to largest.

 

Example 1:

Input: s = "isawsquirrelnearmysquirrelhouseohmy", a = "my", b = "squirrel", k = 15
Output: [16,33]
Explanation: There are 2 beautiful indices: [16,33].
- The index 16 is beautiful as s[16..17] == "my" and there exists an index 4 with s[4..11] == "squirrel" and |16 - 4| <= 15.
- The index 33 is beautiful as s[33..34] == "my" and there exists an index 18 with s[18..25] == "squirrel" and |33 - 18| <= 15.
Thus we return [16,33] as the result.

Example 2:

Input: s = "abcd", a = "a", b = "a", k = 4
Output: [0]
Explanation: There is 1 beautiful index: [0].
- The index 0 is beautiful as s[0..0] == "a" and there exists an index 0 with s[0..0] == "a" and |0 - 0| <= 4.
Thus we return [0] as the result.

Example 3:

Input: s = "bavgoc", a = "ba", b = "c", k = 6
Output: [0]

Example 4:

Input: s = "ababababazzabababb", a = "aba", b = "bb", k = 10
Output: [6,11,13]

Example 5:
Input: s = "uefac", a = "aaasa", b = "a", k = 5
Output: []

Example 6:

Input: s = "dc", a = "dreec", b = "dc", k = 2
Output: []


Example 6:

Input: s = "snwj", a = "snwj", b = "ry", k = 1
Output: []

Example 7:

Input: s = "onwawarwar", a = "wa", b = "r", k = 2
Output: [4,7]

Constraints:

1 <= k <= s.length <= 10^5
1 <= a.length, b.length <= 10
s, a, and b contain only lowercase English letters.
Accepted
13,326
Submissions
41,633
''')