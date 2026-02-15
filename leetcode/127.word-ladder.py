from lc import *

# https://leetcode.com/problems/word-ladder/submissions/639558350/

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0
        n = len(beginWord)
        d = defaultdict(list)
        for w in wordList:
            for i in range(n):
                d[w[:i] + "*" + w[i+1:]].append(w)
        q = collections.deque([(beginWord, 1)])
        v = {beginWord: True}
        while q:
            cw, l = q.popleft()
            for i in range(n):
                iw = cw[:i] + "*" + cw[i+1:]
                for w in d[iw]:
                    if w == endWord:
                        return l + 1
                    if w not in v:
                        v[w] = True
                        q.append((w, l + 1))
                d[iw] = []
        return 0

class Solution:
    def ladderLength(self, b: str, e: str, w: list[str]) -> list[list[str]]:
        return len(min((f:=lambda w,c,d=defaultdict(list):c and([[e]]if e in c else(w:=w-c,n:=set(),[(z:=x[:i]+y+x[i+1:])in w and(d[z].append(x),n.add(z))for x in c for y in ascii_lowercase for i in range(len(b))])and[[a]+t for t in f(w,n,d)for a in d[t[0]]])or[])(set(w),{b}),default=[]))

test('''
127. Word Ladder
Solved
Hard
Topics
premium lock icon
Companies
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

 

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
 

Constraints:

1 <= beginWord.length <= 10
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the words in wordList are unique.
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
1,559,205/3.5M
Acceptance Rate
44.8%
Topics
Hash Table
String
Breadth-First Search
icon
Companies
Similar Questions
Word Ladder II
Hard
Minimum Genetic Mutation
Medium
Words Within Two Edits of Dictionary
Medium
''')
