from lc import *

# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/submissions/305764165/?envType=daily-question&envId=2025-03-11

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        a,b,c,n,res=0,0,0,len(s),0
        for i in range(n):
            if s[i]=='a':
                res+=min(b,c)
                a=i+1
            elif s[i]=='b':
                res+=min(c,a)
                b=i+1
            elif s[i]=='c':
                res+=min(a,b)
                c=i+1
        return res

# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/solutions/772829/python-1-liner/?envType=daily-question&envId=2025-03-11

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        return reduce(lambda y,x:[y[0]+1+min(y[1].values()), dict(y[1],**{x[1]:x[0]})],enumerate(s+'a'),[0,defaultdict(lambda:-1)])[0]

# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/solutions/517059/succinct-5-line-python-solution-152ms/?envType=daily-question&envId=2025-03-11

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n, d = 0, {'a': -1, 'b': -1, 'c': -1}
        for i, c in enumerate(s):
            d[c] = i
            n += i - min(d.values())
        return (1 + len(s)) * len(s) // 2 - n

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        d=[-1]*3;return comb(len(s)+1,2)-sum(setitem(d,'abc'.find(c),i)or i-min(d)for i,c in enumerate(s))

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        d=[-1]*3;return sum(setitem(d,'abc'.find(c),i)or 1+min(d)for i,c in enumerate(s))

test('''
1358. Number of Substrings Containing All Three Characters
Solved
Medium
Topics
Companies
Hint
Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.

 

Example 1:

Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 
Example 2:

Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 
Example 3:

Input: s = "abc"
Output: 1
 

Constraints:

3 <= s.length <= 5 x 10^4
s only consists of a, b or c characters.
Seen this question in a real interview before?
1/5
Yes
No
Accepted
175.4K
Submissions
255K
Acceptance Rate
68.8%
Topics
Hash Table
String
Sliding Window
Companies
Hint 1
For each position we simply need to find the first occurrence of a/b/c on or after this position.
Hint 2
So we can pre-compute three link-list of indices of each a, b, and c.
Similar Questions
Vowels of All Substrings
Medium
Count Complete Substrings
Hard
''')
