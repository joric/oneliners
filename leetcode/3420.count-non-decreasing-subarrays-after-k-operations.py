from lc import *

# https://leetcode.com/problems/count-non-decreasing-subarrays-after-k-operations/solutions/6267498/python-mono-decreasing-deque-on-by-lee21-nywu/?envType=daily-question&envId=2026-11-13

class Solution:
    def countNonDecreasingSubarrays(self, a: List[int], k: int) -> int:
        a = a[::-1]
        res = 0
        q = deque()
        i = 0
        for j in range(len(a)):
            while q and a[q[-1]] < a[j]:
                r = q.pop()
                l = q[-1] if q else i - 1
                k -= (r - l) * (a[j] - a[r])
            q.append(j)
            while k < 0:
                k += a[q[0]] - a[i]
                if q[0] == i:
                    q.popleft()
                i += 1
            res += j - i + 1
        return res

class Solution:
    def countNonDecreasingSubarrays(self, a: List[int], k: int) -> int:
        q=[p:=0];a=[9e9]+a[::-1];return sum((all(a[x]<a[j]and[k:=k-(max(x,p)-max(q[-2],p))*(a[j]-a[q.pop()])]for x in reversed(q)),q.append(j),all(k<0and[k:=k+a[q[bisect_right(q,p)]]-a[(p:=p+1)]]for _ in a))and j-p for j in range(1,len(a)))

test('''
3420. Count Non-Decreasing Subarrays After K Operations
Hard
Topics
premium lock icon
Companies
Hint
You are given an array nums of n integers and an integer k.

For each subarray of nums, you can apply up to k operations on it. In each operation, you increment any element of the subarray by 1.

Note that each subarray is considered independently, meaning changes made to one subarray do not persist to another.

Return the number of subarrays that you can make non-decreasing ​​​​​after performing at most k operations.

An array is said to be non-decreasing if each element is greater than or equal to its previous element, if it exists.

 

Example 1:

Input: nums = [6,3,1,2,4,4], k = 7

Output: 17

Explanation:

Out of all 21 possible subarrays of nums, only the subarrays [6, 3, 1], [6, 3, 1, 2], [6, 3, 1, 2, 4] and [6, 3, 1, 2, 4, 4] cannot be made non-decreasing after applying up to k = 7 operations. Thus, the number of non-decreasing subarrays is 21 - 4 = 17.

Example 2:

Input: nums = [6,3,1,3,6], k = 4

Output: 12

Explanation:

The subarray [3, 1, 3, 6] along with all subarrays of nums with three or fewer elements, except [6, 3, 1], can be made non-decreasing after k operations. There are 5 subarrays of a single element, 4 subarrays of two elements, and 2 subarrays of three elements except [6, 3, 1], so there are 1 + 5 + 4 + 2 = 12 subarrays that can be made non-decreasing.

 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= k <= 109
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
5,113/19.8K
Acceptance Rate
25.9%
Topics
Principal
Array
Stack
Segment Tree
Queue
Sliding Window
Monotonic Stack
Monotonic Queue
Weekly Contest 432
icon
Companies
Hint 1
Use a sparse table.
Hint 2
Compute sp[e][i] = [lastElement, operations] where operations is the number of operations required to make the subarray nums[i...i + 2^e - 1] non-decreasing, and lastElement be the value of the last element after the operations were applied on it.
Hint 3
How can we combine sp[a][i] with sp[b][i + 2^a] to find the answer for the subarray nums[i...i + 2^a + 2^b - 1]?
Similar Questions
Non-decreasing Array
Medium
''')
