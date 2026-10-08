from lc import *

# https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/solutions/779978/simple-solution-in-on-intuitive-beats-10-5j4s/?envType=daily-question&envId=2026-10-09

class Solution:
    def minInsertions(self, s: str) -> int:
        t=s.replace('))',']');a=[*accumulate(1-2*(c>'(')for c in t)];return t.count(')')-3*min(0,*a)+2*a[-1]

class Solution:
    def minInsertions(self, s: str) -> int:
        return(x:=s.replace('))',']')).count(')')+2*(p:=[*accumulate((c=='(')*2-1 for c in x)])[-1]-3*min([0]+p)

class Solution:
    def minInsertions(self, s: str) -> int:
        t=s.replace('))',']');r=t.count(')');b=0
        for c in t:
            b+=1-2*(c>'(')
            r+=b<0;
            b*=b>0
        return r+2*b

class Solution:
    def minInsertions(self, s: str) -> int:
        t=s.replace('))',']');r=t.count(')');b=0;[(b:=b+1-2*(c>'('),r:=r+(b<0),b:=b*(b>0))for c in t];return r+2*b

class Solution:
    def minInsertions(self, s: str) -> int:
        b=0;t=s.replace('))',']');a=[b:=b+1-2*(c>'(')for c in t];return t.count(')')-3*min(0,*a)+2*b

class Solution:
    def minInsertions(self, s: str) -> int:
        t=s.replace('))',']');a=[b:=0]+[b:=b+1-2*(c>'(')for c in t];return t.count(')')+2*b-3*min(a)

class Solution:
    def minInsertions(self, s: str) -> int:
        b=0;t=s.replace('))',']');return t.count(')')-3*min(0,*[b:=b+1-2*(c>'(')for c in t])+2*b

class Solution:
    def minInsertions(self, s: str) -> int:
        return(s:=s.replace('))',']')).count(')')-3*min([b:=0]+[b:=b+1-2*(c>'(')for c in s])+2*b

test('''
1541. Minimum Insertions to Balance a Parentheses String
Medium
Topics
premium lock icon
Companies
Hint
Given a parentheses string s containing only the characters '(' and ')'. A parentheses string is balanced if:

Any left parenthesis '(' must have a corresponding two consecutive right parenthesis '))'.
Left parenthesis '(' must go before the corresponding two consecutive right parenthesis '))'.
In other words, we treat '(' as an opening parenthesis and '))' as a closing parenthesis.

For example, "())", "())(())))" and "(())())))" are balanced, ")()", "()))" and "(()))" are not balanced.
You can insert the characters '(' and ')' at any position of the string to balance it if needed.

Return the minimum number of insertions needed to make s balanced.

 

Example 1:

Input: s = "(()))"
Output: 1
Explanation: The second '(' has two matching '))', but the first '(' has only ')' matching. We need to add one more ')' at the end of the string to be "(())))" which is balanced.
Example 2:

Input: s = "())"
Output: 0
Explanation: The string is already balanced.
Example 3:

Input: s = "))())("
Output: 3
Explanation: Add '(' to match the first '))', Add '))' to match the last '('.
 

Constraints:

1 <= s.length <= 105
s consists of '(' and ')' only.
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
87,425/162.5K
Acceptance Rate
53.8%
Topics
Staff
String
Stack
Greedy
Bracket Sequences
Biweekly Contest 32
icon
Companies
Hint 1
Use a stack to keep opening brackets. If you face single closing ')' add 1 to the answer and consider it as '))'.
Hint 2
If you have '))' with empty stack, add 1 to the answer, If after finishing you have x opening remaining in the stack, add 2x to the answer.
Similar Questions
Minimum Number of Swaps to Make the String Balanced
Medium
''')
