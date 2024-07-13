from lc import *

# https://leetcode.com/problems/robot-collisions/discuss/3679132/JavaPython-3-Check-'RL'-after-sorting-by-positions-w-brief-explanation-and-analysis.

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(healths)
        sorted_indices = sorted(range(n), key=lambda i: positions[i])
        survivors = []
        for i in sorted_indices:
            while survivors and directions[survivors[-1]] == 'R' and directions[i] == 'L' and healths[i] > healths[survivors[-1]]:
                healths[i] -= 1
                survivors.pop()
            if survivors and directions[survivors[-1]] == 'R' and directions[i] == 'L':
                if healths[i] == healths[survivors[-1]]:
                    survivors.pop()
                else:
                    healths[survivors[-1]] -= 1
            else:    
                survivors.append(i) 
        return [healths[i] for i in sorted(survivors)]

# https://leetcode.com/problems/robot-collisions/discuss/3679168/JavaC%2B%2BPython-Stack-Soluton

class Solution:
    def survivedRobotsHealths(self, p: List[int], h: List[int], d: str) -> List[int]:
        q = []
        for i in sorted(range(len(p)),key=p.__getitem__):
            if d[i]=='R':
                q.append(i)
                continue
            while q and h[i] > 0:
                if h[q[-1]] < h[i]:
                    h[q.pop()] = 0
                    h[i] -= 1
                elif h[q[-1]] > h[i]:
                    h[q[-1]] -= 1
                    h[i] = 0
                else:
                    h[q.pop()] = 0
                    h[i] = 0
        return [v for v in h if v > 0]

class Solution:
    def survivedRobotsHealths(self, p: List[int], h: List[int], d: str) -> List[int]:
        q=[];[*map((f:=lambda i:q.append(i)if d[i]=='R'else(q and 0<h[i]and(a:=h[q[-1]],b:=h[i],setitem(h,q[-1]if a>b else q.pop(),~-h[q[-1]]if a>b else 0),setitem(h,i,(0,h[i]-1)[a<b]),f(i)))),sorted(range(len(p)),key=p.__getitem__))];return filter(None,h)

test('''
2751. Robot Collisions
Hard

411

18

Add to List

Share
There are n 1-indexed robots, each having a position on a line, health, and movement direction.

You are given 0-indexed integer arrays positions, healths, and a string directions (directions[i] is either 'L' for left or 'R' for right). All integers in positions are unique.

All robots start moving on the line simultaneously at the same speed in their given directions. If two robots ever share the same position while moving, they will collide.

If two robots collide, the robot with lower health is removed from the line, and the health of the other robot decreases by one. The surviving robot continues in the same direction it was going. If both robots have the same health, they are both removed from the line.

Your task is to determine the health of the robots that survive the collisions, in the same order that the robots were given, i.e. final heath of robot 1 (if survived), final health of robot 2 (if survived), and so on. If there are no survivors, return an empty array.

Return an array containing the health of the remaining robots (in the order they were given in the input), after no further collisions can occur.

Note: The positions may be unsorted.

 
 

Example 1:



Input: positions = [5,4,3,2,1], healths = [2,17,9,15,10], directions = "RRRRR"
Output: [2,17,9,15,10]
Explanation: No collision occurs in this example, since all robots are moving in the same direction. So, the health of the robots in order from the first robot is returned, [2, 17, 9, 15, 10].
Example 2:



Input: positions = [3,5,2,6], healths = [10,10,15,12], directions = "RLRL"
Output: [14]
Explanation: There are 2 collisions in this example. Firstly, robot 1 and robot 2 will collide, and since both have the same health, they will be removed from the line. Next, robot 3 and robot 4 will collide and since robot 4's health is smaller, it gets removed, and robot 3's health becomes 15 - 1 = 14. Only robot 3 remains, so we return [14].
Example 3:



Input: positions = [1,2,5,6], healths = [10,10,11,11], directions = "RLRL"
Output: []
Explanation: Robot 1 and robot 2 will collide and since both have the same health, they are both removed. Robot 3 and 4 will collide and since both have the same health, they are both removed. So, we return an empty array, [].
 

Constraints:

1 <= positions.length == healths.length == directions.length == n <= 105
1 <= positions[i], healths[i] <= 109
directions[i] == 'L' or directions[i] == 'R'
All values in positions are distinct
Accepted
9,990
Submissions
24,362
''')
