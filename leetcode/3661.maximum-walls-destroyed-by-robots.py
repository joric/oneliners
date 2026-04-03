from lc import *

# https://leetcode.com/problems/maximum-walls-destroyed-by-robots/solutions/7115085/python-dp-by-awice-mfxi/?envType=daily-question&envId=2026-04-03

class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        A = sorted(zip(robots, distance))
        N = len(A)
        walls.sort()

        def count(L, R):
            if L > R:
                return 0
            return bisect_right(walls, R) - bisect_left(walls, L)

        avail = 0
        used = count(A[0][0] - A[0][1], A[0][0] - 1)
        A.append([inf, 0])
        for i in range(N):
            l, dl = A[i]
            r, dr = A[i + 1]

            l1, r1 = l + 1, min(l + dl, r - 1)
            l2, r2 = max(r - dr, l + 1), r - 1
            
            left = count(l1, r1)
            right = count(l2, r2)
            both = left + right - count(max(l1, l2), min(r1, r2))

            navail = max(avail + left, used)
            nused = max(avail + both, used + right)
            avail, used = navail, nused

        for x in set(x for x,_ in A):
            used += count(x, x)
        return used

class Solution:
    def maxWalls(self, r: List[int], d: List[int], w: List[int]) -> int:
        a = sorted(zip(r,d))
        n = len(a)
        w.sort()
        c=lambda l,r:l<=r and bisect_right(w,r)-bisect_left(w,l)or 0
        v = 0
        u = c(a[0][0]-a[0][1],a[0][0]-1)
        a.append([inf, 0])
        for i in range(n):
            x, y = a[i]
            p, q = a[i + 1]
            e = x+1
            f = min(x+y, p-1)
            g = max(p-q, x+1)
            h = p - 1
            l = c(e, f)
            r = c(g, h)
            b = l+r-c(max(e,g),min(f,h))
            v,u = max(v+l,u),max(v+b,u+r)
        return u+sum(c(z,z)for z in{z for z,_ in a})

# POTD 2026-04-04

class Solution:
    def maxWalls(self, r: List[int], d: List[int], w: List[int]) -> int:
        w.sort();a=sorted(zip(r,d))+[(inf,0)];f=lambda x,y:max(0,bisect_right(w,y)-bisect_left(w,x));v,u=0,f((h:=a[0])[0]-h[1],h[0]-1);[(c:=f(e:=x+1,g:=min(x+y,p-1)),j:=f(i:=max(p-q,e),h:=p-1),t:=v,v:=max(v+c,u),u:=max(t+c+j-f(max(e,i),min(g,h)),u+j))for(x,y),(p,q)in pairwise(a)];return u+sum(f(z,z)for z in{*r})

test('''
3661. Maximum Walls Destroyed by Robots
Hard
Topics
premium lock icon
Companies
Hint
There is an endless straight line populated with some robots and walls. You are given integer arrays robots, distance, and walls:
robots[i] is the position of the ith robot.
distance[i] is the maximum distance the ith robot's bullet can travel.
walls[j] is the position of the jth wall.
Every robot has one bullet that can either fire to the left or the right at most distance[i] meters.

A bullet destroys every wall in its path that lies within its range. Robots are fixed obstacles: if a bullet hits another robot before reaching a wall, it immediately stops at that robot and cannot continue.

Return the maximum number of unique walls that can be destroyed by the robots.

Notes:

A wall and a robot may share the same position; the wall can be destroyed by the robot at that position.
Robots are not destroyed by bullets.
 

Example 1:

Input: robots = [4], distance = [3], walls = [1,10]

Output: 1

Explanation:

robots[0] = 4 fires left with distance[0] = 3, covering [1, 4] and destroys walls[0] = 1.
Thus, the answer is 1.
Example 2:

Input: robots = [10,2], distance = [5,1], walls = [5,2,7]

Output: 3

Explanation:

robots[0] = 10 fires left with distance[0] = 5, covering [5, 10] and destroys walls[0] = 5 and walls[2] = 7.
robots[1] = 2 fires left with distance[1] = 1, covering [1, 2] and destroys walls[1] = 2.
Thus, the answer is 3.
Example 3:
Input: robots = [1,2], distance = [100,1], walls = [10]

Output: 0

Explanation:

In this example, only robots[0] can reach the wall, but its shot to the right is blocked by robots[1]; thus the answer is 0.

 

Constraints:

1 <= robots.length == distance.length <= 105
1 <= walls.length <= 105
1 <= robots[i], walls[j] <= 109
1 <= distance[i] <= 105
All values in robots are unique
All values in walls are unique
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
8,167/30.7K
Acceptance Rate
26.6%
Topics
Senior Staff
Array
Binary Search
Dynamic Programming
Sorting
Weekly Contest 464
icon
Companies
Hint 1
Sort both the robots and walls arrays. This will help in efficiently processing positions and performing range queries.
Hint 2
Each robot can shoot either left or right. However, if a robot fires and another robot is in its path, the bullet stops. You need to use the positions of neighboring robots to limit the shooting range.
Hint 3
Use binary search (lower_bound and upper_bound) to count how many walls fall within a certain range.
Hint 4
You can use dynamic programming to keep track of the maximum number of walls destroyed so far, depending on the direction the previous robot shot.
''')
