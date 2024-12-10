from lc import *

# https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-i/discuss/4484793/Python-3-oror-7-lines-groupby-and-dict-oror-TS%3A-85-54

class Solution:
    def maximumLength(self, s: str) -> int:
        d = defaultdict(int)
        subs = [''.join(sub) for _, sub in groupby(s)]
        for sub in subs:
            d[sub]+= 1
            if len(sub) > 1: d[sub[1:]]+= 2
            if len(sub) > 2: d[sub[2:]]+= 3
        return max(map(len,filter(lambda x: d[x] > 2, d)), default = -1)

# https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-i/discuss/4482510/ON3-Brute-Force-%2B-Explanation

class Solution(object):
    def maximumLength(self, s):
        c = Counter()
        res = -1
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                t = s[i:j]
                if len(set(t)) == 1:
                    c[t] += 1
                    if c[t] >= 3:
                        res = max(res,len(t))
        return res

class Solution:
    def maximumLength(self, s: str) -> int:
        d=Counter();return max([-1]+[len(t)for i,j in combinations(range(len(s)+1),2)if 2>len(set(t:=s[i:j]))and d.update([t])or d[t]>2])

test('''
2981. Find Longest Special Substring That Occurs Thrice I
Medium

192

14

Add to List

Share
You are given a string s that consists of lowercase English letters.

A string is called special if it is made up of only a single character. For example, the string "abc" is not special, whereas the strings "ddd", "zz", and "f" are special.

Return the length of the longest special substring of s which occurs at least thrice, or -1 if no special substring occurs at least thrice.

A substring is a contiguous non-empty sequence of characters within a string.

 

Example 1:

Input: s = "aaaa"
Output: 2
Explanation: The longest special substring which occurs thrice is "aa": substrings "aaaa", "aaaa", and "aaaa".
It can be shown that the maximum length achievable is 2.
Example 2:

Input: s = "abcdef"
Output: -1
Explanation: There exists no special substring which occurs at least thrice. Hence return -1.
Example 3:

Input: s = "abcaba"
Output: 1
Explanation: The longest special substring which occurs thrice is "a": substrings "abcaba", "abcaba", and "abcaba".
It can be shown that the maximum length achievable is 1.
 

Other examples:

Input: s = "lkwwdddddnnnnnynnnnl"
Output: 4

Constraints:

3 <= s.length <= 50
s consists of only lowercase English letters.
Accepted
25,670
Submissions
58,163
''')
