from lc import *

# https://leetcode.com/problems/process-tasks-using-servers/solutions/1239888/python3-priority-queue-by-ye15-8y1z/?envType=daily-question&envId=2026-11-07

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        busy = []
        free = [(wt, i) for i, wt in enumerate(servers)]
        heapify(free)
        ans = []
        for t, task in enumerate(tasks): 
            while busy and busy[0][0] == t: 
                _, wt, i = heappop(busy)
                heappush(free, (wt, i))
            if free: wt, i = heappop(free)
            else: t, wt, i = heappop(busy)
            ans.append(i)
            heappush(busy, (t+task, wt, i))
        return ans 

class Solution:
    def assignTasks(self, s: List[int], t: List[int]) -> List[int]:
        f=sorted(zip(s,range(9**9)));b=[(1e99,)];return[r[1]for j,x in enumerate(t)if[y:=max(j,b[0][0]*(f==[])),*iter(lambda:b[0][0]>j and f>[]or heappush(f,heappop(b)[1:]),1),heappush(b,(x+y,*(r:=heappop(f))))]]

class Solution:
    def assignTasks(self, s: List[int], t: List[int]) -> List[int]:
        p,o=heappush,heappop;f=sorted(zip(s,range(9**9)));b=[(1e99,)];return[r[1]for j,x in enumerate(t)if[y:=max(j,b[0][0]*(f==[])),*iter(lambda:b[0][0]>j and f>[]or p(f,o(b)[1:]),1),p(b,(x+y,*(r:=o(f))))]]

class Solution:
    def assignTasks(self, s: List[int], t: List[int]) -> List[int]:
        p,o,y=heappush,heappop,0;f=sorted(zip(s,count()));b=[[inf]];return[r[1]for j,x in enumerate(t)if[y:=max(y,j,b[0][0]*(f==[])),*iter(lambda:y<b[0][0]or p(f,o(b)[1]),1),p(b,[x+y,r:=o(f)])]]

test('''
1882. Process Tasks Using Servers
Medium
Topics
premium lock icon
Companies
Hint
You are given two 0-indexed integer arrays servers and tasks of lengths n​​​​​​ and m​​​​​​ respectively. servers[i] is the weight of the i​​​​​​th​​​​ server, and tasks[j] is the time needed to process the j​​​​​​th​​​​ task in seconds.

Tasks are assigned to the servers using a task queue. Initially, all servers are free, and the queue is empty.

At second j, the jth task is inserted into the queue (starting with the 0th task being inserted at second 0). As long as there are free servers and the queue is not empty, the task in the front of the queue will be assigned to a free server with the smallest weight, and in case of a tie, it is assigned to a free server with the smallest index.

If there are no free servers and the queue is not empty, we wait until a server becomes free and immediately assign the next task. If multiple servers become free at the same time, then multiple tasks from the queue will be assigned in order of insertion following the weight and index priorities above.

A server that is assigned task j at second t will be free again at second t + tasks[j].

Build an array ans​​​​ of length m, where ans[j] is the index of the server the j​​​​​​th task will be assigned to.

Return the array ans​​​​.

 

Example 1:

Input: servers = [3,3,2], tasks = [1,2,3,2,1,2]
Output: [2,2,0,2,1,2]
Explanation: Events in chronological order go as follows:
- At second 0, task 0 is added and processed using server 2 until second 1.
- At second 1, server 2 becomes free. Task 1 is added and processed using server 2 until second 3.
- At second 2, task 2 is added and processed using server 0 until second 5.
- At second 3, server 2 becomes free. Task 3 is added and processed using server 2 until second 5.
- At second 4, task 4 is added and processed using server 1 until second 5.
- At second 5, all servers become free. Task 5 is added and processed using server 2 until second 7.
Example 2:

Input: servers = [5,1,4,3,2], tasks = [2,1,2,4,5,2,1]
Output: [1,4,1,4,1,3,2]
Explanation: Events in chronological order go as follows: 
- At second 0, task 0 is added and processed using server 1 until second 2.
- At second 1, task 1 is added and processed using server 4 until second 2.
- At second 2, servers 1 and 4 become free. Task 2 is added and processed using server 1 until second 4. 
- At second 3, task 3 is added and processed using server 4 until second 7.
- At second 4, server 1 becomes free. Task 4 is added and processed using server 1 until second 9. 
- At second 5, task 5 is added and processed using server 3 until second 7.
- At second 6, task 6 is added and processed using server 2 until second 7.
 

Constraints:

servers.length == n
tasks.length == m
1 <= n, m <= 2 * 105
1 <= servers[i], tasks[j] <= 2 * 105
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
52,077/123K
Acceptance Rate
42.4%
Topics
Staff
Array
Heap (Priority Queue)
Weekly Contest 243
icon
Companies
Hint 1
You can maintain a Heap of available Servers and a Heap of unavailable servers
Hint 2
Note that the tasks will be processed in the input order so you just need to find the x-th server that will be available according to the rules
Similar Questions
Parallel Courses III
Hard
''')
