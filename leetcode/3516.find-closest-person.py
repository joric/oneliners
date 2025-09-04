from lc import *

# https://leetcode.com/problems/find-closest-person/solutions/7149326/one-line-solution/?envType=daily-question&envId=2025-09-04

class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        return (0,1,2)[(abs(x-z)<abs(y-z))-(abs(x-z)>abs(y-z))]

class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        return (abs(x-z)<abs(y-z))+2*(abs(x-z)>abs(y-z))

class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        return ((q:=abs(x-z)-abs(y-z))<0)+2*(q>0)

class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        q=abs(x-z)-abs(y-z);return(q<0)+2*(q>0)

test('''
3516. Find Closest Person
Solved
Easy
Topics
premium lock icon
Companies
Hint
You are given three integers x, y, and z, representing the positions of three people on a number line:

x is the position of Person 1.
y is the position of Person 2.
z is the position of Person 3, who does not move.
Both Person 1 and Person 2 move toward Person 3 at the same speed.

Determine which person reaches Person 3 first:

Return 1 if Person 1 arrives first.
Return 2 if Person 2 arrives first.
Return 0 if both arrive at the same time.
Return the result accordingly.

 

Example 1:

Input: x = 2, y = 7, z = 4

Output: 1

Explanation:

Person 1 is at position 2 and can reach Person 3 (at position 4) in 2 steps.
Person 2 is at position 7 and can reach Person 3 in 3 steps.
Since Person 1 reaches Person 3 first, the output is 1.

Example 2:

Input: x = 2, y = 5, z = 6

Output: 2

Explanation:

Person 1 is at position 2 and can reach Person 3 (at position 6) in 4 steps.
Person 2 is at position 5 and can reach Person 3 in 1 step.
Since Person 2 reaches Person 3 first, the output is 2.

Example 3:

Input: x = 1, y = 5, z = 3

Output: 0

Explanation:

Person 1 is at position 1 and can reach Person 3 (at position 3) in 2 steps.
Person 2 is at position 5 and can reach Person 3 in 2 steps.
Since both Person 1 and Person 2 reach Person 3 at the same time, the output is 0.

 

Constraints:

1 <= x, y, z <= 100
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
48,299/57.9K
Acceptance Rate
83.4%
Topics
Math
Weekly Contest 445
icon
Companies
Hint 1
Compare the distances from Persons 1 and 2 to Person 3 to determine the answer.
''')
