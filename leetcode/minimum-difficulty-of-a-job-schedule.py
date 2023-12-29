from lc import *

class Solution:
    def minDifficulty(self, j:List[int], d: int) -> int:
        n = len(j)
        @cache
        def dp(i, r):
            if i == n:
                return -1
            m = inf
            o = 0
            if r == 1:
                for i in range(i, n):
                    o = max(o, j[i])
                return o
            for i in range(i, n):
                o = max(o, j[i])
                q = dp(i + 1, r - 1)
                if q > -1:
                    m = min(m, o + q)
            return -1 if m == inf else m
        return dp(0, d)

class Solution:
    def minDifficulty(self, j:List[int], d: int) -> int:
        @cache
        def dp(i, d):
            m, o = inf, 0

            if i == len(j):
                return -1

            if d == 1:
                for i in range(i, len(j)):
                    o = max(o, j[i])
                return o

            for i in range(i, len(j)):
                o = max(o, j[i])
                r = dp(i + 1, d - 1)
                if r > -1:
                    m = min(m, o + r)

            return -1 if m == inf else m

        return dp(0, d)

class Solution:
    def minDifficulty(self, j: List[int], d: int) -> int:
        @cache
        def f(i,p,d):
            if len(j) < d:
                return -1
            if d == 0:         return max([*j[i:],p])
            if i == len(j): return inf
            return min(f(i+1,j[i],d-1)+p,f(i+1,max(p,j[i]),d))
        return f(0,0,d)

# https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/discuss/3828046/Python-Elegant-recursion-or-3-lines-97-.-Faster-than-your-worst-nightmare

class Solution:
    def minDifficulty(self, j: List[int], d: int) -> int:
        return-1 if d>len(j)else(f:=cache(lambda i,p,d:max([*j[i:],p])if d<1else inf if i==len(j)else min(f(i+1,j[i],d-1)+p,f(i+1,max(p,j[i]),d))))(0,0,d)

test('''
You want to schedule a list of jobs in d days. Jobs are dependent (i.e To work on the ith job, you have to finish all the jobs j where 0 <= j < i).

You have to finish at least one task every day. The difficulty of a job schedule is the sum of difficulties of each day of the d days. The difficulty of a day is the maximum difficulty of a job done on that day.

You are given an integer array jobDifficulty and an integer d. The difficulty of the ith job is jobDifficulty[i].

Return the minimum difficulty of a job schedule. If you cannot find a schedule for the jobs return -1.

 

Example 1:


Input: jobDifficulty = [6,5,4,3,2,1], d = 2
Output: 7
Explanation: First day you can finish the first 5 jobs, total difficulty = 6.
Second day you can finish the last job, total difficulty = 1.
The difficulty of the schedule = 6 + 1 = 7 
Example 2:

Input: jobDifficulty = [9,9,9], d = 4
Output: -1
Explanation: If you finish a job per day you will still have a free day. you cannot find a schedule for the given jobs.
Example 3:

Input: jobDifficulty = [1,1,1], d = 3
Output: 3
Explanation: The schedule is one job per day. total difficulty will be 3.

Example 4:

Input: jobDifficulty=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], d = 10
Output: 0 

Constraints:

1 <= jobDifficulty.length <= 300
0 <= jobDifficulty[i] <= 1000
1 <= d <= 10
''')
