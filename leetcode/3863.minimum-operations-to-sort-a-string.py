from lc import *

# https://leetcode.com/problems/minimum-operations-to-sort-a-string/solutions/7640913/4-line-solution-in-c-by-prashant_tak-7eid/?envType=daily-question&envId=2026-10-21

class Solution:
    def minOperations(self, s:str)->int:
        t=sorted(s);a,b=t[0],t[-1];c=s.count;f,l=s[0],s[-1];return 0if[*s]==t else(len(s)==2and-1or(f==a or l==b)and 1or(c(f)==1and f==b and c(l)==1and a==l)and 3or 2)

class Solution:
    def minOperations(self, s:str)->int:
        t=sorted(s);a,*_,b=t*2;return([*s]!=t)*(s[2:]and 3-(a in s[:-1]or b in s[1:])-(a==s[0]or b==s[-1])or-1)

class Solution:
    def minOperations(self, s:str)->int:
        t=sorted(s);a,*_,b=t*2;return([*s]>t)*(1+(s[0]>a<b>s[-1])|(not{a,b}&{*s[1:-1]})|-(len(s)<3))

test('''
3863. Minimum Operations to Sort a String
Solved
Medium
Topics
premium lock icon
Companies
Hint
You are given a string s consisting of lowercase English letters.

In one operation, you can select any substring of s that is not the entire string and sort it in non-descending alphabetical order.

Return the minimum number of operations required to make s sorted in non-descending order. If it is not possible, return -1.

 

Example 1:

Input: s = "dog"

Output: 1

Explanation:​​​​​​​

Sort substring "og" to "go".
Now, s = "dgo", which is sorted in ascending order. Thus, the answer is 1.
Example 2:

Input: s = "card"

Output: 2

Explanation:

Sort substring "car" to "acr", so s = "acrd".
Sort substring "rd" to "dr", making s = "acdr", which is sorted in ascending order. Thus, the answer is 2.
Example 3:

Input: s = "gf"

Output: -1

Explanation:

It is impossible to sort s under the given constraints. Thus, the answer is -1.
 

Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
18,745/96.6K
Acceptance Rate
19.4%
Topics
Staff
String
Weekly Contest 492
icon
Companies
Hint 1
If s is already sorted, answer is 0.
Hint 2
Let mn be the minimum char and mx be the maximum char; if mn appears at the beginning (not whole string) or mx appears at the end (not whole string), answer is 1.
Hint 3
If s cannot be transformed into a sorted string, return -1.
Hint 4
If no mn exists in any proper prefix and no mx exists in any proper suffix, answer is 3; otherwise answer is 2
''')
