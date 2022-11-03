from lc import *

class Solution1:
    def longestPalindrome(self, words: List[str]) -> int:
        d = Counter(words)
        n=c=p=0
        for w in d:
            if w[0]==w[1]:
                n += d[w]//2*2
                if d[w]%2:
                    c = 2
            else:
                p += min(d[w],d[w[::-1]])*0.5
        return n*2 + c + 4*int(p)

class Solution2:
    def longestPalindrome(self, words: List[str]) -> int:
        return (lambda r:r[0]*2+r[1]+4*int(r[2]))(reduce(lambda a,w:(a[0]+d[w]//2*2, 2 if d[w]%2 else a[1],a[2])
            if w[0]==w[1] else (a[0],a[1],a[2]+min(d[w],d[w[::-1]])*0.5), (d:=Counter(words)), [0,0,0]))


class Solution3:
    def longestPalindrome(self, words: List[str]) -> int:
        c,r = Counter(), 0
        for w in words:
            if c[w[::-1]]>0:
                c[w[::-1]] -= 1
                r += 4
            else:
                c[w] += 1
        return r+2 if any(c[w]>0 and w[0]==w[1] for w in c) else r

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        return (r:=0, c:=Counter(), [(c.__setitem__(b,c[b]-1),r:=r+4) if (c[b:=a[::-1]]>0) else (c.__setitem__(a,c[a]+1)) for a in words]) and (r + 2*any(c[w]>0 and w[0]==w[1] for w in c))


test('''
2131. Longest Palindrome by Concatenating Two Letter Words
Medium

745

20

Add to List

Share
You are given an array of strings words. Each element of words consists of two lowercase English letters.

Create the longest possible palindrome by selecting some elements from words and concatenating them in any order. Each element can be selected at most once.

Return the length of the longest palindrome that you can create. If it is impossible to create any palindrome, return 0.

A palindrome is a string that reads the same forward and backward.

Example 1:

Input: words = ["lc","cl","gg"]
Output: 6
Explanation: One longest palindrome is "lc" + "gg" + "cl" = "lcggcl", of length 6.
Note that "clgglc" is another longest palindrome that can be created.

Example 2:

Input: words = ["ab","ty","yt","lc","cl","ab"]
Output: 8
Explanation: One longest palindrome is "ty" + "lc" + "cl" + "yt" = "tylcclyt", of length 8.
Note that "lcyttycl" is another longest palindrome that can be created.

Example 3:

Input: words = ["cc","ll","xx"]
Output: 2
Explanation: One longest palindrome is "cc", of length 2.
Note that "ll" is another longest palindrome that can be created, and so is "xx".

Example 4:

Input: words = ["qo","fo","fq","qf","fo","ff","qq","qf","of","of","oo","of","of","qf","qf","of"]
Output: 14

Constraints:

1 <= words.length <= 10^5
words[i].length == 2
words[i] consists of lowercase English letters.

''')
