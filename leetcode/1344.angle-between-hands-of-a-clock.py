from lc import *

# https://leetcode.com/problems/angle-between-hands-of-a-clock/?envType=daily-question&envId=2026-06-18

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        return min(abs(hour*30 - minutes*5.5), 360 - abs(hour*30 - minutes*5.5))

class Solution:
    def angleClock(self, h: int, m: int) -> float:
        return min(abs(h*30-m*5.5),360-abs(h*30-m*5.5))

class Solution:
    def angleClock(self, h: int, m: int) -> float:
        return min(a:=abs(h*30-m*5.5),360-a)

test('''
1344. Angle Between Hands of a Clock
Solved
Medium
Topics
premium lock icon
Companies
Hint
Given two numbers, hour and minutes, return the smaller angle (in degrees) formed between the hour and the minute hand.

Answers within 10-5 of the actual value will be accepted as correct.

 

Example 1:


Input: hour = 12, minutes = 30
Output: 165
Example 2:


Input: hour = 3, minutes = 30
Output: 75
Example 3:


Input: hour = 3, minutes = 15
Output: 7.5
 

Constraints:

1 <= hour <= 12
0 <= minutes <= 59
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
144,811/224.6K
Acceptance Rate
64.5%
Topics
Staff
Math
Biweekly Contest 19
icon
Companies
Hint 1
The tricky part is determining how the minute hand affects the position of the hour hand.
Hint 2
Calculate the angles separately then find the difference.
''')
