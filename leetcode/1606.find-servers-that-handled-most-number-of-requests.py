from lc import *

# https://leetcode.com/problems/find-servers-that-handled-most-number-of-requests/solutions/1089184/python3-summarizing-3-approaches-by-ye15-58zq/?envType=daily-question&envId=2026-11-09

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        b=[9e99];f=[*range(k)];return __import__('statistics').multimode(heappush(b,(t+load[i])*k+j)or j for i,t in enumerate(arrival)for j in([heappush(f,i+(heappop(b)-i)%k)for _ in iter(lambda:b[0]<-~t*k,0)]or f)and[heappop(f)%k])

class Solution:
    def busiestServers(self, k: int, a: List[int], l: List[int]) -> List[int]:
        b=[9e99];f=[*range(k)];return multimode(heappush(b,(t+l[i])*k+j)or j for i,t in enumerate(a)for j in([heappush(f,i+(heappop(b)-i)%k)for _ in iter(lambda:b[0]<-~t*k,0)]or f)and[heappop(f)%k])

class Solution:
    def busiestServers(self, k: int, a: List[int], l: List[int]) -> List[int]:
        p,o=heappush,heappop;b=[9e99];f=[*range(k)];return multimode(p(b,(t+l[i])*k+j)or j for i,t in enumerate(a)for j in([p(f,i+(o(b)-i)%k)for _ in iter(lambda:b[0]<-~t*k,0)]or f)and[o(f)%k])

class Solution:
    def busiestServers(self, k: int, a: List[int], l: List[int]) -> List[int]:
        p,o=heappush,heappop;b=[9e99];r=[*range(k)];return multimode(p(b,(t+l[i])*k+j)or j for i,t in enumerate(a)if[p(r,i+(o(b)-i)%k)for _ in iter(lambda:b[0]<-~t*k,0)]+r for j in[o(r)%k])

test('''
1606. Find Servers That Handled Most Number of Requests
Hard
Topics
premium lock icon
Companies
Hint
You have k servers numbered from 0 to k-1 that are being used to handle multiple requests simultaneously. Each server has infinite computational capacity but cannot handle more than one request at a time. The requests are assigned to servers according to a specific algorithm:

The ith (0-indexed) request arrives.
If all servers are busy, the request is dropped (not handled at all).
If the (i % k)th server is available, assign the request to that server.
Otherwise, assign the request to the next available server (wrapping around the list of servers and starting from 0 if necessary). For example, if the ith server is busy, try to assign the request to the (i+1)th server, then the (i+2)th server, and so on.
You are given a strictly increasing array arrival of positive integers, where arrival[i] represents the arrival time of the ith request, and another array load, where load[i] represents the load of the ith request (the time it takes to complete). Your goal is to find the busiest server(s). A server is considered busiest if it handled the most number of requests successfully among all the servers.

Return a list containing the IDs (0-indexed) of the busiest server(s). You may return the IDs in any order.

 

Example 1:


Input: k = 3, arrival = [1,2,3,4,5], load = [5,2,3,3,3] 
Output: [1] 
Explanation: 
All of the servers start out available.
The first 3 requests are handled by the first 3 servers in order.
Request 3 comes in. Server 0 is busy, so it's assigned to the next available server, which is 1.
Request 4 comes in. It cannot be handled since all servers are busy, so it is dropped.
Servers 0 and 2 handled one request each, while server 1 handled two requests. Hence server 1 is the busiest server.
Example 2:

Input: k = 3, arrival = [1,2,3,4], load = [1,2,1,2]
Output: [0]
Explanation: 
The first 3 requests are handled by first 3 servers.
Request 3 comes in. It is handled by server 0 since the server is available.
Server 0 handled two requests, while servers 1 and 2 handled one request each. Hence server 0 is the busiest server.
Example 3:

Input: k = 3, arrival = [1,2,3], load = [10,12,11]
Output: [0,1,2]
Explanation: Each server handles a single request, so they are all considered the busiest.
 

Constraints:

1 <= k <= 105
1 <= arrival.length, load.length <= 105
arrival.length == load.length
1 <= arrival[i], load[i] <= 109
arrival is strictly increasing.
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
31,877/69.4K
Acceptance Rate
45.9%
Topics
Principal
Array
Heap (Priority Queue)
Simulation
Ordered Set
Biweekly Contest 36
icon
Companies
Hint 1
To speed up the next available server search, keep track of the available servers in a sorted structure such as an ordered set.
Hint 2
To determine if a server is available, keep track of the end times for each task in a heap and add the server to the available set once the soonest task ending time is less than or equal to the next task to add.
Similar Questions
Meeting Rooms III
Hard
''')
