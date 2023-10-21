from lc import *

# https://leetcode.com/problems/constrained-subsequence-sum/discuss/736798/Python-Thought-process%3A-Recursion-Memoization-Tabulation-Monoqueue
# TLE
class Solution:
    def constrainedSubsetSum(self, a: List[int], k: int) -> int:
        return max(map(f:=cache(lambda j:j>=0 and a[j]+max(0,max(f(j-i)for i in range(1,k+1)))),range(len(a))))

# another solution

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        # bottom-up dp; time = O(n), space = O(k)
        # dp[i] is maximum sum of subsequence of nums[0:=i] ending at i
        ret = nums[0]
        n = len(nums)
        stack = deque() # monotonic stack (decreasing) { i, dp[i] }
        # stack[0][1] is maximum dp[i] within stack
        stack.append((0, nums[0]))
        for i in range(1,n):
            if stack[0][0] + k < i: # stack is always non-empty
                ret = max(ret, stack.popleft()[1])
            dp = nums[i] + (stack and max(0, stack[0][1]))
            while stack and stack[-1][1] <= dp:
                stack.pop()
            stack.append((i, dp))
        return max(ret, stack[0][1])

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        l,n,s=0,len(nums),[(-k-1,0)];return max(((s[l][0]+k>=i or(l:=l+1))and(d:=nums[i]+max(0,l<len(s)and s[l][1])),all(s[-1][1]<=d and s.pop()for _ in range(l,len(s))),s.append((i,d)))[0]for i in range(n))

# https://leetcode.com/problems/constrained-subsequence-sum/discuss/597751/JavaC%2B%2BPython-O(N)-Decreasing-Deque

class Solution:
    def constrainedSubsetSum(self, a: List[int], k: int) -> int:
        d = deque()
        for i in range(len(a)):
            a[i] += d[0] if d else 0
            while d and a[i]>d[-1]:
                d.pop()
            if a[i]>0:
                d.append(a[i])
            if i>=k and d and d[0]==a[i-k]:
                d.popleft()
        return max(a)

class Solution:
    def constrainedSubsetSum(self, a: List[int], k: int) -> int:
        d=deque();[(setitem(a,i,a[i]+(d and d[0]or 0)),all(d and a[i]>d[-1]and d.pop()for _ in a),a[i]>0and d.append(a[i]),i>=k and d and d[0]==a[i-k]and d.popleft())for i in range(len(a))];return max(a)


test('''
1425. Constrained Subsequence Sum
Hard

1309

65

Add to List

Share
Given an integer array nums and an integer k, return the maximum sum of a non-empty subsequence of that array such that for every two consecutive integers in the subsequence, nums[i] and nums[j], where i < j, the condition j - i <= k is satisfied.

A subsequence of an array is obtained by deleting some number of elements (can be zero) from the array, leaving the remaining elements in their original order.

 

Example 1:

Input: nums = [10,2,-10,5,20], k = 2
Output: 37
Explanation: The subsequence is [10, 2, 5, 20].
Example 2:

Input: nums = [-1,-2,-3], k = 1
Output: -1
Explanation: The subsequence must be non-empty, so we choose the largest number.
Example 3:

Input: nums = [10,-2,-10,-5,20], k = 2
Output: 23
Explanation: The subsequence is [10, -2, -5, 20].
 

Constraints:

1 <= k <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
Accepted
32,072
Submissions
64,127
Seen this question in a real interview before?

Yes

No
Maximum Element-Sum of a Complete Subset of Indices
Hard
Use dynamic programming.
Let dp[i] be the solution for the prefix of the array that ends at index i, if the element at index i is in the subsequence.
dp[i] = nums[i] + max(0, dp[i-k], dp[i-k+1], ..., dp[i-1])
Use a heap with the sliding window technique to optimize the dp.
''')

