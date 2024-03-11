from lc import *

# https://leetcode.com/problems/custom-sort-string

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        c = Counter(s)
        r = []
        for k in order:
            if k in c:
                r.append(c[k]*k)
                c.pop(k)
        for k in c:
            r.append(c[k]*k)
        return ''.join(r)

class Solution:
    def customSortString(self, o: str, s: str) -> str:
        return''.join(sorted(s,key=o.find))

test('''

791. Custom Sort String
Medium

2292

303

Add to List

Share
You are given two strings order and s. All the characters of order are unique and were sorted in some custom order previously.

Permute the characters of s so that they match the order that order was sorted. More specifically, if a character x occurs before a character y in order, then x should occur before y in the permuted string.

Return any permutation of s that satisfies this property.

 

Example 1:

Input: order = "cba", s = "abcd"
Output: "cbad"
Explanation: 
"a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b", and "a". 
Since "d" does not appear in order, it can be at any position in the returned string. "dcba", "cdba", "cbda" are also valid outputs.
Example 2:

Input: order = "cbafg", s = "abcd"
Output: "cbad"
 

Constraints:

1 <= order.length <= 26
1 <= s.length <= 200
order and s consist of lowercase English letters.
All the characters of order are unique.
'''

, check=lambda res,exp,order,_:(o:=[order.index(c) for c in res if c in order]) == sorted(o)

)
