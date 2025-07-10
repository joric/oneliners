from lc import *

# https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-ii/solutions/6943282/python3-three-line-simple-solution/

class Solution:
    def maxFreeTime(
        self, eventTime: int, startTime: List[int], endTime: List[int]
    ) -> int:
        gaps = [*map(sub, startTime + [eventTime], [0] + endTime)]

        three_largest = nlargest(3, enumerate(gaps), key=lambda x: x[1])

        return max(
            (
                gaps[i]
                + gaps[i + 1]
                + (e - s)
                * any(
                    large_group >= (e - s) and lgroup_idx not in (i, i + 1)
                    for lgroup_idx, large_group in three_largest
                )
                for i, (s, e) in enumerate(zip(startTime, endTime))
            ),
            default=0,
        )

class Solution:
    def maxFreeTime(self, t: int, s: list[int], e: list[int]) -> int:
        g=[*map(sub,s+[t],[0]+e)];l=nlargest(3,enumerate(g),key=itemgetter(1));return max((g[i]+g[i+1]+(e-s)*any(v>=(e-s)and j not in(i,i+1)for j,v in l)for i,(s,e)in enumerate(zip(s,e))),default=0)

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
            c = g[i-1]+g[i]
            d = e[i-1]-s[i-1]
            if l>=d or r[i]>=d:
                c+=d
            a = max(a,c)
            l = max(l,g[i-1])
        return a

class Solution:
    def maxFreeTime(self, t: int, s: list[int], e: list[int]) -> int:
        a=accumulate
        g=[*map(sub,s+[t],[0]+e)]
        l,r=[0,*a(g,max)],[0,*a(g[:0:-1],max)][::-1][1:]
        return max(g[i]+g[i+1]+(d:=e[i]-s[i])*(d<=r[i]or l[i]>=d)for i in range(len(s)))

class Solution:
    def maxFreeTime(self, t: int, s: list[int], e: list[int]) -> int:
        a,g=accumulate,[*map(sub,s+[t],[0]+e)];return max(a+b+(1^(e<c-d>f))*(c-d)for a,b,c,d,e,f in zip(g,g[1:],e,s,[0,*a(g,max)],[0,*a(g[:0:-1],max)][-2::-1]))


# https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-ii/solutions/6943115/functional-javascript-1-liner-messiest-code-ever/
# maxFreeTime = (t, s, e, m = 0, $ = (j, i) => m < e[m = Math.max(m, s[j + 1] - ~~e[j]), i] - s[i]) => s.map((x, i) => $(i - 1, i)).reduceRight((n, x, i) => Math.max(n, s[i + 1] - ~~e[i - 1] - $(i, i) * x * (e[i] - s[i])), m = 0 * s.push(t))

class Solution: # Bonus TLE
    def maxFreeTime(self, t: int, s: list[int], e: list[int]) -> int:
        g=[*map(sub,s+[t],[0]+e)];return max(g[i]+g[i+1]+(d:=e[i]-s[i])*(max(g[:i]+g[i+2:])>=d)for i in range(len(s)))

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

Input: eventTime = 37, startTime = [5,14,27,34], endTime = [13,18,31,37]
Output: 16

Input: eventTime = 34, startTime = [0,17], endTime = [14,19]
Output: 18

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
