from lc import *

# https://leetcode.com/problems/word-ladder-ii/

class Solution:
    def findLadders(self, b: str, e: str, wl: list[str]) -> list[list[str]]:
        def f(w,c,d=defaultdict(list)):
            if not c: 
                return []
            if e in c:
                return [[e]]
            w -= c
            n = set()
            for x in c:
                for y in ascii_lowercase:
                    for i in range(len(b)):
                        z = x[:i] + y + x[i + 1:]
                        if z in w:
                            d[z].append(x)
                            n.add(z)
            return [[a] + t for t in f(w,n,d) for a in d[t[0]]]
        return f(set(wl), {b})

class Solution:
    def findLadders(self, b: str, e: str, w: list[str]) -> list[list[str]]:
        return(f:=lambda w,c,d=defaultdict(list):c and([[e]]if e in c else(w:=w-c,n:=set(),[(z:=x[:i]+y+x[i+1:])in w and(d[z].append(x),n.add(z))for x in c for y in ascii_lowercase for i in range(len(b))])and[[a]+t for t in f(w,n,d)for a in d[t[0]]])or[])(set(w),{b})

test('''
126. Word Ladder II
Solved
Hard
Topics
premium lock icon
Companies
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return all the shortest transformation sequences from beginWord to endWord, or an empty list if no such sequence exists. Each sequence should be returned as a list of the words [beginWord, s1, s2, ..., sk].

 

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
Explanation: There are 2 shortest transformation sequences:
"hit" -> "hot" -> "dot" -> "dog" -> "cog"
"hit" -> "hot" -> "lot" -> "log" -> "cog"
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: []
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
 

Constraints:

1 <= beginWord.length <= 5
endWord.length == beginWord.length
1 <= wordList.length <= 500
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the words in wordList are unique.
The sum of all shortest transformation sequences does not exceed 105.
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
450,411/1.6M
Acceptance Rate
27.5%
Topics
Hash Table
String
Backtracking
Breadth-First Search
icon
Companies
Similar Questions
Word Ladder
Hard
Groups of Strings
Hard
''', sort=True)
