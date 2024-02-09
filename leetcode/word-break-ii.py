from lc import *

class Solution:
    def wordBreak(self, s: str, d: List[str]) -> List[str]:
        m = {len(s): ['']}
        def f(i):
            if i not in m:
                m[i] = [s[i:j] + (t and ' ' + t) for j in range(i+1,len(s)+1) if s[i:j] in d for t in f(j)]
            return m[i]
        return f(0)

# https://leetcode.com/submissions/detail/1170088569/

class Solution:
    def wordBreak(self, s: str, d: List[str]) -> List[str]:
        def f(s,t=()):
            if not s:
                yield' '.join(t)
                return
            for w in d:
                if s.startswith(w):
                    yield from f(s[len(w):],t+(w,))
        return f(s)

# https://leetcode.com/submissions/detail/1170092705/

class Solution:
    def wordBreak(self, s: str, d: List[str]) -> List[str]:
        def f(s,t=()):
            if not s:
                return [' '.join(t)]
            r = []
            for w in d:
                if s.startswith(w):
                    r += f(s[len(w):],t+(w,))
            return r
        return f(s)

class Solution:
    def wordBreak(self, s: str, d: List[str]) -> List[str]:
        return(f:=lambda s,t=():sum((f(s[len(w):],t+(w,))for w in d if s.startswith(w)),start=[])if s else[' '.join(t)])(s)

class Solution:
    def wordBreak(self, s: str, d: List[str]) -> List[str]:
        return(f:=lambda s,t=():sum((f(s[len(w):],t+(w,))for w in d if w==s[:len(w)]),start=[])if s else[' '.join(t)])(s)

# https://leetcode.com/problems/word-break-ii/discuss/764188/Python-4-lines-using-lru_cache

class Solution:
    def wordBreak(self, s: str, d: List[str]) -> List[str]:
        return(f:=lambda i:[s[i:j]+(e and' '+e)for j in range(i+1,len(s)+1)if s[i:j]in d for e in f(j)]if s[i:]else[''])(0)

class Solution:
    def wordBreak(self, s: str, d: List[str]) -> List[str]:
        return(f:=lambda s:[s[:j]+(e and' '+e)for j in range(len(s)+1)if s[:j]in d for e in f(s[j:])]if s else[''])(s)

class Solution:
    def wordBreak(self, s: str, d: List[str]) -> List[str]:
        q=[(s,'')];return{*[r[1:]for s,r in q for w in d if w==s[:(l:=len(w))]and q.append((s[l:],r+' '+w))or''==s]}

test('''
140. Word Break II
Hard

6646

525

Add to List

Share
Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]
Example 2:

Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: []
 

Constraints:

1 <= s.length <= 20
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 10
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
Input is generated in a way that the length of the answer doesn't exceed 105.
Accepted
561,170
Submissions
1,185,897
''', check=lambda r,e,*args:sorted(r)==sorted(e))

