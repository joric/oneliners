from lc import *

class Solution:
    def reverseWords(self, s: str) -> str:
        return' '.join(w[::-1]for w in s.split())

test('''
557. Reverse Words in a String III
Easy

5371

234

Add to List

Share
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

 

Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Example 2:

Input: s = "God Ding"
Output: "doG gniD"
 

Constraints:

1 <= s.length <= 5 * 10^4
s contains printable ASCII characters.
s does not contain any leading or trailing spaces.
There is at least one word in s.
All the words in s are separated by a single space.
Accepted
764,247
Submissions
927,038
''')

