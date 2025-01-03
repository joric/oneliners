from lc import *

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def similar(s1,s2)-> bool:
            return sum([s1[i]!=s2[i] for i in range(len(s1))]) <=2
        def find(v):
            if nodes[v] != v:
                nodes[v] = find(nodes[v])
            return nodes[v]
        edges = []
        for i in range(len(strs)-1):
            for j in range(i+1,len(strs)):
                if similar(strs[i],strs[j]):
                    edges.append([i,j])
        nodes = [i for i in range(len(strs))]
        for i, j in edges:
            nodes[find(i)] = find(j)
        return len(set(map(find, nodes)))

class Solution:
    def numSimilarGroups(self, s: List[str]) -> int:
        return (e:=[],n:=[*range(len(s))],p:=lambda a,b:sum([c!=b[i] for i,c in enumerate(a)])<=2,f:=lambda v:
        (n[v]!=v and setitem(n,v,f(n[v])),n[v])[1],[p(s[i],s[j]) and e.append([i,j]) for i in range(len(s)-1) 
        for j in range(i+1,len(s))],[setitem(n,f(i),f(j)) for i,j in e]) and len(set(map(f,n)))

class Solution:
    def numSimilarGroups(self, s: List[str]) -> int:
        return (n:=[*range(m:=len(s))],f:=lambda v:(n[v]!=v and setitem(n,v,f(n[v])),n[v])[1],[setitem(n,f(i),f(j))
        for i in range(m) for j in range(i+1,m) if sum(x!=y for x,y in zip(s[i],s[j]))<3]) and len(set(map(f,n)))


# numpy

import numpy as np

class Solution:
    def numSimilarGroups(self, s):
        m = 999
        T = ''.join(map(chr, range(m)))
        n = len(s)
        for i in range(n):
            for j in range(n):
                if sum(starmap(ne,zip(s[i],s[j])))<3:
                    T = T.replace(T[i],T[j])
        return n-m+len(set(T))

class Solution:
    def numSimilarGroups(self, s: List[str]) -> int:
        return len(set(map(tuple,(np.matrix([[sum([x!=y for x,y in zip(a,b)])<=2 for a in s] for b in s],'bool')**99).A)))

class Solution:
    def numSimilarGroups(self, s: List[str]) -> int:
        return len(np.unique(np.matrix([[sum(starmap(ne,zip(a,b)))<3 for a in s] for b in s])**99,axis=0))

# inline numpy

class Solution:
    def numSimilarGroups(self, s: List[str]) -> int:
        return len(set(map(tuple,(__import__('numpy').matrix([[sum([x!=y for x,y in zip(a,b)])<=2 for a in s] for b in s],'bool')**99).A)))

class Solution:
    def numSimilarGroups(self, s: List[str]) -> int:
        return len(set(map(tuple,(__import__('numpy').matrix([[sum(starmap(ne,zip(a,b)))<=2 for a in s] for b in s],'bool')**99).A)))

class Solution:
    def numSimilarGroups(self, s: List[str]) -> int:
        return len(set(map(tuple,(__import__('numpy').matrix([[sum(starmap(ne,zip(a,b)))<3 for a in s] for b in s])**99).A)))

test('''
839. Similar String Groups
Hard

1064

184

Add to List

Share
Two strings X and Y are similar if we can swap two letters (in different positions) of X, so that it equals Y. Also two strings X and Y are similar if they are equal.

For example, "tars" and "rats" are similar (swapping at positions 0 and 2), and "rats" and "arts" are similar, but "star" is not similar to "tars", "rats", or "arts".

Together, these form two connected groups by similarity: {"tars", "rats", "arts"} and {"star"}.  Notice that "tars" and "arts" are in the same group even though they are not similar.  Formally, each group is such that a word is in the group if and only if it is similar to at least one other word in the group.

We are given a list strs of strings where every string in strs is an anagram of every other string in strs. How many groups are there?

 

Example 1:

Input: strs = ["tars","rats","arts","star"]
Output: 2
Example 2:

Input: strs = ["omv","ovm"]
Output: 1
 

Constraints:

1 <= strs.length <= 300
1 <= strs[i].length <= 300
strs[i] consists of lowercase letters only.
All words in strs have the same length and are anagrams of each other.
Accepted
64,613
Submissions
134,400
Seen this question in a real interview before?

Yes

No
Groups of Strings
''')
