from lc import *

# https://leetcode.com/problems/total-cost-to-hire-k-workers/discuss/2783147/Python3-priority-queues

class Solution:
    def totalCost(self, c: List[int], k: int, t: int) -> int:
        heapify(a:=c[:t])
        heapify(b:=c[max(t,len(c)-t):])
        r,i,j=0,t,len(c)-t-1
        for _ in range(k): 
            if not b or a and a[0]<=b[0]:
                r += heappop(a)
                if i<=j: 
                    heappush(a,c[i])
                    i+=1
            else: 
                r += heappop(b)
                if i<=j:
                    heappush(b,c[j])
                    j-=1
        return r 

class Solution:
    def totalCost(self, c: List[int], k: int, t: int) -> int:
        heapify(a:=c[:t]);heapify(b:=c[max(t,len(c)-t):]);r,i,j=0,t,len(c)-t-1;[(not b or a and a[0]<=b[0])and(r:=r+heappop(a),i<=j and(heappush(a,c[i]),i:=i+1))or(r:=r+heappop(b),i<=j and(heappush(b,c[j]),j:=j-1))for _ in range(k)];return r

class Solution:
    def totalCost(self, c: List[int], k: int, t: int) -> int:
        h,p,u=heapify,heappop,heappush;h(a:=c[:t]);h(b:=c[max(t,len(c)-t):]);r,i,j=0,t,len(c)-t-1;[(not b or a and a[0]<=b[0])and(r:=r+p(a),i<=j and(u(a,c[i]),i:=i+1))or(r:=r+p(b),i<=j and(u(b,c[j]),j:=j-1))for _ in range(k)];return r

class Solution:
    def totalCost(self, c: List[int], k: int, t: int) -> int:
        h=heapify
        h(a:=c[:t])
        h(b:=c[max(t,len(c)-t):])
        r,i,j=0,t,len(c)-t-1
        for _ in range(k):
            x=(b,a)[d:=bool(not b or a and a[0]<=b[0])]
            r += heappop(x)
            if i<=j: 
                heappush(x,c[(j,i)[d]])
                i+=d
                j-=1-d
        return r 

class Solution:
    def totalCost(self, c: List[int], k: int, t: int) -> int:
        h=heapify;h(a:=c[:t]);h(b:=c[max(t,len(c)-t):]);r,i,j=0,t,len(c)+~t;[(x:=(b,a)[d:=bool(not b or a and a[0]<=b[0])],r:=r+heappop(x),i<=j and(heappush(x,c[(j,i)[d]]),i:=i+d,j:=j-1+d))for _ in range(k)];return r

test('''
2462. Total Cost to Hire K Workers
Medium

512

93

Add to List

Share
You are given a 0-indexed integer array costs where costs[i] is the cost of hiring the ith worker.

You are also given two integers k and candidates. We want to hire exactly k workers according to the following rules:

You will run k sessions and hire exactly one worker in each session.
In each hiring session, choose the worker with the lowest cost from either the first candidates workers or the last candidates workers. Break the tie by the smallest index.
For example, if costs = [3,2,7,7,1,2] and candidates = 2, then in the first hiring session, we will choose the 4th worker because they have the lowest cost [3,2,7,7,1,2].
In the second hiring session, we will choose 1st worker because they have the same lowest cost as 4th worker but they have the smallest index [3,2,7,7,2]. Please note that the indexing may be changed in the process.
If there are fewer than candidates workers remaining, choose the worker with the lowest cost among them. Break the tie by the smallest index.
A worker can only be chosen once.
Return the total cost to hire exactly k workers.

 

Example 1:

Input: costs = [17,12,10,2,7,2,11,20,8], k = 3, candidates = 4
Output: 11
Explanation: We hire 3 workers in total. The total cost is initially 0.
- In the first hiring round we choose the worker from [17,12,10,2,7,2,11,20,8]. The lowest cost is 2, and we break the tie by the smallest index, which is 3. The total cost = 0 + 2 = 2.
- In the second hiring round we choose the worker from [17,12,10,7,2,11,20,8]. The lowest cost is 2 (index 4). The total cost = 2 + 2 = 4.
- In the third hiring round we choose the worker from [17,12,10,7,11,20,8]. The lowest cost is 7 (index 3). The total cost = 4 + 7 = 11. Notice that the worker with index 3 was common in the first and last four workers.
The total hiring cost is 11.
Example 2:

Input: costs = [1,2,4,1], k = 3, candidates = 3
Output: 4
Explanation: We hire 3 workers in total. The total cost is initially 0.
- In the first hiring round we choose the worker from [1,2,4,1]. The lowest cost is 1, and we break the tie by the smallest index, which is 0. The total cost = 0 + 1 = 1. Notice that workers with index 1 and 2 are common in the first and last 3 workers.
- In the second hiring round we choose the worker from [2,4,1]. The lowest cost is 1 (index 2). The total cost = 1 + 1 = 2.
- In the third hiring round there are less than three candidates. We choose the worker from the remaining workers [2,4]. The lowest cost is 2 (index 0). The total cost = 2 + 2 = 4.
The total hiring cost is 4.

Example 3:

Input: costs = [57,33,26,76,14,67,24,90,72,37,30], k = 11, candidates = 2
Output: 526

Constraints:

1 <= costs.length <= 10^5
1 <= costs[i] <= 10^5
1 <= k, candidates <= costs.length
Accepted
17,204
Submissions
45,441
Seen this question in a real interview before?

Yes

No
Maintain two minheaps: one for the left and one for the right.
Compare the top element from two heaps and remove the appropriate one.
Add a new element to the heap and maintain its size as k.
''')

