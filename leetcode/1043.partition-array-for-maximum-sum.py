from lc import *

# https://leetcode.com/problems/partition-array-for-maximum-sum/discuss/290863/JavaC++Python-DP-O(K)-Space/832770

class Solution:
    def maxSumAfterPartitioning(self, a: List[int], k: int) -> int:
        n,d = len(a),[0]*k
        for i in range(n-1,-1,-1):
            m = b = 0
            for j in range(i,min(n,i+k)):
                m = max(m,a[j])
                b = max(b,(j-i+1)*m + d[(j+1)%k])
            d[i%k] = b
        return d[0]

# https://leetcode.com/problems/partition-array-for-maximum-sum/discuss/290954/python3-5-lines-beat-100

class Solution:
    def maxSumAfterPartitioning(self, a: List[int], k: int) -> int:
        d = [max(a[:i+1])*(i+1) for i in range(k)]
        for i in range(k,len(a)):
            m = max(d[j] + max(a[i-k+j+1:i+1])*(k-j)for j in range(k))
            d = d[1:]+[m]
        return max(d)

# https://leetcode.com/problems/partition-array-for-maximum-sum/discuss/729771/Python-Recursive-to-Tabulated

class Solution:
    def maxSumAfterPartitioning(self, a: List[int], k: int) -> int:
        return(f:=cache(lambda i,m=0:a[i:]and max((m:=max(m,a[j]))*(j-i+1)+f(j+1)for j in range(i,min(i+k,len(a))))or 0))(0)

# https://leetcode.com/problems/partition-array-for-maximum-sum/discuss/1474132/Python-recursion-intuitive-code

class Solution:
    def maxSumAfterPartitioning(self, a: List[int], k: int) -> int:
        return(f:=cache(lambda i:a[i:]and max(f(j)+max(a[i:j])*(j-i)for j in range(i+1,min(i+k,len(a))+1))or 0))(0)

test('''
1043. Partition Array for Maximum Sum
Medium

3876

281

Add to List

Share
Given an integer array arr, partition the array into (contiguous) subarrays of length at most k. After partitioning, each subarray has their values changed to become the maximum value of that subarray.

Return the largest sum of the given array after partitioning. Test cases are generated so that the answer fits in a 32-bit integer.

 

Example 1:

Input: arr = [1,15,7,9,2,5,10], k = 3
Output: 84
Explanation: arr becomes [15,15,15,9,10,10,10]
Example 2:

Input: arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4
Output: 83
Example 3:

Input: arr = [1], k = 1
Output: 1
 

Constraints:

1 <= arr.length <= 500
0 <= arr[i] <= 10^9
1 <= k <= arr.length
Accepted
101,709
Submissions
138,598
''')