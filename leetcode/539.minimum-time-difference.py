from lc import *

# https://leetcode.com/problems/minimum-time-difference/discuss/1048387/Python-3-lines-solution-with-comments

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        conv = lambda s: int(s[:2]) * 60 + int(s[3:])
        times = sorted([conv(t) for t in timePoints])
        return min((y - x) % 1440 for x, y in zip(times, times[1:] + [times[0] + 1440]))

class Solution:
    def findMinDifference(self, p: List[str]) -> int:
        t=sorted(int(s[:2])*60+int(s[3:])for s in p);return min((y-x)%1440 for x,y in zip(t,t[1:]+[t[0]+1440]))

test('''
539. Minimum Time Difference
Medium

1878

265

Add to List

Share
Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time-points in the list.
 

Example 1:

Input: timePoints = ["23:59","00:00"]
Output: 1
Example 2:

Input: timePoints = ["00:00","23:59","00:00"]
Output: 0
 

Constraints:

2 <= timePoints.length <= 2 * 104
timePoints[i] is in the format "HH:MM".
Accepted
156,100
Submissions
273,540
''')
