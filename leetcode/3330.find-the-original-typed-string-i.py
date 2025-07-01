from lc import *

# https://leetcode.com/problems/find-the-original-typed-string-i/solutions/5972332/simple-1-line/?envType=daily-question&envId=2025-07-01

class Solution:
    def possibleStringCount(self, w: str) -> int:
        return-~sum(a==b for a,b in zip(w,w[1:]))

# https://leetcode.com/problems/find-the-original-typed-string-i/solutions/6892109/one-line-solution/?envType=daily-question&envId=2025-07-01

class Solution:
    def possibleStringCount(self, s: str) -> int:
        return-~len(s)-len(findall(r'(.)\1*',s))

class Solution:
    def possibleStringCount(self, w: str) -> int:
        return len(w)-sum(map(ne,w,w[1:]))

class Solution:
    def possibleStringCount(self, w: str) -> int:
        return-~len(w)-len([*groupby(w)])

test('''
3330. Find the Original Typed String I
Solved
Easy
Topics
premium lock icon
Companies
Hint
Alice is attempting to type a specific string on her computer. However, she tends to be clumsy and may press a key for too long, resulting in a character being typed multiple times.

Although Alice tried to focus on her typing, she is aware that she may still have done this at most once.

You are given a string word, which represents the final output displayed on Alice's screen.

Return the total number of possible original strings that Alice might have intended to type.

 

Example 1:

Input: word = "abbcccc"

Output: 5

Explanation:

The possible strings are: "abbcccc", "abbccc", "abbcc", "abbc", and "abcccc".

Example 2:

Input: word = "abcd"

Output: 1

Explanation:

The only possible string is "abcd".

Example 3:

Input: word = "aaaa"

Output: 4

 

Constraints:

1 <= word.length <= 100
word consists only of lowercase English letters.
Seen this question in a real interview before?
1/5
Yes
No
Accepted
49,642/79.6K
Acceptance Rate
62.3%
Topics
String
icon
Companies
Hint 1
Any group of consecutive characters might have been the mistake.
Similar Questions
Keyboard Row
Easy
Faulty Keyboard
Easy
''')
