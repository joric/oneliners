from lc import *

# Q1. https://leetcode.com/contest/weekly-contest-393/
# https://leetcode.com/problems/latest-time-you-can-obtain-after-replacing-characters/

class Solution:
    def findLatestTime(self, s: str) -> str:
        t = list(s)
        if t[0]=='?': 
            if t[1]=='?' or int(t[1])<=1: t[0]='1'
            else: t[0]='0'
        if t[1]=='?':
            if t[0]=='1': t[1]='1'
            else: t[1]='9'
        if t[3]=='?': t[3]='5'
        if t[4]=='?': t[4]='9'
        return ''.join(t)

class Solution:
    def findLatestTime(self, s: str) -> str:
        r=''
        for h in range(12):
            for m in range(60):
                t = f'{h:02d}:{m:02d}'
                if all(x=='?'or x==y for x,y in zip(s,t)):
                    r = t
        return r

class Solution:
    def findLatestTime(self, s: str) -> str:
        for i in range(12*60-1,-1,-1):
            t = '%02d:%02d'%divmod(i,60)
            if all(x=='?'or x==y for x,y in zip(s,t)):
                return t

class Solution:
    def findLatestTime(self, s: str) -> str:
        return next(t for i in range(12*60-1,-1,-1)if(t:='%02d:%02d'%divmod(i,60))and all(x=='?'or x==y for x,y in zip(s,t))and t)

class Solution:
    def findLatestTime(self, s: str) -> str:
        return reduce(lambda r,i:(r,t:='%02d:%02d'%divmod(i,60))[all(x=='?'or x==y for x,y in zip(s,t))],range(720),'')

test('''
3114. Latest Time You Can Obtain After Replacing Characters
Easy

2

2

Add to List

Share
You are given a string s representing a 12-hour format time where some of the digits (possibly none) are replaced with a "?".

12-hour times are formatted as "HH:MM", where HH is between 00 and 11, and MM is between 00 and 59. The earliest 12-hour time is 00:00, and the latest is 11:59.

You have to replace all the "?" characters in s with digits such that the time we obtain by the resulting string is a valid 12-hour format time and is the latest possible.

Return the resulting string.

 

Example 1:

Input: s = "1?:?4"

Output: "11:54"

Explanation: The latest 12-hour format time we can achieve by replacing "?" characters is "11:54".

Example 2:

Input: s = "0?:5?"

Output: "09:59"

Explanation: The latest 12-hour format time we can achieve by replacing "?" characters is "09:59".


Other examples:

Input: s = "?3:12"
Output: "03:12"

Input: s = "00:00"
Output: "00:00"

Constraints:

s.length == 5
s[2] is equal to the character ":".
All characters except s[2] are digits or "?" characters.
The input is generated such that there is at least one time between "00:00" and "11:59" that you can obtain after replacing the "?" characters.
Accepted
16,696
Submissions
53,362
''')