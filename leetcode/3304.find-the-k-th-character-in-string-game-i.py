from lc import *

# https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/solutions/5846330/java-c-python-1-line-o-logk/?envType=daily-question&envId=2025-07-03

class Solution:
    def kthCharacter(self, k: int) -> str:
        return chr((k-1).bit_count()+97)

test('''
3304. Find the K-th Character in String Game I
Solved
Easy
Topics
premium lock icon
Companies
Hint
Alice and Bob are playing a game. Initially, Alice has a string word = "a".

You are given a positive integer k.

Now Bob will ask Alice to perform the following operation forever:

Generate a new string by changing each character in word to its next character in the English alphabet, and append it to the original word.
For example, performing the operation on "c" generates "cd" and performing the operation on "zb" generates "zbac".

Return the value of the kth character in word, after enough operations have been done for word to have at least k characters.

Note that the character 'z' can be changed to 'a' in the operation.

 

Example 1:

Input: k = 5

Output: "b"

Explanation:

Initially, word = "a". We need to do the operation three times:

Generated string is "b", word becomes "ab".
Generated string is "bc", word becomes "abbc".
Generated string is "bccd", word becomes "abbcbccd".
Example 2:

Input: k = 10

Output: "c"

 

Constraints:

1 <= k <= 500
Seen this question in a real interview before?
1/5
Yes
No
Accepted
74,613/98.4K
Acceptance Rate
75.8%
Topics
Math
Bit Manipulation
Recursion
Simulation
icon
Companies
Hint 1
The constraints are small. Construct the string by simulating the operations.
Similar Questions
Shifting Letters
Medium
''')
