from lc import *

# biweekly-contest-122 Q4
# https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-ii

# https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-ii/solutions/4598346/python3-sortedlist-sliding-window/

class Solution:
    def minimumCost(self, a: List[int], k: int, d: int) -> int:
        n,s,m = len(a),__import__('sortedcontainers').SortedList(a[1:1+d]),inf
        c = sum(s[:k-2])
        for i in range(1+d,n):
            c += a[i]if s.bisect(a[i])<=k-2 else s[k-2]
            m = min(m,c)
            s.add(a[i])
            c -= a[i-d]if s.bisect(a[i-d])<=k-2 else s[k-2]
            s.remove(a[i-d])
        return a[0]+m

class Solution:
    def minimumCost(self, a: List[int], k: int, d: int) -> int:
        n,s,m=len(a),__import__('sortedcontainers').SortedList(a[1:1+d]),inf;c=sum(s[:k-2]);[(c:=c+(a[i]if s.bisect(a[i])<=k-2 else s[k-2]),m:=min(m,c),s.add(a[i]),c:=c-(a[i-d]if s.bisect(a[i-d])<=k-2 else s[k-2]),s.remove(a[i-d]))for i in range(1+d,n)];return a[0]+m

# POTD 2026-02-02 SortedList is globally available now

class Solution:
    def minimumCost(self, a: List[int], k: int, d: int) -> int:
        n,s,m=len(a),SortedList(a[1:1+d]),inf;c=sum(s[:k-2]);[(c:=c+(a[i]if s.bisect(a[i])<=k-2 else s[k-2]),m:=min(m,c),s.add(a[i]),c:=c-(a[i-d]if s.bisect(a[i-d])<=k-2 else s[k-2]),s.remove(a[i-d]))for i in range(1+d,n)];return a[0]+m

class Solution:
    def minimumCost(self, a: List[int], k: int, d: int) -> int:
        n,s,m=len(a),SortedList(a[1:1+d]),inf;c=sum(s[:k-2]);[(m:=min(m,c:=c+(a[i]if s.bisect(a[i])<=k-2 else s[k-2])),s.add(a[i]),c:=c-(a[i-d]if s.bisect(a[i-d])<=k-2 else s[k-2]),s.remove(a[i-d]))for i in range(1+d,n)];return a[0]+m

test('''
3013. Divide an Array Into Subarrays With Minimum Cost II
Hard
Companies
Hint
You are given a 0-indexed array of integers nums of length n, and two positive integers k and dist.

The cost of an array is the value of its first element. For example, the cost of [1,2,3] is 1 while the cost of [3,4,1] is 3.

You need to divide nums into k disjoint contiguous 
subarrays
, such that the difference between the starting index of the second subarray and the starting index of the kth subarray should be less than or equal to dist. In other words, if you divide nums into the subarrays nums[0..(i1 - 1)], nums[i1..(i2 - 1)], ..., nums[ik-1..(n - 1)], then ik-1 - i1 <= dist.

Return the minimum possible sum of the cost of these subarrays.

 

Example 1:

Input: nums = [1,3,2,6,4,2], k = 3, dist = 3
Output: 5
Explanation: The best possible way to divide nums into 3 subarrays is: [1,3], [2,6,4], and [2]. This choice is valid because ik-1 - i1 is 5 - 2 = 3 which is equal to dist. The total cost is nums[0] + nums[2] + nums[5] which is 1 + 2 + 2 = 5.
It can be shown that there is no possible way to divide nums into 3 subarrays at a cost lower than 5.
Example 2:

Input: nums = [10,1,2,2,2,1], k = 4, dist = 3
Output: 15
Explanation: The best possible way to divide nums into 4 subarrays is: [10], [1], [2], and [2,2,1]. This choice is valid because ik-1 - i1 is 3 - 1 = 2 which is less than dist. The total cost is nums[0] + nums[1] + nums[2] + nums[3] which is 10 + 1 + 2 + 2 = 15.
The division [10], [1], [2,2,2], and [1] is not valid, because the difference between ik-1 and i1 is 5 - 1 = 4, which is greater than dist.
It can be shown that there is no possible way to divide nums into 4 subarrays at a cost lower than 15.
Example 3:

Input: nums = [10,8,18,9], k = 3, dist = 1
Output: 36
Explanation: The best possible way to divide nums into 4 subarrays is: [10], [8], and [18,9]. This choice is valid because ik-1 - i1 is 2 - 1 = 1 which is equal to dist.The total cost is nums[0] + nums[1] + nums[2] which is 10 + 8 + 18 = 36.
The division [10], [8,18], and [9] is not valid, because the difference between ik-1 and i1 is 3 - 1 = 2, which is greater than dist.
It can be shown that there is no possible way to divide nums into 3 subarrays at a cost lower than 36.
 

Constraints:

3 <= n <= 10^5
1 <= nums[i] <= 10^9
3 <= k <= n
k - 2 <= dist <= n - 2
''')

