from lc import *

# https://leetcode.com/problems/meeting-rooms-iii/discuss/2527548/Python-Heap-Solution

class Solution:
    def mostBooked(self, n: int, m: List[List[int]]) -> int:
        q = [*range(n)]
        p = []
        heapify(q)
        d = [0] * n
        for s,e in sorted(m):
            while p and p[0][0] <= s:
                t,r = heappop(p)
                heappush(q,r)
            if q:
                r = heappop(q)
                heappush(p,[e,r])
            else:
                t,r = heappop(p)
                heappush(p,[t+e-s,r])
            d[r] += 1
        return d.index(max(d))

# https://leetcode.com/problems/meeting-rooms-iii/discuss/2543888/Python-2-solution%3A-heap-and-linear-scan

class Solution:
    def mostBooked(self, n: int, m: List[List[int]]) -> int:
        m.sort()
        r,c=[0]*n,[0]*n
        for s,e in m:
            j = -1
            for i in range(n):
                if r[i] <= s:
                    j = i
                    break
                elif j == -1 or r[i] < r[j]:
                    j = i
            c[j] += 1
            r[j] = max(r[j],s)+e-s
        return c.index(max(c))

# https://leetcode.com/problems/meeting-rooms-iii/discuss/4746695/one-line-solution

class Solution:
    def mostBooked(self, n: int, m: List[List[int]]) -> int:
        r,c,f=[0]*n,[0]*n,setitem;[(j:=-1,any(s>=r[i]and[j:=i]or(j<0 or r[i]<r[j])and(j:=i)<0 for i in range(n)),f(c,j,c[j]+1),f(r,j,max(r[j],s)+e-s))for s,e in sorted(m)];return c.index(max(c))

# https://leetcode.com/problems/meeting-rooms-iii/solutions/4747389/python3-11-lines-solution/

class Solution:
    def mostBooked(self, n: int, m: List[List[int]]) -> int:
        m.sort()
        c = [0] * n
        e = [0] * n
        for s, t in m:
            e = [max(x, s) for x in e]
            r = e.index(min(e))
            e[r] += (t - s)
            c[r] += 1
        return c.index(max(c))

class Solution:
    def mostBooked(self, n: int, m: List[List[int]]) -> int:
        c,e,s=[0]*n,[0]*n,setitem;[(i:=(e:=[max(x,a)for x in e]).index(min(e)),s(e,i,e[i]+b-a),s(c,i,c[i]+1))for a,b in sorted(m)];return c.index(max(c))

test('''
2402. Meeting Rooms III
Hard

894

51

Add to List

Share
You are given an integer n. There are n rooms numbered from 0 to n - 1.

You are given a 2D integer array meetings where meetings[i] = [starti, endi] means that a meeting will be held during the half-closed time interval [starti, endi). All the values of starti are unique.

Meetings are allocated to rooms in the following manner:

Each meeting will take place in the unused room with the lowest number.
If there are no available rooms, the meeting will be delayed until a room becomes free. The delayed meeting should have the same duration as the original meeting.
When a room becomes unused, meetings that have an earlier original start time should be given the room.
Return the number of the room that held the most meetings. If there are multiple rooms, return the room with the lowest number.

A half-closed interval [a, b) is the interval between a and b including a and not including b.

 

Example 1:

Input: n = 2, meetings = [[0,10],[1,5],[2,7],[3,4]]
Output: 0
Explanation:
- At time 0, both rooms are not being used. The first meeting starts in room 0.
- At time 1, only room 1 is not being used. The second meeting starts in room 1.
- At time 2, both rooms are being used. The third meeting is delayed.
- At time 3, both rooms are being used. The fourth meeting is delayed.
- At time 5, the meeting in room 1 finishes. The third meeting starts in room 1 for the time period [5,10).
- At time 10, the meetings in both rooms finish. The fourth meeting starts in room 0 for the time period [10,11).
Both rooms 0 and 1 held 2 meetings, so we return 0. 
Example 2:

Input: n = 3, meetings = [[1,20],[2,10],[3,5],[4,9],[6,8]]
Output: 1
Explanation:
- At time 1, all three rooms are not being used. The first meeting starts in room 0.
- At time 2, rooms 1 and 2 are not being used. The second meeting starts in room 1.
- At time 3, only room 2 is not being used. The third meeting starts in room 2.
- At time 4, all three rooms are being used. The fourth meeting is delayed.
- At time 5, the meeting in room 2 finishes. The fourth meeting starts in room 2 for the time period [5,10).
- At time 6, all three rooms are being used. The fifth meeting is delayed.
- At time 10, the meetings in rooms 1 and 2 finish. The fifth meeting starts in room 1 for the time period [10,12).
Room 0 held 1 meeting while rooms 1 and 2 each held 2 meetings, so we return 1. 
 

Constraints:

1 <= n <= 100
1 <= meetings.length <= 10^5
meetings[i].length == 2
0 <= starti < endi <= 5 * 10^5
All the values of starti are unique.
Accepted
34,576
Submissions
101,943
''')