from lc import *

# https://leetcode.com/problems/clear-digits/solutions/6399962/python-one-line/?envType=daily-question&envId=2025-02-10

class Solution:
    def clearDigits(self, s: str) -> str:
        return reduce(lambda a,x:[x+a[0],0]if not a[1]and ord(x)>58 else [a[0],a[1]-((ord(x)>58)<<1)+1],s[::-1],['',0])[0]

# https://leetcode.com/problems/clear-digits/solutions/5369174/four-line-intuitive-recursive-solution-python/?envType=daily-question&envId=2025-02-10

class Solution:
    def clearDigits(self, s: str) -> str:
        for i in range(len(s)):
            if i-1 >=0 and s[i].isdigit():
                return self.clearDigits(s[0:i-1]+s[i+1:])
        return s

class Solution:
    def clearDigits(self, s: str) -> str:
        return next((self.clearDigits(s[0:i-1]+s[i+1:])for i in range(len(s))if i>0 and s[i].isdigit()),s)

class Solution:
    def clearDigits(self, s: str) -> str:
        return(f:=lambda s:next((f(s[0:i-1]+s[i+1:])for i in range(len(s))if i>0 and '/'<s[i]<':'),s))(s)

class Solution:
    def clearDigits(self, s: str) -> str:
        return next((self.clearDigits(s[0:i-1]+s[i+1:])for i in range(len(s))if'/'<s[i]<':'),s)

# https://leetcode.com/problems/clear-digits/solutions/6400487/t100-python-solution-regex-version/?envType=daily-question&envId=2025-02-10

class Solution:
    def clearDigits(self, s: str) -> str:
        while search(p:='(\D)\d', s):
            s=re.sub(p,'',s)
        return s

class Solution:
    def clearDigits(self, s: str) -> str:
        [s:=re.sub(p,'',s)for _ in s if search(p:='(\D)\d', s)];return s

class Solution:
    def clearDigits(self, s: str) -> str:
        [s:=re.sub('(\D)\d','',s)for _ in s];return s

test('''
3174. Clear Digits
Easy
Topics
Companies
Hint
You are given a string s.

Your task is to remove all digits by doing this operation repeatedly:

Delete the first digit and the closest non-digit character to its left.
Return the resulting string after removing all digits.

 

Example 1:

Input: s = "abc"

Output: "abc"

Explanation:

There is no digit in the string.

Example 2:

Input: s = "cb34"

Output: ""

Explanation:

First, we apply the operation on s[2], and s becomes "c4".

Then we apply the operation on s[1], and s becomes "".

 

Constraints:

1 <= s.length <= 100
s consists only of lowercase English letters and digits.
The input is generated such that it is possible to delete all digits.
Seen this question in a real interview before?
1/5
Yes
No
Accepted
87.4K
Submissions
113.5K
Acceptance Rate
77.0%
Topics
String
Stack
Simulation
Companies
Hint 1
Process string s from left to right, if s[i] is a digit, mark the nearest unmarked non-digit index to its left.
Hint 2
Delete all digits and all marked characters.
''')
