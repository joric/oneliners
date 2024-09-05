from lc import *

# https://leetcode.com/problems/replace-words/discuss/2474325/Python-solution-or-Two-lines

class Solution:
    def replaceWords(self, d: List[str], s: str) -> str:
        p= '|'.join(sorted(d));return' '.join(search(p,w).group(0) if search(p, w) and w.startswith(search(p,w).group(0)) else w for w in s.split())

# https://leetcode.com/problems/replace-words/discuss/2418342/7-Lines-of-simple-python-code-or-Only-For-Loops

class Solution:
    def replaceWords(self, d: List[str], s: str) -> str:
        p = [*s.split()]
        for j in range(len(p)):
            for w in d:
                if w==p[j][:len(w)]:
                    p[j] = w
        return ' '.join(p)

class Solution:
    def replaceWords(self, d: List[str], s: str) -> str:
        return' '.join(next((t for t in sorted(d) if w[:len(t)]==t),0)or w for w in s.split())

class Solution:
    def replaceWords(self, d: List[str], s: str) -> str:
        d.sort();return' '.join(next(filter(w.startswith,d),0)or w for w in s.split())

# https://leetcode.com/problems/replace-words/discuss/105763/One-Line-Regex-Solution-Java-and-JavaScript

class Solution:
    def replaceWords(self, d: List[str], s: str) -> str:
        return re.sub(f'\\b({"|".join(sorted(d))})\w+','\\1',s)

test('''
648. Replace Words
Medium

2234

174

Add to List

Share
In English, we have a concept called root, which can be followed by some other word to form another longer word - let's call this word derivative. For example, when the root "help" is followed by the word "ful", we can form a derivative "helpful".

Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the derivatives in the sentence with the root forming it. If a derivative can be replaced by more than one root, replace it with the root that has the shortest length.

Return the sentence after the replacement.

 

Example 1:

Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"
Example 2:

Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
Output: "a a b c"
 

Other examples:

Input: dictionary = ["a", "aa", "aaa", "aaaa"], sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"
Output: "a a a a a a a a bbb baba a"

Input: dictionary = ["catt","cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"

Constraints:

1 <= dictionary.length <= 1000
1 <= dictionary[i].length <= 100
dictionary[i] consists of only lower-case letters.
1 <= sentence.length <= 106
sentence consists of only lower-case letters and spaces.
The number of words in sentence is in the range [1, 1000]
The length of each word in sentence is in the range [1, 1000]
Every two consecutive words in sentence will be separated by exactly one space.
sentence does not have leading or trailing spaces.
Accepted
139,617
Submissions
221,855
''')