from lc import *

# https://leetcode.com/problems/uncommon-words-from-two-sentences/discuss/723882/Clean-python-one-line

class Solution:
    def uncommonFromSentences(self, a: str, b: str) -> List[str]:
        return[x for x in(a+' '+b).split()if(a+' '+b).split().count(x)<2]

# https://leetcode.com/problems/uncommon-words-from-two-sentences/discuss/376648/Python-one-line

class Solution:
    def uncommonFromSentences(self, a: str, b: str) -> List[str]:
        return[k for k,v in Counter(a.split()+b.split()).items()if v<2]

# https://leetcode.com/problems/uncommon-words-from-two-sentences/discuss/158967/C%2B%2BJavaPython-Easy-Solution-with-Explanation

class Solution:
    def uncommonFromSentences(self, a: str, b: str) -> List[str]:
        return[k for k,v in Counter((a+' '+b).split()).items() if v<2]

class Solution:
    def uncommonFromSentences(self, a: str, b: str) -> List[str]:
        c=Counter(a.split()+b.split());return[w for w in c if c[w]<2]

class Solution:
    def uncommonFromSentences(self, a: str, b: str) -> List[str]:
        c=Counter((a+' '+b).split());return[w for w in c if c[w]<2]

test('''
884. Uncommon Words from Two Sentences
Easy

1451

176

Add to List

Share
A sentence is a string of single-space separated words where each word consists only of lowercase letters.

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.

 

Example 1:

Input: s1 = "this apple is sweet", s2 = "this apple is sour"

Output: ["sweet","sour"]

Explanation:

The word "sweet" appears only in s1, while the word "sour" appears only in s2.

Example 2:

Input: s1 = "apple apple", s2 = "banana"

Output: ["banana"]

 

Constraints:

1 <= s1.length, s2.length <= 200
s1 and s2 consist of lowercase English letters and spaces.
s1 and s2 do not have leading or trailing spaces.
All the words in s1 and s2 are separated by a single space.
Accepted
176,217
Submissions
251,006
''')
