from lc import *

# https://leetcode.com/problems/minimum-cost-to-hire-k-workers/discuss/141768/Detailed-explanation-O(NlogN)

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        workers = sorted([float(w) / q, q] for w, q in zip(wage, quality))
        res = float('inf')
        qsum = 0
        heap = []
        for r, q in workers:
            heapq.heappush(heap, -q)
            qsum += q
            if len(heap) > k: qsum += heapq.heappop(heap)
            if len(heap) == k: res = min(res, qsum * r)
        return res

class Solution:
    def mincostToHireWorkers(self, q: List[int], w: List[int], k: int) -> float:
        r = inf
        s = 0
        h = []
        for q,w in sorted((w/q,q)for w,q in zip(w,q)):
            heappush(h, -w)
            s += w
            if len(h) > k:
                s += heappop(h)
            if len(h) == k:
                r = min(r, s * q)
        return r

class Solution:
    def mincostToHireWorkers(self, q: List[int], w: List[int], k: int) -> float:
        s,h=0,[];return min(s*q for q,w in sorted((w/q,q)for w,q in zip(w,q))if(heappush(h,-w),s:=s+w,k<len(h)and(s:=s+heappop(h)))and len(h)==k)

class Solution:
    def mincostToHireWorkers(self, q: List[int], w: List[int], k: int) -> float:
        s,h=0,[];return min(s*q for q,w in sorted((w/q,q)for w,q in zip(w,q))if(heappush(h,-w),s:=s+w+(k<len(h)and heappop(h)))and h[k-1:])

test('''
857. Minimum Cost to Hire K Workers
Hard

2203

287

Add to List

Share
There are n workers. You are given two integer arrays quality and wage where quality[i] is the quality of the ith worker and wage[i] is the minimum wage expectation for the ith worker.

We want to hire exactly k workers to form a paid group. To hire a group of k workers, we must pay them according to the following rules:

Every worker in the paid group must be paid at least their minimum wage expectation.
In the group, each worker's pay must be directly proportional to their quality. This means if a worker’s quality is double that of another worker in the group, then they must be paid twice as much as the other worker.
Given the integer k, return the least amount of money needed to form a paid group satisfying the above conditions. Answers within 10-5 of the actual answer will be accepted.

 

Example 1:

Input: quality = [10,20,5], wage = [70,50,30], k = 2
Output: 105.00000
Explanation: We pay 70 to 0th worker and 35 to 2nd worker.
Example 2:

Input: quality = [3,1,10,10,1], wage = [4,8,2,2,7], k = 3
Output: 30.66667
Explanation: We pay 4 to 0th worker, 13.33333 to 2nd and 3rd workers separately.
 

Constraints:

n == quality.length == wage.length
1 <= k <= n <= 104
1 <= quality[i], wage[i] <= 104
Accepted
65,496
Submissions
123,635
''')
