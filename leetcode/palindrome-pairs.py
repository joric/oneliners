from lc import *

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        index, res = {w: i for i, w in enumerate(words)}, set()
        for i, w in enumerate(words):
            for s in range(len(w) + 1):
                if w[s:][::-1] in index and w[:s] == w[:s][::-1] and index[w[s:][::-1]] != i and (index[w[s:][::-1]], i) not in res:
                    res.add((index[w[s:][::-1]], i))
            w = w[::-1]
            for s in range(len(w) + 1):
                if w[s:] in index and w[:s] == w[:s][::-1] and index[w[s:]] != i and (i, index[w[s:]]) not in res:
                    res.add((i, index[w[s:]]))
        return [[e[0], e[1]] for e in res]

# TLE
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        return (d := {w: i for i, w in enumerate(words)}) and (j:=lambda i, a, b: d.get(a == a[::-1] and b[::-1], i)) and [r for i, w in enumerate(words) for k in range(len(w) + 1) for r in ([i, j(i, w[k:], w[:k]) if w[k:] else i], [j(i, w[:k], w[k:]), i]) if r[0] != r[1]]

# TLE
class Solution:
    def palindromePairs(self, words):
        return [(g:=lambda d,a,b,f,i:set([(d[b],i) if f else (i,d[b])]) if a==a[::-1] and b in d and d[b]!=i else set(),fn:=lambda a,b: (a[0],a[1]|g(a[0],b[0],b[1][::-1],0,b[2])|g(a[0],b[1],b[0][::-1],1,b[2]))),reduce(fn, ((w[j:],w[:j],i) for i,w in enumerate(words) for j in range(len(w)+1)), [{w:i for i,w in enumerate(words)},set()])][1][1]

# https://leetcode.com/problems/palindrome-pairs/discuss/1282375/Python-5-lines-4-lines-3-lines-and-1-liner-from-case-to-case-basis-with-hashmap

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        isPalindrome, indexOf, res = lambda x: x == x[::-1] , {w:i for i,w in enumerate(words)}, []
        # case 1: empty string exists
        if '' in indexOf: res.extend([(indexOf[''],i) for i in range(len(words)) if isPalindrome(words[i])])
        # # case 2: reverse of a string exists
        res.extend([(i,indexOf[words[i][::-1]]) for i in range(len(words)) if words[i][::-1] in indexOf])
        # case 3: reverse of a prefix exists and suffix is palindrome  
        res.extend([(i,indexOf[words[i][:k][::-1]]) for i in range(len(words)) for k in range(len(words[i])) if words[i][:k][::-1] in indexOf and isPalindrome(words[i][k:])])
        # case 4: reverse of my suffix exists and prefix is palindrome
        res.extend([(indexOf[words[i][k:][::-1]],i) for i in range(len(words)) for k in range(len(words[i])) if words[i][k:][::-1] in indexOf and isPalindrome(words[i][:k])])
        return list(set([(i,j) for i,j in res if i!=j]))

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        isPalindrome, indexOf = lambda x: x == x[::-1] , {w:i for i,w in enumerate(words)}
        return list(set([(i,j) for i,j in [(indexOf[''],i) for i in range(len(words)) if isPalindrome(words[i]) and '' in indexOf]+[(i,indexOf[words[i][:k][::-1]]) for i in range(len(words)) for k in range(len(words[i])) if words[i][:k][::-1] in indexOf and isPalindrome(words[i][k:])]+[(indexOf[words[i][k:][::-1]],i) for i in range(len(words)) for k in range(len(words[i])) if words[i][k:][::-1] in indexOf and isPalindrome(words[i][:k])] if i!=j]))

class Solution:
    def palindromePairs(self, w: List[str]) -> List[List[int]]:
        return (p:=lambda x: x == x[::-1],o:={w:i for i,w in enumerate(w)}) and list(set([(i,j) for i,j in [(o[''],i)
            for i in range(len(w)) if p(w[i]) and '' in o]+[(i,o[w[i][:k][::-1]]) for i in range(len(w)) for k in range(len(w[i]))
            if w[i][:k][::-1] in o and p(w[i][k:])]+[(o[w[i][k:][::-1]],i) for i in range(len(w)) for k in range(len(w[i]))
            if w[i][k:][::-1] in o and p(w[i][:k])] if i!=j]))

test('''

336. Palindrome Pairs
Hard

4051

417

Add to List

Share
You are given a 0-indexed array of unique strings words.

A palindrome pair is a pair of integers (i, j) such that:

0 <= i, j < word.length,
i != j, and
words[i] + words[j] (the concatenation of the two strings) is a palindrome.
Return an array of all the palindrome pairs of words.

 

Example 1:

Input: words = ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
Explanation: The palindromes are ["abcddcba","dcbaabcd","slls","llssssll"]
Example 2:

Input: words = ["bat","tab","cat"]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["battab","tabbat"]
Example 3:

Input: words = ["a",""]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["a","a"]
 

Constraints:

1 <= words.length <= 5000
0 <= words[i].length <= 300
words[i] consists of lowercase English letters.

''',
check=lambda res,exp,s:(u:=lambda v: sorted(list(map(sorted,v))))(res)==u(exp)
)
