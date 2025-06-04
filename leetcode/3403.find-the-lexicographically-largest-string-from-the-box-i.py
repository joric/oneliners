from lc import *

# https://leetcode.com/problems/find-the-lexicographically-largest-string-from-the-box-i/solutions/6199547/java-c-python-the-longer-the-bigger/?envType=daily-question&envId=2025-06-04

class Solution:
    def answerString(self, w: str, n: int) -> str:
        return(w,max(w[i:i+len(w)-n+1]for i in range(len(w))))[n>1]

class Solution:
    def answerString(self, w: str, n: int) -> str:
        return[w,max(w[i:i-~len(w)-n]for i in range(len(w)))][n>1]

test('''
3403. Find the Lexicographically Largest String From the Box I
Solved
Medium
Topics
premium lock icon
Companies
Hint
You are given a string word, and an integer numFriends.

Alice is organizing a game for her numFriends friends. There are multiple rounds in the game, where in each round:

word is split into numFriends non-empty strings, such that no previous round has had the exact same split.
All the split words are put into a box.
Find the lexicographically largest string from the box after all the rounds are finished.

 

Example 1:

Input: word = "dbca", numFriends = 2

Output: "dbc"

Explanation: 

All possible splits are:

"d" and "bca".
"db" and "ca".
"dbc" and "a".
Example 2:

Input: word = "gggg", numFriends = 4

Output: "g"

Explanation: 

The only possible split is: "g", "g", "g", and "g".

Other examples:

Input: word = "bif", numFriends = 2
Output: "if"

Constraints:

1 <= word.length <= 5 * 103
word consists only of lowercase English letters.
1 <= numFriends <= word.length
Seen this question in a real interview before?
1/5
Yes
No
Accepted
17,408/72.8K
Acceptance Rate
23.9%
Topics
Two Pointers
String
Enumeration
icon
Companies
Hint 1
Find lexicographically largest substring of size n - numFriends + 1 or less starting at every index.
Similar Questions
Last Substring in Lexicographical Order
Hard
Construct the Lexicographically Largest Valid Sequence
Medium
''')
