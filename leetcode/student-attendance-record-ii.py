from lc import *

# https://leetcode.com/problems/student-attendance-record-ii/discuss/3435455/Python-3-or-Simple-One-Line-Iteration-Method

class Solution:
    def checkRecord(self, n: int) -> int:
        a,b,c,d,e,f,m=1,1,0,1,0,0,10**9+7
        for k in range(n-1):
            a,b,c,d,e,f = (a+b+c)%m,a,b,(a+b+c+d+e+f)%m,d,e
        return (a+b+c+d+e+f)%m

class Solution:
    def checkRecord(self, n: int) -> int:
        m=10**9+7;return sum(reduce(lambda p,_:[sum(p[:3])%m,*p[:2],sum(p)%m,*p[3:5]],[0]*~-n,[1,1,0,1,0,0]))%m

class Solution:
    def checkRecord(self, n: int) -> int:
        p=1,1,0,1,0,0;m=10**9+7;[p:=(sum(p[:3])%m,*p[:2],sum(p)%m,*p[3:5])for _ in[0]*~-n];return sum(p)%m

class Solution:
    def checkRecord(self, n: int) -> int:
        p=1,1,0,1;m=10**9+7;[p:=(sum(p[:3])%m,*p[:2],sum(p)%m,*p[3:5])for _ in[0]*~-n];return sum(p)%m

class Solution:
    def checkRecord(self, n: int) -> int:
        p=1,1,0,1;m=10**9+7;[p:=(sum(p[:3])%m,*p[:2],sum(p)%m,*p[3:5])for _ in[0]*n];return p[3]

class Solution:
    def checkRecord(self, n: int) -> int:
        p=1,1,1;m=10**9+7;[p:=(sum(p[::2])%m,sum(p)%m,*p[:4])for _ in[0]*n];return p[1]

class Solution:
    def checkRecord(self, n: int) -> int:
        p=1,;m=10**9+7;[p:=(sum(p[::2])%m,sum(p)%m,*p[:4])for _ in-~n*p];return p[1]

test('''
552. Student Attendance Record II
Hard

1735

249

Add to List

Share
An attendance record for a student can be represented as a string where each character signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:

'A': Absent.
'L': Late.
'P': Present.
Any student is eligible for an attendance award if they meet both of the following criteria:

The student was absent ('A') for strictly fewer than 2 days total.
The student was never late ('L') for 3 or more consecutive days.
Given an integer n, return the number of possible attendance records of length n that make a student eligible for an attendance award. The answer may be very large, so return it modulo 109 + 7.

 

Example 1:

Input: n = 2
Output: 8
Explanation: There are 8 records with length 2 that are eligible for an award:
"PP", "AP", "PA", "LP", "PL", "AL", "LA", "LL"
Only "AA" is not eligible because there are 2 absences (there need to be fewer than 2).
Example 2:

Input: n = 1
Output: 3
Example 3:

Input: n = 10101
Output: 183236316
 

Constraints:

1 <= n <= 105
Accepted
66,936
Submissions
156,010
''')
