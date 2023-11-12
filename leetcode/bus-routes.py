from lc import *

# https://leetcode.com/problems/bus-routes/discuss/122771/C%2B%2BJavaPython-BFS-Solution

class Solution:
    def numBusesToDestination(self, r: List[List[int]], s: int, t: int) -> int:
        g = defaultdict(set)
        for i,x in enumerate(r):
            for j in x:
                g[j].add(i)
        q = [(s,0)]
        v = set([s])
        for x,b in q:
            if x==t:
                return b
            for i in g[x]:
                for j in r[i]:
                    if j not in v:
                        q.append((j,b+1))
                        v.add(j)
                r[i] = []
        return -1

class Solution:
    def numBusesToDestination(self, r: List[List[int]], s: int, t: int) -> int:
        g,q,v = defaultdict(set),[(s,0)],set([s])
        any(g[j].add(i)for i,x in enumerate(r) for j in x)
        for x,b in q:
            if x==t:
                return b
            [([v.add(j)or q.append((j,b+1))for j in r[i]if j not in v],setitem(r,i,[]))for i in g[x]]
        return -1

class Solution:
    def numBusesToDestination(self, r: List[List[int]], s: int, t: int) -> int:
        g,q,v=defaultdict(set),[(s,0)],set([s]);any(g[j].add(i)for i,x in enumerate(r)for j in x);return next((b for x,b in q if x==t or not[([v.add(j)or q.append((j,b+1))for j in r[i]if j not in v],setitem(r,i,[]))for i in g[x]]),-1)

test('''
815. Bus Routes
Hard

3396

84

Add to List

Share
You are given an array routes representing bus routes where routes[i] is a bus route that the ith bus repeats forever.

For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.
You will start at the bus stop source (You are not on any bus initially), and you want to go to the bus stop target. You can travel between bus stops by buses only.

Return the least number of buses you must take to travel from source to target. Return -1 if it is not possible.

 

Example 1:

Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6
Output: 2
Explanation: The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.
Example 2:

Input: routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12
Output: -1
 

Constraints:

1 <= routes.length <= 500.
1 <= routes[i].length <= 10^5
All the values of routes[i] are unique.
sum(routes[i].length) <= 10^5
0 <= routes[i][j] < 10^6
0 <= source, target < 10^6
Accepted
143,541
Submissions
312,692
''')

