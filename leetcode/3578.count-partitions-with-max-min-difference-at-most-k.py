from lc import *

# https://leetcode.com/problems/count-partitions-with-max-min-difference-at-most-k/solutions/6821972/recursive-to-optimal-solution-memoizatio-qlce/
# TLE

class Solution:
    def countPartitions(self, a: List[int], k: int) -> int:
        @cache
        def f(i):
            n = len(a)
            if i == n:
                return 1
            w = 0
            l,r = inf,-inf
            for j in range(i,n):
                x = a[j]
                l = min(l,x)
                r = max(r,x)
                if r - l > k:
                    break
                w += f(j+1)
            return w
        return f(0) %(10**9+7)

class Solution:
    def countPartitions(self, a: List[int], k: int) -> int:
        return(f:=cache(lambda i,l=inf,r=-inf:i<(n:=len(a))and sum(f(j+1)for j in range(i,n)if(r:=max(r,a[j]))-(l:=min(l,a[j]))<=k)%(10**9+7)or 1))(0)

# https://leetcode.com/problems/count-partitions-with-max-min-difference-at-most-k/description/?envType=daily-question&envId=2025-12-06

class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        left, cnt, mod_ = 0, 1, 1_000_000_007
        mnQueue, mxQueue, dp = deque(), deque(), [cnt]
        for rght, num in enumerate(nums):
            while mxQueue and num > nums[mxQueue[-1]]:
                mxQueue.pop()
            while mnQueue and num < nums[mnQueue[-1]]:
                mnQueue.pop()
            mxQueue.append(rght)
            mnQueue.append(rght)
            while nums[mxQueue[0]] - nums[mnQueue[0]] > k:
                cnt-= dp[left]
                left+= 1
                if left > mnQueue[0]: mnQueue.popleft()
                if left > mxQueue[0]: mxQueue.popleft()
            dp.append(cnt)
            cnt*= 2
            cnt%= mod_
        return dp[-1] %mod_

# https://leetcode.com/problems/count-partitions-with-max-min-difference-at-most-k/solutions/6824546/python3-beats-100-time-and-space-sliding-okp3/?envType=daily-question&envId=2025-12-06

class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        mod = 10**9 + 7
        n = len(nums)
        min_stack = []
        max_stack = []
        prefix = [0, 1]
        val = -1
        j = 0
        Window = SortedList()
        for i in range(n):
            Window.add(nums[i])
            while j <= i and Window[-1]-Window[0] > k:
                Window.remove(nums[j])            
                j+=1
            val = (prefix[-1] - prefix[j] + mod) %mod
            prefix.append((val + prefix[-1]) %mod)
        return val

class Solution:
    def countPartitions(self, a: List[int], k: int) -> int:
        n,p,v,j,w=len(a),[0,1],-1,0,SortedList()
        for i in range(n):
            w.add(a[i])
            all(j<=i and k<w[-1]-w[0]and(w.remove(a[j]),j:=j+1)for _ in a)
            p.append(((v:=p[-1]-p[j])+p[-1]))
        return v%(10**9+7)

class Solution:
    def countPartitions(self, a: List[int], k: int) -> int:
        p,v,j,w=[0,1],-1,0,SortedList();[(w.add(x),all(j<i and k<w[-1]-w[0]and(w.remove(a[j]),j:=j+1)for _ in a),p.append(p[-1]+(v:=p[-1]-p[j])))for i,x in enumerate(a)];return v%(10**9+7)

class Solution:
    def countPartitions(self, a: List[int], k: int) -> int:
        v=j=-1;p,w=[0,1],SortedList()
        for i,x in enumerate(a):
            w.add(x)
            all(j<i and k<w[-1]-w[0]and[w.remove(a[j:=j+1])]for _ in a)
            p.append((v:=p[-1]-p[j+1])+p[-1])
        return v%(10**9+7)

class Solution:
    def countPartitions(self, a: List[int], k: int) -> int:
        v=j=-1;p,w=[0,1],SortedList();[(w.add(x),all(j<i and k<w[-1]-w[0]!=w.remove(a[j:=j+1])for _ in a),p.append(p[-1]+(v:=p[-1]-p[j+1])))for i,x in enumerate(a)];return v%(10**9+7)

test('''
3578. Count Partitions With Max-Min Difference at Most K
Solved
Medium
Topics
premium lock icon
Companies
Hint
You are given an integer array nums and an integer k. Your task is to partition nums into one or more non-empty contiguous segments such that in each segment, the difference between its maximum and minimum elements is at most k.

Return the total number of ways to partition nums under this condition.

Since the answer may be too large, return it modulo 109 + 7.

 

Example 1:

Input: nums = [9,4,1,3,7], k = 4

Output: 6

Explanation:

There are 6 valid partitions where the difference between the maximum and minimum elements in each segment is at most k = 4:

[[9], [4], [1], [3], [7]]
[[9], [4], [1], [3, 7]]
[[9], [4], [1, 3], [7]]
[[9], [4, 1], [3], [7]]
[[9], [4, 1], [3, 7]]
[[9], [4, 1, 3], [7]]
Example 2:

Input: nums = [3,3,4], k = 0

Output: 2

Explanation:

There are 2 valid partitions that satisfy the given conditions:

[[3], [3], [4]]
[[3, 3], [4]]
 

Constraints:

2 <= nums.length <= 5 * 104
1 <= nums[i] <= 109
0 <= k <= 109
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
10,018/26.8K
Acceptance Rate
37.3%
Topics
Array
Dynamic Programming
Queue
Sliding Window
Prefix Sum
Monotonic Queue
Weekly Contest 453
icon
Companies
Hint 1
Use dynamic programming.
Hint 2
Let dp[idx] be the count of ways to partition the array with the last partition ending at index idx.
Hint 3
Try using a sliding window; we can track the minimum and maximum in the window using deques.
Similar Questions
Number of Great Partitions
Hard
''')
