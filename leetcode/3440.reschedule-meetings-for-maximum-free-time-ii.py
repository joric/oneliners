from lc import *

# https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-ii/solutions/6914758/reschedule-meetings-for-maximum-free-time-ii/?envType=daily-question&envId=2025-07-10

class Solution:
    def maxFreeTime(self, eventTime: int, startTime: list[int], endTime: list[int]) -> int:
        n = len(startTime)
        q = [False] * n
        t1 = 0
        t2 = 0
        for i in range(n):
            if endTime[i] - startTime[i] <= t1:
                q[i] = True
            t1 = max(t1, startTime[i] - (0 if i == 0 else endTime[i - 1]))
            if endTime[n - i - 1] - startTime[n - i - 1] <= t2:
                q[n - i - 1] = True
            t2 = max(t2,(eventTime if i == 0 else startTime[n - i])- endTime[n - i - 1])
        res = 0
        for i in range(n):
            left = 0 if i == 0 else endTime[i - 1]
            right = eventTime if i == n - 1 else startTime[i + 1]
            if q[i]:
                res = max(res, right - left)
            else:
                res = max(res, right - left - (endTime[i] - startTime[i]))
        return res

class Solution:
    def maxFreeTime(self, e: int, s: list[int], d: list[int]) -> int:
        n=len(s)
        q=[0]*n
        a=b=0
        for i in range(n):
            if d[i]-s[i]<=a:
                q[i]=1
            a=max(a,s[i]-(0 if i==0 else d[i-1]))
            j=n-i-1
            if d[j]-s[j]<=b:
                q[j]=1
            b=max(b,(e if i==0 else s[j+1])-d[j])
        r=0
        for i in range(n):
            l=0 if i==0 else d[i-1]
            h=e if i==n-1 else s[i+1]
            r=max(r,h-l) if q[i] else max(r,h-l-(d[i]-s[i]))
        return r


# https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-ii/solutions/6357765/c-java-explained-find-largest-gap-towards-left-and-right/?envType=daily-question&envId=2025-07-10

class Solution:
    def maxFreeTime(self, T: int, S: List[int], E: List[int]) -> int:
        n = len(S)
        gap = [S[0]]
        S += [T]
        largest_right = [0] * (n+1)
        for i in range(n): gap.append(S[i+1] - E[i])
        for i in range(n - 1, -1, -1): largest_right[i] = max(largest_right[i+1], gap[i+1])
        ans = largest_left = 0
        for i in range(1, n + 1):
            cur = gap[i-1] + gap[i]
            cur_gap = E[i-1] - S[i-1]
            if largest_left >= cur_gap or largest_right[i] >= cur_gap: cur += cur_gap
            ans = max(ans, cur)
            largest_left = max(largest_left, gap[i-1])
        return ans

class Solution:
    def maxFreeTime(self, t: int, s: list[int], e: list[int]) -> int:
        n=len(s)
        g=[s[0]];s+=[t];r=[0]*(n+1)
        for i in range(n):g.append(s[i+1]-e[i])
        for i in range(n-1,-1,-1):r[i]=max(r[i+1],g[i+1])
        a=l=0
        for i in range(1,n+1):
            c=g[i-1]+g[i];d=e[i-1]-s[i-1]
            if l>=d or r[i]>=d:c+=d
            a=max(a,c)
            l=max(l,g[i-1])
        return a

class Solution:
    def maxFreeTime(self, t: int, s: list[int], e: list[int]) -> int:
        n=len(s);g,s,r,a,l=[s[0]],s+[t],[0]*(n+1),0,0;[g.append(s[i+1]-e[i])for i in range(n)];[setitem(r,i,max(r[i+1],g[i+1]))for i in range(n-1,-1,-1)];[(c:=g[i-1]+g[i],d:=e[i-1]-s[i-1],c:=c+d*(l>=d or r[i]>=d),a:=max(a,c),l:=max(l,g[i-1]))for i in range(1,n+1)];return a

class Solution:
    def maxFreeTime(self, t: int, s: list[int], e: list[int]) -> int:
        n=len(s);s+=[t];g=[s[0]]+[*map(sub,s[1:],e)];r=[0,*accumulate(g[:0:-1],max)][::-1];l=a=0;[(d:=e[i-1]-s[i-1],a:=max(a,c:=g[i-1]+g[i]+d*(l>=d or r[i]>=d)),l:=max(l,g[i-1]))for i in range(1,n+1)];return a

test('''
3440. Reschedule Meetings for Maximum Free Time II
Medium
Topics
premium lock icon
Companies
Hint
You are given an integer eventTime denoting the duration of an event. You are also given two integer arrays startTime and endTime, each of length n.

These represent the start and end times of n non-overlapping meetings that occur during the event between time t = 0 and time t = eventTime, where the ith meeting occurs during the time [startTime[i], endTime[i]].

You can reschedule at most one meeting by moving its start time while maintaining the same duration, such that the meetings remain non-overlapping, to maximize the longest continuous period of free time during the event.

Return the maximum amount of free time possible after rearranging the meetings.

Note that the meetings can not be rescheduled to a time outside the event and they should remain non-overlapping.

Note: In this version, it is valid for the relative ordering of the meetings to change after rescheduling one meeting.

 

Example 1:

Input: eventTime = 5, startTime = [1,3], endTime = [2,5]

Output: 2

Explanation:



Reschedule the meeting at [1, 2] to [2, 3], leaving no meetings during the time [0, 2].

Example 2:

Input: eventTime = 10, startTime = [0,7,9], endTime = [1,8,10]

Output: 7

Explanation:



Reschedule the meeting at [0, 1] to [8, 9], leaving no meetings during the time [0, 7].

Example 3:

Input: eventTime = 10, startTime = [0,3,7,9], endTime = [1,4,8,10]

Output: 6

Explanation:



Reschedule the meeting at [3, 4] to [8, 9], leaving no meetings during the time [1, 7].

Example 4:

Input: eventTime = 5, startTime = [0,1,2,3,4], endTime = [1,2,3,4,5]

Output: 0

Explanation:

There is no time during the event not occupied by meetings.

Other examples:

Input: eventTime = 41, startTime = [17,24], endTime = [19,25]
Output: 24

 

Constraints:

1 <= eventTime <= 109
n == startTime.length == endTime.length
2 <= n <= 105
0 <= startTime[i] < endTime[i] <= eventTime
endTime[i] <= startTime[i + 1] where i lies in the range [0, n - 2].
Seen this question in a real interview before?
1/5
Yes
No
Accepted
40,128/72.9K
Acceptance Rate
55.1%
Topics
Array
Greedy
Enumeration
icon
Companies
Hint 1
If we reschedule a meeting earlier or later, we need to find a gap of length at least endTime[i] - startTime[i]. Try maintaining the gaps in some sorted data structure.
''')
