from lc import *

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        c, res, w, m, n = Counter(p), [], None, len(s), len(p)
        for i in range(m-n+1):
            if i==0: 
                w = Counter(s[i:i+n])
            else:
                w -= {s[i-1]:1}
                w += {s[i+n-1]:1}
            if c==w:
                res.append(i)
        return res

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        return (lambda t:[i for i in range(len(s)-len(p)+1) if t==sorted(s[i:i+len(p)])])(sorted(p))

test('''

438. Find All Anagrams in a String
Medium

9655

294

Add to List

Share
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
 

Constraints:

1 <= s.length, p.length <= 3 * 10^4
s and p consist of lowercase English letters.

''')
