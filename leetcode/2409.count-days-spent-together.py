from lc import *

# https://leetcode.com/problems/count-days-spent-together/solutions/8578432/two-simple-lines-of-code-by-mikposp-81ix/?envType=daily-question&envId=2026-10-24

class Solution:
    def countDaysTogether(self, a1: str, a2: str, b1: str, b2: str) -> int:
        f = lambda s:date(1,*map(int,s.split('-'))).toordinal()
        return max(f(min(a2,b2))-f(max(a1,b1))+1,0)

class Solution:
    def countDaysTogether(self, a1: str, a2: str, b1: str, b2: str) -> int:
        f = lambda s:time.strptime(s,'%m-%d').tm_yday
        return max(f(min(a2,b2))-f(max(a1,b1))+1,0)

class Solution:
    def countDaysTogether(self, a1: str, a2: str, b1: str, b2: str) -> int:
        f = lambda s:date.fromisoformat('1900-'+s)
        return max((f(min(a2,b2))-f(max(a1,b1))).days+1,0)

class Solution:
    def countDaysTogether(self, a1: str, a2: str, b1: str, b2: str) -> int:
        f = lambda s:(m:=int(s[:2]))*275//9-2*(m>2)+int(s[3:])-30
        return len(range(f(max(a1,b1)),f(min(a2,b2))+1))

class Solution:
    def countDaysTogether(self, *d):
        a1,a2,b1,b2 = (date.fromisoformat('1900-'+s).toordinal() for s in d)
        return len({*range(a1,a2+1)}&{*range(b1,b2+1)})

# POTD 2026-10-23

class Solution:
    def countDaysTogether(self, a: str, x: str, b: str, y: str) -> int:
        f=lambda s:time.strptime(s,'%m-%d')[7];return max(0,f(min(x,y))-f(max(a,b))+1)

class Solution:
    def countDaysTogether(self, a: str, x: str, b: str, y: str) -> int:
        t=time.strptime;return max(0,t(min(x,y),'%m-%d')[7]-t(max(a,b),'%m-%d')[7]+1)

class Solution:
    def countDaysTogether(self, a: str, x: str, b: str, y: str) -> int:
        t=time.strptime;return max(0,t(min(x,y),f:='%m-%d')[7]-t(max(a,b),f)[7]+1)

test('''
2409. Count Days Spent Together
Easy
Topics
premium lock icon
Companies
Hint
Alice and Bob are traveling to Rome for separate business meetings.

You are given 4 strings arriveAlice, leaveAlice, arriveBob, and leaveBob. Alice will be in the city from the dates arriveAlice to leaveAlice (inclusive), while Bob will be in the city from the dates arriveBob to leaveBob (inclusive). Each will be a 5-character string in the format "MM-DD", corresponding to the month and day of the date.

Return the total number of days that Alice and Bob are in Rome together.

You can assume that all dates occur in the same calendar year, which is not a leap year. Note that the number of days per month can be represented as: [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31].

 

Example 1:

Input: arriveAlice = "08-15", leaveAlice = "08-18", arriveBob = "08-16", leaveBob = "08-19"
Output: 3
Explanation: Alice will be in Rome from August 15 to August 18. Bob will be in Rome from August 16 to August 19. They are both in Rome together on August 16th, 17th, and 18th, so the answer is 3.
Example 2:

Input: arriveAlice = "10-01", leaveAlice = "10-31", arriveBob = "11-01", leaveBob = "12-31"
Output: 0
Explanation: There is no day when Alice and Bob are in Rome together, so we return 0.
 

Constraints:

All dates are provided in the format "MM-DD".
Alice and Bob's arrival dates are earlier than or equal to their leaving dates.
The given dates are valid dates of a non-leap year.
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
33,054/67.8K
Acceptance Rate
48.8%
Topics
Mid Level
Math
String
Biweekly Contest 87
icon
Companies
Hint 1
For a given day, determine if Alice or Bob or both are in Rome.
Hint 2
Brute force all 365 days for both Alice and Bob.
Similar Questions
Number of Days Between Two Dates
Easy
Minimum Number of Operations to Convert Time
Easy
''')
