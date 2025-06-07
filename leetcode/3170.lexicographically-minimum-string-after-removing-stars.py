from lc import *

# https://leetcode.com/problems/lexicographically-minimum-string-after-removing-stars/solutions/5253494/python-3-four-lines-using-heapq/?envType=daily-question&envId=2025-06-07

class Solution:
    def clearStars(self, s: str) -> str:
        h=[];[heappop(h)if c=='*'else heappush(h,(c,-i))for i,c in enumerate(s)];return''.join(c for c,_ in sorted(h,key=lambda x:-x[1]))

class Solution:
    def clearStars(self, s: str) -> str:
        h=[];[heappush(h,(c,-i))if c>'*'else heappop(h)for i,c in enumerate(s)];return''.join(c for c,_ in sorted(h,key=lambda x:-x[1]))

test('''
3170. Lexicographically Minimum String After Removing Stars
Solved
Medium
Topics
premium lock icon
Companies
You are given a string s. It may contain any number of '*' characters. Your task is to remove all '*' characters.

While there is a '*', do the following operation:

Delete the leftmost '*' and the smallest non-'*' character to its left. If there are several smallest characters, you can delete any of them.
Return the lexicographically smallest resulting string after removing all '*' characters.

 

Example 1:

Input: s = "aaba*"

Output: "aab"

Explanation:

We should delete one of the 'a' characters with '*'. If we choose s[3], s becomes the lexicographically smallest.

Example 2:

Input: s = "abc"

Output: "abc"

Explanation:

There is no '*' in the string.

 

Constraints:

1 <= s.length <= 105
s consists only of lowercase English letters and '*'.
The input is generated such that it is possible to delete all '*' characters.
Seen this question in a real interview before?
1/5
Yes
No
Accepted
33,549/89.5K
Acceptance Rate
37.5%
Topics
Hash Table
String
Stack
Greedy
Heap (Priority Queue)
''')
