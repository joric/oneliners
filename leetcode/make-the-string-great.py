from lc import *

# https://leetcode.com/problems/make-the-string-great

class Solution:
    def makeGood(self, s: str) -> str:
        q = []
        for c in s: 
            if q and ord(q[-1])^ord(c)==32:
                q.pop()
            else:
                q.append(c)
        return ''.join(q)

class Solution:
    def makeGood(self, s: str) -> str:
        return ''.join(reduce(lambda q,c:(q and ord(q[-1])^ord(c)==32 and q.pop() or q.append(c),q)[1], s, []))

class Solution:
    def makeGood(self, s: str) -> str:
        return (q:=[],[q and ord(q[-1])^ord(c)==32 and q.pop() or q.append(c) for c in s],''.join(q))[2]

# updated 2024-04-05

class Solution:
    def makeGood(self, s: str) -> str:
        q=[];[q and q[-1].swapcase()==c and q.pop()or q.append(c)for c in s];return''.join(q)

# https://leetcode.com/problems/make-the-string-great/discuss/4977499/One-Line-Solution

class Solution:
    def makeGood(self, s: str) -> str:
        return reduce(lambda q,c:q[:-1]if q and q[-1]==c.swapcase()else q+c,s)

class Solution:
    def makeGood(self, s: str) -> str:
        return reduce(lambda q,c:q[:-1]if q[-1:]==c.swapcase()else q+c,s)

# https://leetcode.com/problems/make-the-string-great/discuss/4978386/Python-3-regex

class Solution:
    def makeGood(self, s: str) -> str:
        g=ascii_lowercase,ascii_uppercase
        p='|'.join(''.join(t) for k in [g,g[::-1]] for t in zip(*k))
        return reduce(lambda s,_:re.sub(p,'',s),s,s)

class Solution:
    def makeGood(self, s: str) -> str:
        while m:=re.search(r'(.)(?!\1)(?i:\1)',s):
            s = s.replace(m.group(0),'')
        return s

class Solution:
    def makeGood(self, s: str) -> str:
        return self.makeGood(s.replace(m.group(0),''))if(m:=re.search(r'(.)(?!\1)(?i:\1)',s))else s

class Solution:
    def makeGood(self, s: str) -> str:
        return reduce(lambda s,_:re.sub(r'(.)(?!\1)(?i:\1)','',s),s,s)

class Solution:
    def makeGood(self, s: str) -> str:
        [s:=re.sub(r'(.)(?!\1)(?i:\1)','',s)for _ in s];return s

class Solution:
    def makeGood(self, s: str) -> str:
        return reduce(lambda s,_:re.sub(r'(.)(?!\1)(?i:\1)','',s),s,s)

test('''
1544. Make The String Great
Easy

895

57

Add to List

Share
Given a string s of lower and upper case English letters.

A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:

0 <= i <= s.length - 2
s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.
To make the string good, you can choose two adjacent characters that make the string bad and remove them. You can keep doing this until the string becomes good.

Return the string after making it good. The answer is guaranteed to be unique under the given constraints.

Notice that an empty string is also good.

 

Example 1:

Input: s = "leEeetcode"
Output: "leetcode"
Explanation: In the first step, either you choose i = 1 or i = 2, both will result "leEeetcode" to be reduced to "leetcode".
Example 2:

Input: s = "abBAcC"
Output: ""
Explanation: We have many possible scenarios, and all lead to the same answer. For example:
"abBAcC" --> "aAcC" --> "cC" --> ""
"abBAcC" --> "abBA" --> "aA" --> ""
Example 3:

Input: s = "s"
Output: "s"
 

Other examples:

Input: s = "jeSsEJ"
Output: ""

Constraints:

1 <= s.length <= 100
s contains only lower and upper case English letters.

''')
