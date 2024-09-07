from lc import *

# https://leetcode.com/problems/substring-with-concatenation-of-all-words/

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words: return []
        m, n, o, target = len(s), len(words), len(words[0]), []
        for i in range(m-n*o+1):
            word_target = words[:]
            for k in range(n):
                word = s[i+k*o:i+k*o+o]
                if word in word_target: word_target.remove(word)
                else: break
            if not word_target: target.append(i)
        return target

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        m,n,k,d=len(s),len(words),len(words[0]),Counter(words)
        def check(i,temp):
            for j in range(n):
                word=s[i+j*k:i+(j+1)*k]
                if not temp[word]:return False
                temp[word]-=1
            return True
        return [i for i in range(m-n*k+1) if check(i,d.copy())]

# https://leetcode.com/problems/substring-with-concatenation-of-all-words/discuss/2671278/Python-time-inefficient-(50)-but-1-line-short-solution

class Solution:
    def findSubstring(self, s: str, w: List[str]) -> List[int]:
        n,k,d=len(w),len(w[0]),sorted(w);return[i for i in range(len(s)-k*n+1)if d==sorted([s[i+j:i+j+k]for j in range(0,k*n,k)])]

test('''
30. Substring with Concatenation of All Words
Hard

1913

277

Add to List

Share
You are given a string s and an array of strings words. All the strings of words are of the same length.

A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.

For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.
Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.

 

Example 1:

Input: s = "barfoothefoobarman", words = ["foo","bar"]

Output: [0,9]

Explanation:

The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.

Example 2:

Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]

Output: []

Explanation:

There is no concatenated substring.

Example 3:

Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]

Output: [6,9,12]

Explanation:

The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"].
The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"].
The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"].

 

Constraints:

1 <= s.length <= 104
1 <= words.length <= 5000
1 <= words[i].length <= 30
s and words[i] consist of lowercase English letters.
Accepted
485,238
Submissions
1,490,767
''')
