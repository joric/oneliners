from lc import *

# https://leetcode.com/problems/reconstruct-itinerary/discuss/78768/Short-Ruby-Python-Java-C%2B%2B

class Solution:
    def findItinerary(self, t: List[List[str]]) -> List[str]:
        d,r = defaultdict(list),[]
        for a,b in sorted(t)[::-1]:
            d[a].append(b)
        def f(a):
            while d[a]:
                f(d[a].pop())
            r.append(a)
        f('JFK')
        return r[::-1]

class Solution:
    def findItinerary(self, t: List[List[str]]) -> List[str]:
        d,r=defaultdict(list),[];[d[a].append(b)for a,b in sorted(t)[::-1]];return(f:=lambda a:next(r.append(a)for _ in[0]*300if not(d[a]and[f(d[a].pop())])))('JFK')or r[::-1]

class Solution:
    def findItinerary(self, t: List[List[str]]) -> List[str]:
        d,r=defaultdict(list),[];[d[a].append(b)for a,b in sorted(t)[::-1]];f=lambda a:([f(d[a].pop())for _ in[0]*300if d[a]],r.append(a));f('JFK');return r[::-1]

test('''
332. Reconstruct Itinerary
Hard

4909

1694

Add to List

Share
You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

 

Example 1:


Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output: ["JFK","MUC","LHR","SFO","SJC"]
Example 2:


Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.
 

Constraints:

1 <= tickets.length <= 300
tickets[i].length == 2
fromi.length == 3
toi.length == 3
fromi and toi consist of uppercase English letters.
fromi != toi
''')

