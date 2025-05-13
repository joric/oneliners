from lc import *

# https://leetcode.com/problems/total-characters-in-string-after-transformations-i/solutions/6737303/five-simple-lines-of-code/?envType=daily-question&envId=2025-05-13

class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        q = deque(itemgetter(*ascii_lowercase)(Counter(s)))
        for _ in range(t):
            q.appendleft(q.pop())
            q[1] += q[0]
        return sum(q)%(10**9+7)

class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        return sum(reduce(lambda q,_:(q[-1],q[0]+q[-1])+q[1:-1],range(t),itemgetter(*ascii_lowercase)(Counter(s))))%(10**9+7)

test('''
3335. Total Characters in String After Transformations I
Solved
Medium
Topics
Companies
Hint
You are given a string s and an integer t, representing the number of transformations to perform. In one transformation, every character in s is replaced according to the following rules:

If the character is 'z', replace it with the string "ab".
Otherwise, replace it with the next character in the alphabet. For example, 'a' is replaced with 'b', 'b' is replaced with 'c', and so on.
Return the length of the resulting string after exactly t transformations.

Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:

Input: s = "abcyy", t = 2

Output: 7

Explanation:

First Transformation (t = 1):
'a' becomes 'b'
'b' becomes 'c'
'c' becomes 'd'
'y' becomes 'z'
'y' becomes 'z'
String after the first transformation: "bcdzz"
Second Transformation (t = 2):
'b' becomes 'c'
'c' becomes 'd'
'd' becomes 'e'
'z' becomes "ab"
'z' becomes "ab"
String after the second transformation: "cdeabab"
Final Length of the string: The string is "cdeabab", which has 7 characters.
Example 2:

Input: s = "azbk", t = 1

Output: 5

Explanation:

First Transformation (t = 1):
'a' becomes 'b'
'z' becomes "ab"
'b' becomes 'c'
'k' becomes 'l'
String after the first transformation: "babcl"
Final Length of the string: The string is "babcl", which has 5 characters.
 

Constraints:

1 <= s.length <= 105
s consists only of lowercase English letters.
1 <= t <= 105
Seen this question in a real interview before?
1/5
Yes
No
Accepted
16.5K
Submissions
62.2K
Acceptance Rate
26.6%
Topics
Hash Table
Math
String
Dynamic Programming
Counting
Companies
Hint 1
Maintain the frequency of each character.
''')
