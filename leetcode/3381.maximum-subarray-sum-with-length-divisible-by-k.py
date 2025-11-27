from lc import *

# https://leetcode.com/problems/maximum-subarray-sum-with-length-divisible-by-k/solutions/6124606/dp-in-5-lines-of-python3-by-metaphysical-j29a/?envType=daily-question&envId=2025-11-27

class Solution:
    def maxSubarraySum(self, a: List[int], k: int) -> int:
        n = len(a)
        p = [0,*accumulate(a)]
        d = [-inf]*(n+1)
        for i in range(k,n+1):
            d[i]=(p[i]-p[i-k])+max(0,d[i-k])
        return max(d)

# https://leetcode.com/problems/maximum-subarray-sum-with-length-divisible-by-k/solutions/6141294/memoziationrecursive-solution-by-farzan_-uqzy/?envType=daily-question&envId=2025-11-27

class Solution:
    def maxSubarraySum(self, a: List[int], k: int) -> int:
        s=[*accumulate(a)]
        q=lambda l,r:l and s[r]-s[l-1]or s[r]
        f=cache(lambda i:i>=k-1 and max(q(i-k+1,i),q(i-k+1,i)+f(i-k)))
        return max(f(i)for i in range(k-1,len(a)))

class Solution:
    def maxSubarraySum(self, a: List[int], k: int) -> int:
        s=[*accumulate(a)]
        q=lambda l,r:l and s[r]-s[l-1]or s[r]
        return max(map(f:=cache(lambda i:i>=k-1 and max(q(i-k+1,i),q(i-k+1,i)+f(i-k))),range(k-1,len(a))))

# https://leetcode.com/problems/maximum-subarray-sum-with-length-divisible-by-k/solutions/6124583/javacpython-best-time-to-buy-and-sell-st-u6fb/?envType=daily-question&envId=2025-11-27

class Solution:
    def maxSubarraySum(self, a: List[int], k: int) -> int:
        prefix = [inf] * k
        prefix[-1] = 0
        res = -inf
        for i, pre in enumerate(accumulate(a)):
            res = max(res, pre - prefix[i % k])
            prefix[i % k] = min(prefix[i % k], pre)
        return res

class Solution:
    def maxSubarraySum(self, a: List[int], k: int) -> int:
        p=defaultdict(lambda:inf);p[k-1]=0;return max((s-p[t:=i%k],p.update({t:min(s,p[t])}))[0]for i,s in enumerate(accumulate(a)))

class Solution:
    def maxSubarraySum(self, a: List[int], k: int) -> int:
        p=[inf]*~-k+[0];return max((s-p[i%k],setitem(p,i%k,min(p[i%k],s)))[0]for i,s in enumerate(accumulate(a)))

class Solution:
    def maxSubarraySum(self, a: List[int], k: int) -> int:
        p=[inf]*~-k+[0];return max((s-p[t:=i%k],setitem(p,t,min(s,p[t])))[0]for i,s in enumerate(accumulate(a)))

class Solution:
    def maxSubarraySum(self, a: List[int], k: int) -> int:
        p,s=[inf]*~-k+[0],0;return max(((s:=s+x)-p[t:=i%k],setitem(p,t,min(s,p[t])))[0]for i,x in enumerate(a))

test('''
3381. Maximum Subarray Sum With Length Divisible by K
Solved
Medium
Topics
premium lock icon
Companies
Hint
You are given an array of integers nums and an integer k.

Return the maximum sum of a subarray of nums, such that the size of the subarray is divisible by k.

 

Example 1:

Input: nums = [1,2], k = 1

Output: 3

Explanation:

The subarray [1, 2] with sum 3 has length equal to 2 which is divisible by 1.

Example 2:

Input: nums = [-1,-2,-3,-4,-5], k = 4

Output: -10

Explanation:

The maximum sum subarray is [-1, -2, -3, -4] which has length equal to 4 which is divisible by 4.

Example 3:

Input: nums = [-5,1,2,-3,4], k = 2

Output: 4

Explanation:

The maximum sum subarray is [1, 2, -3, 4] which has length equal to 4 which is divisible by 2.

 

Constraints:

1 <= k <= nums.length <= 2 * 105
-109 <= nums[i] <= 109
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
13,808/48.9K
Acceptance Rate
28.2%
Topics
Array
Hash Table
Prefix Sum
Weekly Contest 427
icon
Companies
Hint 1
Maintain minimum prefix sum ending at every possible index%k.
Similar Questions
Subarray Sums Divisible by K
Medium
''')
