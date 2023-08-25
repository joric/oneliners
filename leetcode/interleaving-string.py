from lc import *

class Solution:
    @cache
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if not (s1 and s2):
            return (s1 or s2 or "") == s3    
        return any(s3[:1] == x[:1] and self.isInterleave(x[1:], y, s3[1:]) for x, y in ((s1, s2), (s2, s1)))

class Solution:
    def isInterleave(self, a: str, b: str, c: str) -> bool:
        return(f:=cache(lambda a,b,c:any(c[:1]==x[:1]and f(x[1:],y,c[1:])for x,y in((a,b),(b,a)))if(a and b)else(a or b or'')==c))(a,b,c)

test('''
97. Interleaving String
Medium

6775

409

Add to List

Share
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where s and t are divided into n and m substrings respectively, such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.

 

Example 1:


Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Explanation: One way to obtain s3 is:
Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".
Interleaving the two splits, we get "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac".
Since s3 can be obtained by interleaving s1 and s2, we return true.
Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
Explanation: Notice how it is impossible to interleave s2 with any other string to obtain s3.
Example 3:

Input: s1 = "", s2 = "", s3 = ""
Output: true
 

Constraints:

0 <= s1.length, s2.length <= 100
0 <= s3.length <= 200
s1, s2, and s3 consist of lowercase English letters.
 

Follow up: Could you solve it using only O(s2.length) additional memory space?
''')
