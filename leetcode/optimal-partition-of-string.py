from lc import *

class Solution:
    def partitionString(self, s: str) -> int:
        d = set()
        r = 1
        for c in s:
            if c in d:
                d = set()
                r += 1
            d.add(c)
        return r

class Solution:
    def partitionString(self, s: str) -> int:
        return reduce(lambda p,c:c in p[1] and (p[0]+1,{c}) or (p[0],p[1]|{c}),s,[1,set()])[0]

class Solution:
    def partitionString(self, s: str) -> int:
        return (d:=set(),r:=1,all((c in d and (d:=set(),r:=r+1),d.add(c)) for c in s),r)[3]

test('''

2405. Optimal Partition of String
Medium

632

31

Add to List

Share
Given a string s, partition the string into one or more substrings such that the characters in each substring are unique. That is, no letter appears in a single substring more than once.

Return the minimum number of substrings in such a partition.

Note that each character should belong to exactly one substring in a partition.

 

Example 1:

Input: s = "abacaba"
Output: 4
Explanation:
Two possible partitions are ("a","ba","cab","a") and ("ab","a","ca","ba").
It can be shown that 4 is the minimum number of substrings needed.
Example 2:

Input: s = "ssssss"
Output: 6
Explanation:
The only valid partition is ("s","s","s","s","s","s").
 

Constraints:

1 <= s.length <= 10^5
s consists of only English lowercase letters.

Accepted
41,435
Submissions
54,030

''')

