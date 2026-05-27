from lc import *

# https://leetcode.com/problems/longest-common-suffix-queries/solutions/8294056/trie-backward-by-anhkind-jd8b/

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        A = sorted([(w, i) for i, w in enumerate(wordsContainer)], key=lambda a: (len(a[0]), a[1]))
        trie = {'$': A[0][1]}
        for w, idx in A:
            node = trie
            for i in range(len(w) - 1, -1, -1):
                c = w[i]
                if c not in node: node[c] = {'$': idx}
                node = node[c]
        res = []
        for w in wordsQuery:
            node = trie
            for i in range(len(w) - 1, -1, -1):
                c = w[i]
                if c not in node: break
                node = node[c]
            res.append(node['$'])
        return res

# my solution

class Solution:
    def stringIndices(self, c: List[str], q: List[str]) -> List[int]:
        t=(T:=lambda:defaultdict(T))();e='$';s='|'
        for i,w in enumerate(c):
            n=t
            for x in s+w[::-1]:
                n=n[x]
                (e not in n or(len(c[n[e]]),n[e])>(len(w),i))and setitem(n,e,i)
        def f(w):
            n=t[s]
            for x in w[::-1]:
                if x not in n:
                    break
                n=n[x]
            return n[e]
        return[*map(f,q)]

class Solution:
    def stringIndices(self, c: List[str], q: List[str]) -> List[int]:
        t=(T:=lambda:defaultdict(T))();e='$';s='|';[(n:=t,[(n:=n[x],({e}-{*n}or(len(c[n[e]]),n[e])>(len(w),i))and setitem(n,e,i))for x in s+w[::-1]])for i,w in enumerate(c)];return[*map(f:=lambda w:(n:=t[s],any({x}-{*n}or[n:=n[x]]<[]for x in w[::-1]),n[e])[2],q)]

class Solution:
    def stringIndices(self, c: List[str], q: List[str]) -> List[int]:
        t=(T:=lambda:defaultdict(T))();[(n:=t,[setitem(n:=n[x],'$',-i)for x in'|'+w[::-1]])for _,i,w in sorted((-len(w),-i,w)for i,w in enumerate(c))];return[(n:=t['|'],all(x in n and[n:=n[x]]for x in w[::-1]),n['$'])[2]for w in q]

class Solution:
    def stringIndices(self, c: List[str], q: List[str]) -> List[int]:
        t=(T:=lambda:defaultdict(T))();[(n:=t,[setitem(n:=n[x],'$',-i)for x in'|'+w[::-1]])for _,i,w in sorted((-len(w),-i,w)for i,w in enumerate(c))];return[n['$']for w in q if(n:=t['|'],all(x in n and[n:=n[x]]for x in w[::-1]))]

test('''
3093. Longest Common Suffix Queries
Hard
Topics
premium lock icon
Companies
Hint
You are given two arrays of strings wordsContainer and wordsQuery.

For each wordsQuery[i], you need to find a string from wordsContainer that has the longest common suffix with wordsQuery[i]. If there are two or more strings in wordsContainer that share the longest common suffix, find the string that is the smallest in length. If there are two or more such strings that have the same smallest length, find the one that occurred earlier in wordsContainer.

Return an array of integers ans, where ans[i] is the index of the string in wordsContainer that has the longest common suffix with wordsQuery[i].

 

Example 1:

Input: wordsContainer = ["abcd","bcd","xbcd"], wordsQuery = ["cd","bcd","xyz"]

Output: [1,1,1]

Explanation:

Let's look at each wordsQuery[i] separately:

For wordsQuery[0] = "cd", strings from wordsContainer that share the longest common suffix "cd" are at indices 0, 1, and 2. Among these, the answer is the string at index 1 because it has the shortest length of 3.
For wordsQuery[1] = "bcd", strings from wordsContainer that share the longest common suffix "bcd" are at indices 0, 1, and 2. Among these, the answer is the string at index 1 because it has the shortest length of 3.
For wordsQuery[2] = "xyz", there is no string from wordsContainer that shares a common suffix. Hence the longest common suffix is "", that is shared with strings at index 0, 1, and 2. Among these, the answer is the string at index 1 because it has the shortest length of 3.
Example 2:

Input: wordsContainer = ["abcdefgh","poiuygh","ghghgh"], wordsQuery = ["gh","acbfgh","acbfegh"]

Output: [2,0,2]

Explanation:

Let's look at each wordsQuery[i] separately:

For wordsQuery[0] = "gh", strings from wordsContainer that share the longest common suffix "gh" are at indices 0, 1, and 2. Among these, the answer is the string at index 2 because it has the shortest length of 6.
For wordsQuery[1] = "acbfgh", only the string at index 0 shares the longest common suffix "fgh". Hence it is the answer, even though the string at index 2 is shorter.
For wordsQuery[2] = "acbfegh", strings from wordsContainer that share the longest common suffix "gh" are at indices 0, 1, and 2. Among these, the answer is the string at index 2 because it has the shortest length of 6.
 

Constraints:

1 <= wordsContainer.length, wordsQuery.length <= 104
1 <= wordsContainer[i].length <= 5 * 103
1 <= wordsQuery[i].length <= 5 * 103
wordsContainer[i] consists only of lowercase English letters.
wordsQuery[i] consists only of lowercase English letters.
Sum of wordsContainer[i].length is at most 5 * 105.
Sum of wordsQuery[i].length is at most 5 * 105.
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
15,007/41.9K
Acceptance Rate
35.8%
Topics
Senior Staff
Array
String
Trie
Weekly Contest 390
icon
Companies
Hint 1
If we reverse the strings, the problem changes to finding the longest common prefix.
Hint 2
Build a Trie, each node is a letter and only saves the best word’s index in each node, based on the criteria.
Similar Questions
Longest Common Prefix
Easy
Find the Length of the Longest Common Prefix
Medium
''')
