from lc import *

# https://leetcode.com/problems/walking-robot-simulation-ii/solutions/7770979/simple-o1-by-mexalen-ejtp/?envType=daily-question&envId=2026-04-07

class Robot:
    def __init__(s,w:int,h:int):
        a=w+h
        s.n=2*a-4
        s.f=0
        s.p=[0,0]
        s.d=1
        s.m=[[0,0,1]]+[[i,0,0]for i in range(1,w)]+[[w-1,i-w+1,2]for i in range(w,a-1)]+[[2*w+h-3-i,h-1,3]for i in range(a-1,2*w+h-2)]+[[0,2*a-4-i,1]for i in range(2*w+h-2,s.n)]
    def step(s,num:int)->None:
        s.f=(s.f+num)%s.n
        *s.p,s.d=s.m[s.f]
    def getPos(s)->List[int]:
        return s.p
    def getDir(s)->str:
        return['East','South','North','West'][s.d]

class Robot:
    def __init__(s,w,h):
        s.n=(w+h-2)*2
        s.f=0
        r=range
        s.m=[[0,0,1]]+[[i,0,0]for i in r(1,w)]+[[w-1,i,2]for i in r(1,h)]+[[w-2-i,h-1,3]for i in r(w-1)]+[[0,h-i-2,1]for i in r(h)]
    def step(s,n):
        s.f=(s.f+n)%s.n
        s.k=s.m[s.f]
    getPos=lambda s:s.k[:2]
    getDir=lambda s:['South','East','North','West'][s.k[2]]

r,t=range,setattr;Robot=type('',(),{'__init__':lambda s,w,h:t(s,'k',[0]*3)or t(s,'n',(w+h-2)*2)or t(s,'f',0)or t(s,'m',[[0,0,1]]+[[i,0,0]for i in r(1,w)]+[[w-1,i,2]for i in r(1,h)]+[[w-2-i,h-1,3]for i in r(w-1)]+[[0,h-i-2,1]for i in r(h)]),'step':lambda s,n:t(s,'f',(s.f+n)%s.n)or t(s,'k',s.m[s.f]),'getPos':lambda s:s.k[:2],'getDir':lambda s:['East','South','North','West'][s.k[2]]})

test('''
2069. Walking Robot Simulation II
Medium
Topics
premium lock icon
Companies
Hint
A width x height grid is on an XY-plane with the bottom-left cell at (0, 0) and the top-right cell at (width - 1, height - 1). The grid is aligned with the four cardinal directions ("North", "East", "South", and "West"). A robot is initially at cell (0, 0) facing direction "East".

The robot can be instructed to move for a specific number of steps. For each step, it does the following.

Attempts to move forward one cell in the direction it is facing.
If the cell the robot is moving to is out of bounds, the robot instead turns 90 degrees counterclockwise and retries the step.
After the robot finishes moving the number of steps required, it stops and awaits the next instruction.

Implement the Robot class:

Robot(int width, int height) Initializes the width x height grid with the robot at (0, 0) facing "East".
void step(int num) Instructs the robot to move forward num steps.
int[] getPos() Returns the current cell the robot is at, as an array of length 2, [x, y].
String getDir() Returns the current direction of the robot, "North", "East", "South", or "West".
 

Example 1:

example-1
Input
["Robot", "step", "step", "getPos", "getDir", "step", "step", "step", "getPos", "getDir"]
[[6, 3], [2], [2], [], [], [2], [1], [4], [], []]
Output
[null, null, null, [4, 0], "East", null, null, null, [1, 2], "West"]

Explanation
Robot robot = new Robot(6, 3); // Initialize the grid and the robot at (0, 0) facing East.
robot.step(2);  // It moves two steps East to (2, 0), and faces East.
robot.step(2);  // It moves two steps East to (4, 0), and faces East.
robot.getPos(); // return [4, 0]
robot.getDir(); // return "East"
robot.step(2);  // It moves one step East to (5, 0), and faces East.
                // Moving the next step East would be out of bounds, so it turns and faces North.
                // Then, it moves one step North to (5, 1), and faces North.
robot.step(1);  // It moves one step North to (5, 2), and faces North (not West).
robot.step(4);  // Moving the next step North would be out of bounds, so it turns and faces West.
                // Then, it moves four steps West to (1, 2), and faces West.
robot.getPos(); // return [1, 2]
robot.getDir(); // return "West"

 

Constraints:

2 <= width, height <= 100
1 <= num <= 105
At most 104 calls in total will be made to step, getPos, and getDir.
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
17,556/67.7K
Acceptance Rate
25.9%
Topics
Senior
Design
Simulation
Biweekly Contest 65
icon
Companies
Hint 1
The robot only moves along the perimeter of the grid. Can you think if modulus can help you quickly compute which cell it stops at?
Hint 2
After the robot moves one time, whenever the robot stops at some cell, it will always face a specific direction. i.e., The direction it faces is determined by the cell it stops at.
Hint 3
Can you precompute what direction it faces when it stops at each cell along the perimeter, and reuse the results?
Similar Questions
Walking Robot Simulation
Medium
''', Robot)
