from lc import *

# https://leetcode.com/problems/move-pieces-to-obtain-a-string/discuss/5983924/Python-one-line-solution

class Solution:
    def canChange(self, s: str, t: str) -> bool:
        return s.replace('_', '')==t.replace('_','')and min(accumulate((a=='R')-(b=='R') for a,b in zip(s,t)))>=0 and min(accumulate((a=='L')-(b=='L') for a,b in zip(s[::-1],t[::-1])))>=0

# https://leetcode.com/problems/move-pieces-to-obtain-a-string/discuss/2306178/Python-3-two-lines-one-pass-constant-memory

class Solution:
    def canChange(self, s: str, t: str) -> bool:
        return all(c==d and(le,ge)[c=='L'](i,j)for (i,c),(j,d)in zip_longest(*(((i,c)for i,c in enumerate(x)if c!='_')for x in(s,t)),fillvalue=(0,0)))

test('''
2337. Move Pieces to Obtain a String
Medium

671

45

Add to List

Share
You are given two strings start and target, both of length n. Each string consists only of the characters 'L', 'R', and '_' where:

The characters 'L' and 'R' represent pieces, where a piece 'L' can move to the left only if there is a blank space directly to its left, and a piece 'R' can move to the right only if there is a blank space directly to its right.
The character '_' represents a blank space that can be occupied by any of the 'L' or 'R' pieces.
Return true if it is possible to obtain the string target by moving the pieces of the string start any number of times. Otherwise, return false.

 

Example 1:

Input: start = "_L__R__R_", target = "L______RR"
Output: true
Explanation: We can obtain the string target from start by doing the following moves:
- Move the first piece one step to the left, start becomes equal to "L___R__R_".
- Move the last piece one step to the right, start becomes equal to "L___R___R".
- Move the second piece three steps to the right, start becomes equal to "L______RR".
Since it is possible to get the string target from start, we return true.
Example 2:

Input: start = "R_L_", target = "__LR"
Output: false
Explanation: The 'R' piece in the string start can move one step to the right to obtain "_RL_".
After that, no pieces can move anymore, so it is impossible to obtain the string target from start.
Example 3:

Input: start = "_R", target = "R_"
Output: false
Explanation: The piece in the string start can move only to the right, so it is impossible to obtain the string target from start.
 

Constraints:

n == start.length == target.length
1 <= n <= 105
start and target consist of the characters 'L', 'R', and '_'.
Accepted
27,455
Submissions
57,570
''')
