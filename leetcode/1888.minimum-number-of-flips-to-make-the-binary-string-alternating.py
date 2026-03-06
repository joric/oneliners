from lc import *

# https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/solutions/6250214/my-simple-python-5-lines-of-code-method-04cbj/?envType=daily-question&envId=2026-03-07

class Solution:
    def minFlips(self, s: str) -> int:
        a=sum( i != str(index%2)for index,i in enumerate(s) )
        minf=min(a,len(s)-a)
        for i in range(len(s)):
            a= (len(s)-a + (s[i]!=str((len(s)-1)%2) ) - (s[i]=="0"))
            minf =min(minf,a,len(s)-a)
        return minf

class Solution: #TLE
    def minFlips(self, s: str) -> int:
        return min(sum(c!=t[j%2]for j,c in enumerate(s[i:]+s[:i]))for i in range(len(s))for t in('01','10'))

class Solution:
    def minFlips(self,s:str)->int:
        n=len(s);a=sum(s[i]!=str(i&1)for i in range(n));return min(min(a:=n-a+n%2*(int(c)*2-1),n-a)for c in s)

class Solution:
    def minFlips(self,s:str)->int:
        n=len(s);a=sum(i&1^int(s[i])for i in range(n));return min(min(a:=n-a+n%2*(int(c)*2-1),n-a)for c in s)

test('''
1888. Minimum Number of Flips to Make the Binary String Alternating
Medium
Topics
premium lock icon
Companies
Hint
You are given a binary string s. You are allowed to perform two types of operations on the string in any sequence:

Type-1: Remove the character at the start of the string s and append it to the end of the string.
Type-2: Pick any character in s and flip its value, i.e., if its value is '0' it becomes '1' and vice-versa.
Return the minimum number of type-2 operations you need to perform such that s becomes alternating.

The string is called alternating if no two adjacent characters are equal.

For example, the strings "010" and "1010" are alternating, while the string "0100" is not.
 

Example 1:

Input: s = "111000"
Output: 2
Explanation: Use the first operation two times to make s = "100011".
Then, use the second operation on the third and sixth elements to make s = "101010".
Example 2:

Input: s = "010"
Output: 0
Explanation: The string is already alternating.
Example 3:

Input: s = "1110"
Output: 1
Explanation: Use the second operation on the second element to make s = "1010".


Other examples:

Input: s = "0001100010101000111101000110101111000000101100000001001"
Output: 22

Constraints:

1 <= s.length <= 105
s[i] is either '0' or '1'.
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
36,871/89.6K
Acceptance Rate
41.1%
Topics
Staff
String
Dynamic Programming
Sliding Window
Weekly Contest 244
icon
Companies
Hint 1
Note what actually matters is how many 0s and 1s are in odd and even positions
Hint 2
For every cyclic shift we need to count how many 0s and 1s are at each parity and convert the minimum between them for each parity
Similar Questions
Minimum Operations to Make the Array Alternating
Medium
''')
