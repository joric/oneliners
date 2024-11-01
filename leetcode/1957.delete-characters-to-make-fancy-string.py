from lc import *

# https://leetcode.com/problems/delete-characters-to-make-fancy-string/
# s.replace(/(.)\1\1+/g, '$1$1'); // js

class Solution:
    def makeFancyString(self, s: str) -> str:
        return re.sub(r'(.)\1\1+','\\1'*2,s)

class Solution:
    def makeFancyString(self, s: str) -> str:
        return re.sub(r'(.)\1+','\\1'*2,s)

# https://leetcode.com/problems/delete-characters-to-make-fancy-string/discuss/5992534/One-Line-Solution

class Solution:
    def makeFancyString(self, s: str) -> str:
        return s[:2]+''.join(c for p,q,c in zip(s,s[1:],s[2:]) if p+q!=q+c)

class Solution:
    def makeFancyString(self, s: str) -> str:
        return ''.join(c*min(len([*p]),2) for c,p in groupby(s))

class Solution:
    def makeFancyString(self, s: str) -> str:
        return re.sub(r'(.)\1+',r'\1\1',s)

test('''
1957. Delete Characters to Make Fancy String
Easy

470

25

Add to List

Share
A fancy string is a string where no three consecutive characters are equal.

Given a string s, delete the minimum possible number of characters from s to make it fancy.

Return the final string after the deletion. It can be shown that the answer will always be unique.

 

Example 1:

Input: s = "leeetcode"
Output: "leetcode"
Explanation:
Remove an 'e' from the first group of 'e's to create "leetcode".
No three consecutive characters are equal, so return "leetcode".
Example 2:

Input: s = "aaabaaaa"
Output: "aabaa"
Explanation:
Remove an 'a' from the first group of 'a's to create "aabaaaa".
Remove two 'a's from the second group of 'a's to create "aabaa".
No three consecutive characters are equal, so return "aabaa".
Example 3:

Input: s = "aab"
Output: "aab"
Explanation: No three consecutive characters are equal, so return "aab".
 

Constraints:

1 <= s.length <= 105
s consists only of lowercase English letters.
Accepted
48,504
Submissions
78,618
''')
