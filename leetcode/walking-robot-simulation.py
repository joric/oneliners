from lc import *

# https://leetcode.com/problems/walking-robot-simulation/discuss/4974559/Python-3-oror-12-lines-simple-iteration-oror-TS-98-58

class Solution:
    def robotSim(self, c: List[int], o: List[List[int]]) -> int:
        g = {*map(tuple,o)}
        x,y, i,j, a = 0,0, 0,1, 0
        for d in c:
            if d<0:
                i,j = (j,-i) if d+2 else (-j,i)
            else:
                for _ in range(d):
                    if (x+i, y+j) in g:
                        break
                    x,y = x+i, y+j
            a = max(a, x*x + y*y)
        return a

class Solution:
    def robotSim(self, c: List[int], o: List[List[int]]) -> int:
        g,z,w,a = {i+j*1j for i,j in o},0j,1j,0
        for d in c:
            if d<0:
                w *= (1j,-1j)[d+2]
            else:
                [(z:=z+w)for _ in range(d)if(z+w)not in g]
            a = max(a, abs(z**2))
        return int(a)

class Solution:
    def robotSim(self, c: List[int], o: List[List[int]]) -> int:
        g,z,w={i+j*1j for i,j in o},0,1j;return int(max((d<0 and(w:=w*(1j,-1j)[d+2])or[(z:=z+w)for _ in range(d)if(z+w)not in g],abs(z**2))[1]for d in c))

class Solution:
    def robotSim(self, c: List[int], o: List[List[int]]) -> int:
        g,z,w={i+j*1j for i,j in o},0,1j;return int(max(abs(z**2)for d in c if d<0 and(w:=w*(1j,-1j)[d+2])or[(z:=z+w)for _ in range(d)if(z+w)not in g]))

test('''
874. Walking Robot Simulation
Medium

207

50

Add to List

Share
A robot on an infinite XY-plane starts at point (0, 0) facing north. The robot can receive a sequence of these three possible types of commands:

-2: Turn left 90 degrees.
-1: Turn right 90 degrees.
1 <= k <= 9: Move forward k units, one unit at a time.
Some of the grid squares are obstacles. The ith obstacle is at grid point obstacles[i] = (xi, yi). If the robot runs into an obstacle, then it will instead stay in its current location and move on to the next command.

Return the maximum Euclidean distance that the robot ever gets from the origin squared (i.e. if the distance is 5, return 25).

Note:

North means +Y direction.
East means +X direction.
South means -Y direction.
West means -X direction.
There can be obstacle in [0,0].
 

Example 1:

Input: commands = [4,-1,3], obstacles = []
Output: 25
Explanation: The robot starts at (0, 0):
1. Move north 4 units to (0, 4).
2. Turn right.
3. Move east 3 units to (3, 4).
The furthest point the robot ever gets from the origin is (3, 4), which squared is 32 + 42 = 25 units away.
Example 2:

Input: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
Output: 65
Explanation: The robot starts at (0, 0):
1. Move north 4 units to (0, 4).
2. Turn right.
3. Move east 1 unit and get blocked by the obstacle at (2, 4), robot is at (1, 4).
4. Turn left.
5. Move north 4 units to (1, 8).
The furthest point the robot ever gets from the origin is (1, 8), which squared is 12 + 82 = 65 units away.
Example 3:

Input: commands = [6,-1,-1,6], obstacles = []
Output: 36
Explanation: The robot starts at (0, 0):
1. Move north 6 units to (0, 6).
2. Turn right.
3. Turn right.
4. Move south 6 units to (0, 0).
The furthest point the robot ever gets from the origin is (0, 6), which squared is 62 = 36 units away.
 

More examples:

Input: commands = [-2,-1,8,9,6], obstacles = [[-1,3],[0,1],[-1,5],[-2,-4],[5,4],[-2,-3],[5,-1],[1,-1],[5,5],[5,2]]
Output: 0

Constraints:

1 <= commands.length <= 104
commands[i] is either -2, -1, or an integer in the range [1, 9].
0 <= obstacles.length <= 104
-3 * 104 <= xi, yi <= 3 * 104
The answer is guaranteed to be less than 231.
Accepted
43,165
Submissions
105,947
''')
