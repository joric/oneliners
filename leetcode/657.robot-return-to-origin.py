from lc import *

# https://leetcode.com/problems/robot-return-to-origin/solutions/106315/python-one-liner-by-aditya74-w6kg/comments/3401026/

class Solution:
    def judgeCircle(self, m: str) -> bool:
        return m.count('L')==m.count('R')and m.count('U')==m.count('D')

class Solution:
    def judgeCircle(self, m: str) -> bool:
        c=m.count;return c('L')==c('R')and c('U')==c('D')

class Solution:
    def judgeCircle(self, m: str) -> bool:
        l,r,u,d=map(m.count,'LRUD');return r==l and u==d

class Solution:
    def judgeCircle(self, m: str) -> bool:
        return not sum(1j**'LURD'.find(c)for c in m)

class Solution:
    def judgeCircle(self, m: str) -> bool:
        return sum(14**ord(c)%333%15-7for c in m)>0

class Solution:
    def judgeCircle(self, m: str) -> bool:
        return not sum(1j**(ord(c)%19)for c in m)

class Solution:
    def judgeCircle(self, m: str) -> bool:
        return 0==sum(1j**(ord(c)%19)for c in m)

test('''
657. Robot Return to Origin
Easy
Topics
premium lock icon
Companies
There is a robot starting at the position (0, 0), the origin, on a 2D plane. Given a sequence of its moves, judge if this robot ends up at (0, 0) after it completes its moves.

You are given a string moves that represents the move sequence of the robot where moves[i] represents its ith move. Valid moves are 'R' (right), 'L' (left), 'U' (up), and 'D' (down).

Return true if the robot returns to the origin after it finishes all of its moves, or false otherwise.

Note: The way that the robot is "facing" is irrelevant. 'R' will always make the robot move to the right once, 'L' will always make it move left, etc. Also, assume that the magnitude of the robot's movement is the same for each move.

 

Example 1:

Input: moves = "UD"
Output: true
Explanation: The robot moves up once, and then down once. All moves have the same magnitude, so it ended up at the origin where it started. Therefore, we return true.
Example 2:

Input: moves = "LL"
Output: false
Explanation: The robot moves left twice. It ends up two "moves" to the left of the origin. We return false because it is not at the origin at the end of its moves.
 

Constraints:

1 <= moves.length <= 2 * 104
moves only contains the characters 'U', 'D', 'L' and 'R'.
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
548,336/716.3K
Acceptance Rate
76.5%
Topics
Mid Level
String
Simulation
icon
Companies
Similar Questions
Number of Provinces
Medium
Execution of All Suffix Instructions Staying in a Grid
Medium
Furthest Point From Origin
Easy
''')
