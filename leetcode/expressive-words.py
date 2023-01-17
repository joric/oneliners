from lc import *

# https://leetcode.com/problems/expressive-words/discuss/122660/C%2B%2BJavaPython-2-Pointers-and-4-pointers

class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def f(v,w,j=0):
            for i in range(len(v)):
                if j<len(w) and a[i]==w[j]:
                    j += 1
                elif v[i-1:i+2] != v[i]*3 != v[i-2:i+1]:
                    return False
            return j==len(w)
        return sum(f(s,w) for w in words)

class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def f(v,w):
            i=j=p=q=0
            n,m = len(v), len(w)
            while i<n and j<m:
                if v[i]!=w[j]:
                    return False
                while p<n and v[p]==v[i]:
                    p += 1
                while q<m and w[q]==w[j]:
                    q += 1
                if p-i != q-j and p-i<max(3,q-j):
                    return False
                i,j = p,q
            return i==n and j==m
        return sum(f(s,w) for w in words)

# https://leetcode.com/problems/expressive-words/discuss/730428/Python-in-4-lines

class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        r = lambda w:((k, len(list(g))) for k,g in groupby(w))
        c = lambda a,b:a and b and (a==b or a[1]>=3 and a[1]>b[1])
        f = lambda v:all(c(a,b) for a,b in zip_longest(r(s),r(v)))
        return sum(map(f, words))


class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        return (r:=lambda w:((k,len(list(g))) for k,g in groupby(w))) and sum(map((f:=lambda v:all((c:=lambda a,b:a and b and (a==b or a[1]>=3 and a[1]>b[1]))(a,b) for a,b in zip_longest(r(s),r(v)))),words))

test('''
809. Expressive Words
Medium

778

1787

Add to List

Share
Sometimes people repeat letters to represent extra feeling. For example:

"hello" -> "heeellooo"
"hi" -> "hiiii"
In these strings like "heeellooo", we have groups of adjacent letters that are all the same: "h", "eee", "ll", "ooo".

You are given a string s and an array of query strings words. A query word is stretchy if it can be made to be equal to s by any number of applications of the following extension operation: choose a group consisting of characters c, and add some number of characters c to the group so that the size of the group is three or more.

For example, starting with "hello", we could do an extension on the group "o" to get "hellooo", but we cannot get "helloo" since the group "oo" has a size less than three. Also, we could do another extension like "ll" -> "lllll" to get "helllllooo". If s = "helllllooo", then the query word "hello" would be stretchy because of these two extension operations: query = "hello" -> "hellooo" -> "helllllooo" = s.
Return the number of query strings that are stretchy.

 

Example 1:

Input: s = "heeellooo", words = ["hello", "hi", "helo"]
Output: 1
Explanation: 
We can extend "e" and "o" in the word "hello" to get "heeellooo".
We can't extend "helo" to get "heeellooo" because the group "ll" is not size 3 or more.
Example 2:

Input: s = "zzzzzyyyyy", words = ["zzyy","zy","zyy"]
Output: 3
 

Constraints:

1 <= s.length, words.length <= 100
1 <= words[i].length <= 100
s and words[i] consist of lowercase letters.
''')
