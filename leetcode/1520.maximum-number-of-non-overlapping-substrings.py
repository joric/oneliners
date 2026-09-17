from lc import *

# https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/solutions/744726/python-easy-to-read-solution-with-explan-jz6k/?envType=daily-question&envId=2026-09-18

class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        ranges = {c: (s.rindex(c), s.index(c)) for c in set(s)}
        for c in set(s):
            r, l = ranges[c]
            r_, l_ = -1, -1
            while not (r_ == r and l_ == l):
                r_, l_ = r, l
                r = max(ranges[c][0] for c in set(s[l:r+1]))
                l = min(ranges[c][1] for c in set(s[l:r+1]))
            ranges[c] = (r, l)

        ans, curr = [], 0
        for r, l in sorted(ranges.values()):
            if l >= curr:
                ans.append(s[l:r+1])
                curr = r
        return ans

class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        d={c:[s.rfind(c),s.find(c)]for c in set(s)};[d.update({c:[max(d[x][0]for x in u),min(d[x][1]for x in u)]})for _ in d for c in d for u in[set(s[d[c][1]:d[c][0]+1])]];m=-1;return[s[l:r+1]for r,l in sorted(d.values())if l>m and[m:=r]]

class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        d={c:[s.rfind(c),s.find(c)]for c in s};[d.update({c:[max(d[x][0]for x in u),min(d[x][1]for x in u)]})for _ in d for c in d for u in[{*s[d[c][1]:d[c][0]+1]}]];m=-1;return[s[l:r+1]for r,l in sorted(d.values())if l>m<(m:=r)]

test('''
1520. Maximum Number of Non-Overlapping Substrings
Hard
Topics
premium lock icon
Companies
Hint
Given a string s of lowercase letters, you need to find the maximum number of non-empty substrings of s that meet the following conditions:

The substrings do not overlap, that is for any two substrings s[i..j] and s[x..y], either j < x or i > y is true.
A substring that contains a certain character c must also contain all occurrences of c.
Find the maximum number of substrings that meet the above conditions. If there are multiple solutions with the same number of substrings, return the one with minimum total length. It can be shown that there exists a unique solution of minimum total length.

Notice that you can return the substrings in any order.

 

Example 1:

Input: s = "adefaddaccc"
Output: ["e","f","ccc"]
Explanation: The following are all the possible substrings that meet the conditions:
[
  "adefaddaccc"
  "adefadda",
  "ef",
  "e",
  "f",
  "ccc",
]
If we choose the first string, we cannot choose anything else and we'd get only 1. If we choose "adefadda", we are left with "ccc" which is the only one that doesn't overlap, thus obtaining 2 substrings. Notice also, that it's not optimal to choose "ef" since it can be split into two. Therefore, the optimal way is to choose ["e","f","ccc"] which gives us 3 substrings. No other solution of the same number of substrings exist.
Example 2:

Input: s = "abbaccd"
Output: ["d","bb","cc"]
Explanation: Notice that while the set of substrings ["d","abba","cc"] also has length 3, it's considered incorrect since it has larger total length.
 

Constraints:

1 <= s.length <= 105
s contains only lowercase English letters.
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
29,310/66.3K
Acceptance Rate
44.2%
Topics
icon
Companies
Hint 1
Notice that it's impossible for any two valid substrings to overlap unless one is inside another.
Hint 2
We can start by finding the starting and ending index for each character.
Hint 3
From these indices, we can form the substrings by expanding each character's range if necessary (if another character exists in the range with smaller/larger starting/ending index).
Hint 4
Sort the valid substrings by length and greedily take those with the smallest length, discarding the ones that overlap those we took.
Similar Questions
Maximum Number of Non-overlapping Palindrome Substrings
Hard
''', sort=True)
