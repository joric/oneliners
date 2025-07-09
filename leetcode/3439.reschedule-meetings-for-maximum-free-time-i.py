from lc import *

# https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-i/solutions/6358452/prefix-sum-sliding-window-6-lines-o-n/

class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        free_time = [e-s for e, s in zip(startTime+[eventTime], [0]+endTime)]
        ans = window = sum(free_time[:k+1])
        for i in range(len(free_time)-k-1):
            window += free_time[i+k+1] - free_time[i]
            ans = max(window, ans)
        return ans

# https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-i/solutions/6708954/python-3-lines-beats-99-15/

class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        gaps = [s - e for s, e in zip(startTime + [eventTime], [0] + endTime)]
        sm = sum(gaps[:k]) + gaps[-1]
        return max(sm := sm + gaps[i] - gaps[i - k - 1] for i in range(k, len(gaps)))

# https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-i/solutions/6915156/two-simple-lines-of-code/

class Solution:
    def maxFreeTime(self, t: int, k: int, s: List[int], e: List[int]) -> int:
        q = [*map(sub,s+[t],[0]+e)]
        return max(accumulate(map(sub,q[k+1:],q),initial=sum(q[:k+1])))

class Solution:
    def maxFreeTime(self, t: int, k: int, s: List[int], e: List[int]) -> int:
        q=[*map(sub,s+[t],[0]+e)];s=sum(q[:k])+q[-1];return max(s:=s+q[i]-q[i+~k]for i in range(k,len(q)))

class Solution: # TLE
    def maxFreeTime(self, t: int, k: int, s: List[int], e: List[int]) -> int:
        q=[*map(sub,s+[t],[0]+e)];return max(sum(q[i:i+k+1])for i in range(len(q)-k))

class Solution:
    def maxFreeTime(self, t: int, k: int, s: List[int], e: List[int]) -> int:
        q=[*map(sub,s+[t],[0]+e)];return max(accumulate(map(sub,q[k+1:],q),initial=sum(q[:k+1])))

class Solution:
    def maxFreeTime(self, t: int, k: int, s: List[int], e: List[int]) -> int:
        c=[0,*accumulate(map(sub,s+[t],[0]+e))];return max(map(sub,c[k+1:],c))

test('''
3439. Reschedule Meetings for Maximum Free Time I
Medium
Topics
premium lock icon
Companies
Hint
You are given an integer eventTime denoting the duration of an event, where the event occurs from time t = 0 to time t = eventTime.

You are also given two integer arrays startTime and endTime, each of length n. These represent the start and end time of n non-overlapping meetings, where the ith meeting occurs during the time [startTime[i], endTime[i]].

You can reschedule at most k meetings by moving their start time while maintaining the same duration, to maximize the longest continuous period of free time during the event.

The relative order of all the meetings should stay the same and they should remain non-overlapping.

Return the maximum amount of free time possible after rearranging the meetings.

Note that the meetings can not be rescheduled to a time outside the event.

 

Example 1:

Input: eventTime = 5, k = 1, startTime = [1,3], endTime = [2,5]

Output: 2

Explanation:



Reschedule the meeting at [1, 2] to [2, 3], leaving no meetings during the time [0, 2].

Example 2:

Input: eventTime = 10, k = 1, startTime = [0,2,9], endTime = [1,4,10]

Output: 6

Explanation:



Reschedule the meeting at [2, 4] to [1, 3], leaving no meetings during the time [3, 9].

Example 3:

Input: eventTime = 5, k = 2, startTime = [0,1,2,3,4], endTime = [1,2,3,4,5]

Output: 0

Explanation:

There is no time during the event not occupied by meetings.

 

Constraints:

1 <= eventTime <= 109
n == startTime.length == endTime.length
2 <= n <= 105
1 <= k <= n
0 <= startTime[i] < endTime[i] <= eventTime
endTime[i] <= startTime[i + 1] where i lies in the range [0, n - 2].
Seen this question in a real interview before?
1/5
Yes
No
Accepted
19,111/59.3K
Acceptance Rate
32.2%
Topics
Array
Greedy
Sliding Window
icon
Companies
Hint 1
In a sequence of K meetings and K + 1 gaps, you could move all meetings to the start of the sequence to get the max free time.
Hint 2
Use a sliding window of K + 1 size to store sum of gaps and take the maximum.
Similar Questions
Meeting Scheduler
Medium
''')
