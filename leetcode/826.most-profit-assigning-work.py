from lc import *

# https://leetcode.com/problems/most-profit-assigning-work/discuss/222641/One-line-javascript-solution-%3A)
# JS version: maxProfitAssignment=(d,p,w)=>w.reduce((t,x)=>t+d.reduce((v,y,i)=>y<=x&&p[i]>v?p[i]:v,0),0)
# sadly, Python version gives TLE

class Solution:
    def maxProfitAssignment(self, d: List[int], p: List[int], w: List[int]) -> int:
        return reduce(lambda t,x:t+reduce(lambda v,q:(t:=q[1],v)[x<q[0]or v>t],zip(d,p),0),w,0)

# https://leetcode.com/problems/most-profit-assigning-work/discuss/127031/C%2B%2BJavaPython-Sort-and-Two-pointer

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(zip(difficulty, profit))
        res = i = best = 0
        for ability in sorted(worker):
            while i < len(jobs) and ability >= jobs[i][0]:
                best = max(jobs[i][1], best)
                i += 1
            res += best
        return res

class Solution:
    def maxProfitAssignment(self, d: List[int], p: List[int], w: List[int]) -> int:
        i=b=0;j=sorted(zip(d,p));return sum((all(j[i:]and a>=j[i][0]and(b:=max(j[i][1],b),i:=i+1)for _ in j),b)[1]for a in sorted(w))

test('''
826. Most Profit Assigning Work
Medium

1757

149

Add to List

Share
You have n jobs and m workers. You are given three arrays: difficulty, profit, and worker where:

difficulty[i] and profit[i] are the difficulty and the profit of the ith job, and
worker[j] is the ability of jth worker (i.e., the jth worker can only complete a job with difficulty at most worker[j]).
Every worker can be assigned at most one job, but one job can be completed multiple times.

For example, if three workers attempt the same job that pays $1, then the total profit will be $3. If a worker cannot complete any job, their profit is $0.
Return the maximum profit we can achieve after assigning the workers to the jobs.

 

Example 1:

Input: difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
Output: 100
Explanation: Workers are assigned jobs of difficulty [4,4,6,6] and they get a profit of [20,20,30,30] separately.
Example 2:

Input: difficulty = [85,47,57], profit = [24,66,99], worker = [40,25,25]
Output: 0

Other examples:

Input: difficulty = [64,88,97], profit = [53,86,89], worker = [98,11,6]
Output: 89

Constraints:

n == difficulty.length
n == profit.length
m == worker.length
1 <= n, m <= 104
1 <= difficulty[i], profit[i], worker[i] <= 105
Accepted
96,796
Submissions
193,762
''')