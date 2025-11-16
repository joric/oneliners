from lc import *

# Q2 https://leetcode.com/contest/weekly-contest-197/ (Sun, Jul 12, 2020)
# https://leetcode.com/problems/number-of-substrings-with-only-1s/

class Solution:
    def numSub(self, s: str) -> int:

        if len(s)==0:
            return 0

        result  = 0

        groups = [1]
        for i in range(1, len(s)):
            if s[i-1] != s[i]:
                groups.append(1)
            else:
                groups[-1] += 1

        print(groups)

        alternate = s[0]=='1'

        # scan all groups that are 1
        for count in groups:
            if alternate:
                result += count * (count + 1) // 2

            alternate = not alternate

        return result % (10**9 + 7)

# https://leetcode.com/problems/number-of-substrings-with-only-1s/solutions/7350983/one-line-solution-by-mikposp-wokh/?envType=daily-question&envId=2025-11-16

class Solution:
    def numSub(self, s: str) -> int:
        return sum(comb(len(t)+1,2)for t in s.split('0'))%(10**9+7)

test('''
1513. Number of Substrings With Only 1s
Solved
Medium
Topics
premium lock icon
Companies
Hint
Given a binary string s, return the number of substrings with all characters 1's. Since the answer may be too large, return it modulo 109 + 7.

 

Example 1:

Input: s = "0110111"
Output: 9
Explanation: There are 9 substring in total with only 1's characters.
"1" -> 5 times.
"11" -> 3 times.
"111" -> 1 time.
Example 2:

Input: s = "101"
Output: 2
Explanation: Substring "1" is shown 2 times in s.
Example 3:

Input: s = "111111"
Output: 21
Explanation: Each substring contains only 1's characters.
 

Constraints:

1 <= s.length <= 105
s[i] is either '0' or '1'.
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
71,646/139.3K
Acceptance Rate
51.4%
Topics
Math
String
Weekly Contest 197
icon
Companies
Hint 1
Count number of 1s in each consecutive-1 group. For a group with n consecutive 1s, the total contribution of it to the final answer is (n + 1) * n // 2.
Similar Questions
Count Number of Homogenous Substrings
Medium
Count Vowel Substrings of a String
Easy
''')
