from lc import * 

# https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/solutions/6363043/just-four-lines-using-counter/?envType=daily-question&envId=2025-06-10

class Solution:
    def maxDifference(self, s: str) -> int:
        cntr=Counter(s)
        mx=max(val for val in cntr.values() if val%2!=0 )
        mn=min(val for val in cntr.values() if val%2==0 )
        return mx-mn

class Solution:
    def maxDifference(self, s: str) -> int:
        c=Counter(s);f=lambda a,e:a(c[i]for i in c if e(c[i]%2,0));return f(max,ne)-f(min,eq)

class Solution:
    def maxDifference(self, s: str) -> int:
        v=Counter(s).values();return max(x for x in v if x%2)-min(x for x in v if x%2==0)

class Solution:
    def maxDifference(self, s: str) -> int:
        v=Counter(s).values();return max(x%2*x for x in v)-min(x for x in v if~x%2)

class Solution:
    def maxDifference(self, s: str) -> int:
        v=Counter(s).values();return max(x%2*x for x in v)-min(x+x%2*99 for x in v)

test('''
3442. Maximum Difference Between Even and Odd Frequency I
Solved
Easy
Topics
premium lock icon
Companies
Hint
You are given a string s consisting of lowercase English letters.

Your task is to find the maximum difference diff = a1 - a2 between the frequency of characters a1 and a2 in the string such that:

a1 has an odd frequency in the string.
a2 has an even frequency in the string.
Return this maximum difference.

 

Example 1:

Input: s = "aaaaabbc"

Output: 3

Explanation:

The character 'a' has an odd frequency of 5, and 'b' has an even frequency of 2.
The maximum difference is 5 - 2 = 3.
Example 2:

Input: s = "abcabcab"

Output: 1

Explanation:

The character 'a' has an odd frequency of 3, and 'c' has an even frequency of 2.
The maximum difference is 3 - 2 = 1.

Other examples:

Input: s = "tzt"
Output: -1

Constraints:

3 <= s.length <= 100
s consists only of lowercase English letters.
s contains at least one character with an odd frequency and one with an even frequency.
Seen this question in a real interview before?
1/5
Yes
No
Accepted
41,780/85.3K
Acceptance Rate
49.0%
Topics
Hash Table
String
Counting
icon
Companies
Hint 1
Use a frequency map to identify the maximum odd and minimum even frequencies. Then, calculate their difference.
''')
