from lc import *

# https://leetcode.com/problems/asteroid-collision/discuss/201659/7-lines-concise-python-beats-97

class Solution:
    def asteroidCollision(self, a: List[int]) -> List[int]:
        s = []
        for i in a:
            while s and i<0 and s[-1]>0:
                if s[-1]>-i:
                    break 
                else:
                    if s.pop()==-i:
                        break
            else:
                s.append(i)
        return s

class Solution:
    def asteroidCollision(self, a: List[int]) -> List[int]:
        s = []
        for i in a:
            for _ in count():
                if s[-1]>-i or s.pop()==-i if s and i<0 and s[-1]>0 else not s.append(i):
                    break
        return s

class Solution:
    def asteroidCollision(self, a: List[int]) -> List[int]:
        s = []
        for i in a:
            any(s[-1]>-i or s.pop()==-i if s and i<0 and s[-1]>0 else not s.append(i) for _ in count())
        return s

class Solution:
    def asteroidCollision(self, a: List[int]) -> List[int]:
        s=[];[any(-i<s[-1]or-i==s.pop()if s and i<0<s[-1]else[s.append(i)]for _ in a)for i in a];return s

class Solution:
    def asteroidCollision(self, a):
        s=[];[any(-i<s[-1]or-i==s.pop()if s and i<0<s[-1]else(s:=s+[i])for _ in a)for i in a];return s

test('''
735. Asteroid Collision
Medium

5808

579

Add to List

Share
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

 

Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

Example 2:

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.

Example 3:

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.

Example 4:
Input: asteroids = [-2,-2,1,-2]
Output: [-2,-2,-2]

Constraints:

2 <= asteroids.length <= 10^4
-1000 <= asteroids[i] <= 1000
asteroids[i] != 0
''')
