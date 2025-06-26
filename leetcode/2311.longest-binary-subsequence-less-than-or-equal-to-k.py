from lc import *

# https://leetcode.com/problems/longest-binary-subsequence-less-than-or-equal-to-k/solutions/5301872/one-line-solution/

class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        return(f:=lambda i,k:s[i:]and k and 1+f(i+1,k-(k&1<int(s[~i]))>>1)or s[:-i].count('0'))(0,k)

class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        return(i:=next((i for i in range(len(s)+1)if int(s[~i:],2)>k),len(s)))+s[:-i].count('0')

test('''
2311. Longest Binary Subsequence Less Than or Equal to K
Medium
Topics
premium lock icon
Companies
Hint
You are given a binary string s and a positive integer k.

Return the length of the longest subsequence of s that makes up a binary number less than or equal to k.

Note:

The subsequence can contain leading zeroes.
The empty string is considered to be equal to 0.
A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.
 

Example 1:

Input: s = "1001010", k = 5
Output: 5
Explanation: The longest subsequence of s that makes up a binary number less than or equal to 5 is "00010", as this number is equal to 2 in decimal.
Note that "00100" and "00101" are also possible, which are equal to 4 and 5 in decimal, respectively.
The length of this subsequence is 5, so 5 is returned.
Example 2:

Input: s = "00101001", k = 1
Output: 6
Explanation: "000001" is the longest subsequence of s that makes up a binary number less than or equal to 1, as this number is equal to 1 in decimal.
The length of this subsequence is 6, so 6 is returned.
 

Other examples:

Input: s = "0", k = 583196182
Output: 1

Constraints:

1 <= s.length <= 1000
s[i] is either '0' or '1'.
1 <= k <= 109
Seen this question in a real interview before?
1/5
Yes
No
Accepted
24,812/64.6K
Acceptance Rate
38.4%
Topics
String
Dynamic Programming
Greedy
Memoization
icon
Companies
Hint 1
Choosing a subsequence from the string is equivalent to deleting all the other digits.
Hint 2
If you were to remove a digit, which one should you remove to reduce the value of the string?
Similar Questions
Maximum Binary String After Change
Medium
''')
