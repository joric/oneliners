from lc import *

# https://leetcode.com/problems/minimum-sum-of-squared-difference/solutions/2260532/python-9-lines-solution-and-a-more-effic-w92a/?envType=daily-question&envId=2026-10-10

class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        heap = [-abs(nums1[i] - nums2[i]) for i in range(len(nums1))]
        heapify(heap)
        k, n = k1 + k2, len(nums1)
        while k > 0 and heap[0] < 0:
            i = heappop(heap)
            delta = min(max(k // n, 1), -i)
            heappush(heap, i + delta)
            k -= delta
        return sum(i * i for i in heap)

class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        d=[abs(a-b)for a,b in zip(nums1,nums2)];k=k1+k2;t=bisect_left(range(max(d)+1),1,key=lambda t:sum(max(0,x-t)for x in d)<=k);return sum(min(x,t)**2 for x in d)-(t>0)*(k-sum(max(0,x-t)for x in d))*(2*t-1)

class Solution:
    def minSumSquareDiff(self, a: List[int], b: List[int], c: int, d: int) -> int:
        v=[*map(abs,map(sub,a,b))];f=lambda h:sum(min(0,h-x)for x in v);h=bisect_left(range(9**6),-c-d,key=f);return h and sum(min(x,h)**2for x in v)-(c+d+f(h))*(2*h-1)

test('''
2333. Minimum Sum of Squared Difference
Medium
Topics
premium lock icon
Companies
Hint
You are given two positive 0-indexed integer arrays nums1 and nums2, both of length n.

The sum of squared difference of arrays nums1 and nums2 is defined as the sum of (nums1[i] - nums2[i])2 for each 0 <= i < n.

You are also given two positive integers k1 and k2. You can modify any of the elements of nums1 by +1 or -1 at most k1 times. Similarly, you can modify any of the elements of nums2 by +1 or -1 at most k2 times.

Return the minimum sum of squared difference after modifying array nums1 at most k1 times and modifying array nums2 at most k2 times.

Note: You are allowed to modify the array elements to become negative integers.

 

Example 1:

Input: nums1 = [1,2,3,4], nums2 = [2,10,20,19], k1 = 0, k2 = 0
Output: 579
Explanation: The elements in nums1 and nums2 cannot be modified because k1 = 0 and k2 = 0. 
The sum of square difference will be: (1 - 2)2 + (2 - 10)2 + (3 - 20)2 + (4 - 19)2 = 579.
Example 2:

Input: nums1 = [1,4,10,12], nums2 = [5,8,6,9], k1 = 1, k2 = 1
Output: 43
Explanation: One way to obtain the minimum sum of square difference is: 
- Increase nums1[0] once.
- Increase nums2[2] once.
The minimum of the sum of square difference will be: 
(2 - 5)2 + (4 - 8)2 + (10 - 7)2 + (12 - 9)2 = 43.
Note that, there are other ways to obtain the minimum of the sum of square difference, but there is no way to obtain a sum smaller than 43.
 

Constraints:

n == nums1.length == nums2.length
1 <= n <= 105
0 <= nums1[i], nums2[i] <= 105
0 <= k1, k2 <= 109
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
20,192/74.4K
Acceptance Rate
27.1%
Topics
Staff
Array
Binary Search
Greedy
Sorting
Heap (Priority Queue)
Biweekly Contest 82
icon
Companies
Hint 1
There is no difference between the purpose of k1 and k2. Adding +1 to one element in nums1 is same as performing -1 to one element in nums2, and vice versa.
Hint 2
Reduce the sum of squared difference greedily. One operation of k should use the index that has the current maximum difference.
Hint 3
Binary search the maximum difference for the final result.
Similar Questions
Minimum Absolute Sum Difference
Medium
Partition Array Into Two Arrays to Minimize Sum Difference
Hard
''')
