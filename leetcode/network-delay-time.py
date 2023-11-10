from lc import *

# https://leetcode.com/problems/network-delay-time

from queue import PriorityQueue

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        d,s,q,r = defaultdict(dict),set(),PriorityQueue(),0
        for x,y,t in times:
            d[x][y] = t
        q.put((0,k))
        while not q.empty():
            t,c = q.get()
            s.add(c)
            if len(s)==n:
                return t
            for o in d[c]:
                if o not in s:
                    q.put((t+d[c][o],o))
        return -1

# heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        d,s,q,r = defaultdict(dict),set(),[(0,k)],0
        for x,y,t in times:
            d[x][y] = t
        while q:
            t,c = heappop(q)
            s.add(c)
            if len(s)==n:
                return t
            for o in d[c]:
                if o not in s:
                    heappush(q,(t+d[c][o],o))
        return -1

class Solution:
    def networkDelayTime(self, v: List[List[int]], n: int, k: int) -> int:
        d,s,q,r = defaultdict(dict),set(),[(0,k)],0;[setitem(d[x],y,t)for x,y,t in v];return(f:=lambda t,c:s.add(c)or(t if len(s)==n else[heappush(q,(t+d[c][o],o))for o in d[c]if o not in s]!=0and q and f(*heappop(q))or -1))(*heappop(q))

test('''

743. Network Delay Time
Medium

6145

332

Add to List

Share
You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

 

Example 1:


Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
Example 2:

Input: times = [[1,2,1]], n = 2, k = 1
Output: 1
Example 3:

Input: times = [[1,2,1]], n = 2, k = 2
Output: -1
 

Constraints:

1 <= k <= n <= 100
1 <= times.length <= 6000
times[i].length == 3
1 <= ui, vi <= n
ui != vi
0 <= wi <= 100
All the pairs (ui, vi) are unique. (i.e., no multiple edges.)

Accepted
365,723
Submissions
705,714

''')


