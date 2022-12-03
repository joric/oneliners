from lc import *

class Solution:
    def frequencySort(self, s: str) -> str:
        return ''.join(v*k for k,v in Counter(s).most_common())


def check(res,exp,s):
    # check presence
    if Counter(res)!=Counter(s):
        return False

    # check grouping
    g = set()
    for c,_ in groupby(res):
        if c in g:
            return False
        g.add(c)

    # check ordering
    c,f = Counter(s), inf
    for x in res:
        if c[x]<=f:
            f = c[x]
        else:
            return False

    return True


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

Constraints:

1 <= s.length <= 5 * 10^5
s consists of uppercase and lowercase English letters and digits.

''', check = check
)
