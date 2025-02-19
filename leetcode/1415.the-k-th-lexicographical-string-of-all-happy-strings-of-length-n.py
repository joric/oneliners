from lc import *

# Q3 https://leetcode.com/contest/biweekly-contest-24/
# https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        self.res = ''
        self.count = 0
        def next(s, n, k):
            if self.res!='':
                return self.res
            if len(s)==n:
                self.count += 1
                if self.count==k:
                    self.res = s
                return
            prev = s[-1] if len(s) else ''
            for c in ('a','b','c'):
                if c != prev:
                    next(s+c, n, k)
        next('',n, k)
        return self.res if self.count==k else ''

# https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/discuss/688639/Python-One-Line-O(n)-solution-(97-Faster-70-Less-Mem)

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        return '' if k > [0,3][n>0] * 2**(n-1) else [l + ''.join([l[i+1] for i in range(n-1) if (k:=k-(ns//(2**i)) * (k // (ns//(2**i)))) != None and (l:=l+['bc', 'ac', 'ab'][('b'==l[-1]) + ('c'==l[-1])*2][k//(ns//(2**(i+1)))])]) for _ in [0] if (ns:=([0,3][n>0] * 2**(n-1))//3)!=None and (k:=k-1)!=None and (l:=['a', 'b', 'c'][k//ns])][0]

# Claude 3.5 (fixed)

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def f(p,l):
            if l==0:
                self.c+=1
                if self.c==k:self.r=p
                return
            for i in'abc':
                if not p or i!=p[-1]:
                    f(p+i,l-1)
                    if self.r:return
        self.c=self.r=0
        f('',n)
        return(self.r,'')[self.c<k]

# https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/discuss/1210921/Python-simple-solution-no-recursion

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        pos, k = 2 ** (n - 1), k -1
        if k >= pos * 3:
            return ''
        letters = {
            ('' , 0): 'a',
            ('' , 1): 'b',
            ('' , 2): 'c',
            ('a', 0): 'b',
            ('a', 1): 'c',
            ('b', 0): 'a',
            ('b', 1): 'c',
            ('c', 0): 'a',
            ('c', 1): 'b'
        }
        result = ['']
        while pos > 0:
            result.append(letters[(result[-1], k // pos)])
            k = k % pos
            pos = pos // 2
        return ''.join(result)

# https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/discuss/688639/Python-One-Line-O(n)-solution-(97-Faster-70-Less-Mem)

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        return '' if k > [0,3][n>0] * 2**(n-1) else [l + ''.join([l[i+1] for i in range(n-1) if (k:=k-(ns//(2**i)) * (k // (ns//(2**i)))) != None and (l:=l+['bc', 'ac', 'ab'][('b'==l[-1]) + ('c'==l[-1])*2][k//(ns//(2**(i+1)))])]) for _ in [0] if (ns:=([0,3][n>0] * 2**(n-1))//3)!=None and (k:=k-1)!=None and (l:=['a', 'b', 'c'][k//ns])][0]

# https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/discuss/1404881/4-line-Python-no-list

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        return next(islice(filter(lambda s:not any(2*x in s for x in'abc'),(''.join(p)for p in product('abc',repeat=n))),k-1,k),'')

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        return next(islice((''.join(p)for p in product('abc',repeat=n)if all(2*x not in''.join(p)for x in'abc')),k-1,k),'')

# https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/solutions/5533528/a-lazy-4-line-bfs/?envType=daily-question&envId=2025-02-19

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        r=[''];[r:=[s+c for s in r for c in'abc'if s[-1:]!=c]for _ in range(n)];return(r[k-1:]or[''])[0]

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        r=[''];[r:=[s+c for s in r for c in'abc'if s[-1:]!=c]for _ in[0]*n];return(r[k-1:]or[''])[0]

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        r=[''];[r:=[s+c for s in r for c in'abc'if s[-1:]!=c]for _ in r*n];return(r[k-1:]+[''])[0]

test('''
1415. The k-th Lexicographical String of All Happy Strings of Length n
Medium

962

26

Add to List

Share
A happy string is a string that:

consists only of letters of the set ['a', 'b', 'c'].
s[i] != s[i + 1] for all values of i from 1 to s.length - 1 (string is 1-indexed).
For example, strings "abc", "ac", "b" and "abcbabcbcb" are all happy strings and strings "aa", "baa" and "ababbc" are not happy strings.

Given two integers n and k, consider a list of all happy strings of length n sorted in lexicographical order.

Return the kth string of this list or return an empty string if there are less than k happy strings of length n.

 

Example 1:

Input: n = 1, k = 3
Output: "c"
Explanation: The list ["a", "b", "c"] contains all happy strings of length 1. The third string is "c".
Example 2:

Input: n = 1, k = 4
Output: ""
Explanation: There are only 3 happy strings of length 1.
Example 3:

Input: n = 3, k = 9
Output: "cab"
Explanation: There are 12 different happy string of length 3 ["aba", "abc", "aca", "acb", "bab", "bac", "bca", "bcb", "cab", "cac", "cba", "cbc"]. You will find the 9th string = "cab"
 

Constraints:

1 <= n <= 10
1 <= k <= 100
Accepted
40,133
Submissions
53,675
''')