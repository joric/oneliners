from lc import *

# https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/discuss/4824285/Straightforward-Python-solution

class Solution:
    def minimumLength(self, s: str) -> int:
        q=deque((k,len([*v]))for k,v in groupby(s))
        while 2<len(q)and q[0][0]==q[-1][0]:
            q.popleft()
            q.pop()
        return+(1<len(q)and sum(x[1]for x in q)or q[0][1]==1)

class Solution:
    def minimumLength(self, s: str) -> int:
        q=[(k,len([*v]))for k,v in groupby(s)];all(2<len(q)and q[0][0]==q[-1][0]and[q.pop(0),q.pop()]for _ in q*2);return+(1<len(q)and sum(x[1]for x in q)or q[0][1]==1)

# https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/discuss/4824224/Beat-100.00-or-Full-explanation-with-pictures

class Solution:
    def minimumLength(self, s: str) -> int:
        i,j = 0,len(s)-1
        while i<j and s[i]==s[j]:
            c = s[i]
            while i<=j and s[i]==c:
                i += 1
            while j>=i and s[j]==c:
                j -= 1
        return j-i+1

class Solution:
    def minimumLength(self, s: str) -> int:
        i,j=0,len(s)-1;all(i<j and s[i]==s[j]and(c:=s[i],all(i<=j and c==s[i]and[i:=i+1]for _ in s),all(j>=i and c==s[j]and[j:=j-1]for _ in s))for _ in s);return j-i+1

# https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/discuss/1052535/Python-Easy-and-Concise

class Solution:
    def minimumLength(self, s: str) -> int:
        while len(s)>1 and s[0]==s[-1]:
            s=s.strip(s[0])
        return len(s)

class Solution:
    def minimumLength(self, s: str) -> int:
        all(s[1:]and s[0]==s[-1]and(s:=s.strip(s[0]))for _ in s);return len(s)

test('''
1750. Minimum Length of String After Deleting Similar Ends
Medium

479

32

Add to List

Share
Given a string s consisting only of characters 'a', 'b', and 'c'. You are asked to apply the following algorithm on the string any number of times:

Pick a non-empty prefix from the string s where all the characters in the prefix are equal.
Pick a non-empty suffix from the string s where all the characters in this suffix are equal.
The prefix and the suffix should not intersect at any index.
The characters from the prefix and suffix must be the same.
Delete both the prefix and the suffix.
Return the minimum length of s after performing the above operation any number of times (possibly zero times).

 

Example 1:

Input: s = "ca"
Output: 2
Explanation: You can't remove any characters, so the string stays as is.
Example 2:

Input: s = "cabaabac"
Output: 0
Explanation: An optimal sequence of operations is:
- Take prefix = "c" and suffix = "c" and remove them, s = "abaaba".
- Take prefix = "a" and suffix = "a" and remove them, s = "baab".
- Take prefix = "b" and suffix = "b" and remove them, s = "aa".
- Take prefix = "a" and suffix = "a" and remove them, s = "".
Example 3:

Input: s = "aabccabba"
Output: 3
Explanation: An optimal sequence of operations is:
- Take prefix = "aa" and suffix = "a" and remove them, s = "bccabb".
- Take prefix = "b" and suffix = "bb" and remove them, s = "cca".
 

Constraints:

1 <= s.length <= 10^5
s only consists of characters 'a', 'b', and 'c'.
Accepted
25,053
Submissions
54,557
''')