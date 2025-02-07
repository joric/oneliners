from lc import *

# testcase issue for sorting?
# https://github.com/LeetCode-Feedback/LeetCode-Feedback/issues/20113

# The following tests do not pass leetcode solver

# loveleetcode
# 221424411214

# eeeelolovtcd
# 444422221111

# eeeeoollvtdc
# 444422221111

# faulty tests below

class Solution:
    def frequencySort(self, s: str) -> str:
        return''.join(sorted(s,key=lambda x:-Counter(s)[x]))

class Solution:
    def frequencySort(self, s: str) -> str:
        return''.join(sorted(s,key=lambda c:-s.count(c)))

class Solution:
    def frequencySort(self, s: str) -> str:
        return''.join(sorted(s,key=Counter(s).get)[::-1])

# https://leetcode.com/problems/sort-characters-by-frequency

class Solution:
    def frequencySort(self, s: str) -> str:
        return''.join(v*k for k,v in Counter(s).most_common())

class Solution:
    def frequencySort(self, s: str) -> str:
        return''.join(starmap(mul,Counter(s).most_common()))


test('''

451. Sort Characters By Frequency
Medium

5214

203

Add to List

Share
Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.

 

Example 1:

Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Example 2:

Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.

Example 3:

Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.

Example 4:
Input: s = "loveleetcode"
Output: "eeeeoollvtdc"

Constraints:

1 <= s.length <= 5 * 10^5
s consists of uppercase and lowercase English letters and digits.

''',
    #check=lambda res,exp,s:(g:=set(),c:=Counter(res),f:=inf) and next((0 for a,_ in groupby(res) if a in g or c[a]>f or not (f:=c[a],g.add(a))),c==Counter(s))
    check = lambda r,_,s:sorted(r)==sorted(s)and[*Counter(r).values()]==sorted(Counter(s).values())[::-1]
)