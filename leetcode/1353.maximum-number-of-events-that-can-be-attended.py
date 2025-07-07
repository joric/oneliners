from lc import *

# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/solutions/510263/java-c-python-priority-queue/

class Solution:
    def maxEvents(self, e: List[List[int]]) -> int:
        e.sort(reverse=1)
        h = []
        r = d = 0
        while e or h:
            if not h: d = e[-1][0]
            while e and e[-1][0] <= d:
                heappush(h, e.pop()[1])
            heappop(h)
            r += 1
            d += 1
            while h and h[0] < d:
                heappop(h)
        return r

# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/solutions/744651/c-beats-97-greedy-and-union-find/

class Solution:
    def maxEvents(self, e: list[list[int]]) -> int:
        e.sort(key=itemgetter(1))
        p = [*range(e[-1][1]+2)]
        def f(x):
            if p[x] == x:
                return x
            p[x] = f(p[x])
            return p[x]
        r = 0
        for a,b in e:
            c = f(a)
            if c <= b:
                r += 1
                p[c] = f(c+1)
        return r

class Solution:
    def maxEvents(self, e: list[list[int]]) -> int:
        e.sort(key=itemgetter(1));p=[*range(e[-1][1]+2)];f=lambda x:x if x==p[x]else setitem(p,x,f(p[x]))or p[x];return len([setitem(p,c,f(c+1))for a,b in e if(c:=f(a))<=b])

# unicode find

class Solution:
    def maxEvents(self, e: list[list[int]]) -> int:
        e.sort(key=itemgetter(1))
        t=''.join(map(chr,range(e[-1][1]+2)))
        r = 0
        for a,b in e:
            c = ord(t[a])
            if b>=c:
                r += 1
                t = t.replace(t[a],t[c+1])
        return r

class Solution:
    def maxEvents(self, e: list[list[int]]) -> int:
        e.sort(key=itemgetter(1));t=''.join(map(chr,range(e[-1][1]+2)));return sum(b>=(c:=ord(t[a]))and(t:=t.replace(t[a],t[c+1]))!=0for a,b in e)

test('''
1353. Maximum Number of Events That Can Be Attended
Attempted
Medium
Topics
premium lock icon
Companies
Hint
You are given an array of events where events[i] = [startDayi, endDayi]. Every event i starts at startDayi and ends at endDayi.

You can attend an event i at any day d where startTimei <= d <= endTimei. You can only attend one event at any time d.

Return the maximum number of events you can attend.

 

Example 1:


Input: events = [[1,2],[2,3],[3,4]]
Output: 3
Explanation: You can attend all the three events.
One way to attend them all is as shown.
Attend the first event on day 1.
Attend the second event on day 2.
Attend the third event on day 3.
Example 2:

Input: events = [[1,2],[2,3],[3,4],[1,2]]
Output: 4

Other examples:

Input: events = [[1,4],[4,4],[2,2],[3,4],[1,1]]
Output: 4

Input: events = [[1,2],[1,2],[3,3],[1,5],[1,5]]
Output: 5

Constraints:

1 <= events.length <= 105
events[i].length == 2
1 <= startDayi <= endDayi <= 105
Seen this question in a real interview before?
1/5
Yes
No
Accepted
108,934/330.2K
Acceptance Rate
33.0%
Topics
Array
Greedy
Sorting
Heap (Priority Queue)
icon
Companies
Hint 1
Sort the events by the start time and in case of tie by the end time in ascending order.
Hint 2
Loop over the sorted events. Attend as much as you can and keep the last day occupied. When you try to attend new event keep in mind the first day you can attend a new event in.
Similar Questions
Maximum Number of Events That Can Be Attended II
Hard
Maximum Earnings From Taxi
Medium
Meeting Rooms III
Hard
''')
