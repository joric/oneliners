from lc import *

# https://leetcode.com/problems/build-array-where-you-can-find-the-maximum-exactly-k-comparisons/discuss/586693/Clean-Python-3-top-down-DP

class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        return(f:=cache(lambda a,b,c:c==k if a==n else c<=k and sum(f(a+1,max(b,i),c+(i>b))for i in range(1,m+1))))(0,0,0)%(10**9+7)

class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        return(f:=cache(lambda a,b,c:a<n and sum(f(a+1,max(b,i),c+(i>b))for i in range(1,m+1))or c==k))(0,0,0)%(10**9+7)

test('''
1420. Build Array Where You Can Find The Maximum Exactly K Comparisons
Hard

515

11

Add to List

Share
You are given three integers n, m and k. Consider the following algorithm to find the maximum element of an array of positive integers:


You should build the array arr which has the following properties:

arr has exactly n integers.
1 <= arr[i] <= m where (0 <= i < n).
After applying the mentioned algorithm to arr, the value search_cost is equal to k.
Return the number of ways to build the array arr under the mentioned conditions. As the answer may grow large, the answer must be computed modulo 109 + 7.

 

Example 1:

Input: n = 2, m = 3, k = 1
Output: 6
Explanation: The possible arrays are [1, 1], [2, 1], [2, 2], [3, 1], [3, 2] [3, 3]
Example 2:

Input: n = 5, m = 2, k = 3
Output: 0
Explanation: There are no possible arrays that satisify the mentioned conditions.
Example 3:

Input: n = 9, m = 1, k = 1
Output: 1
Explanation: The only possible array is [1, 1, 1, 1, 1, 1, 1, 1, 1]
 

Constraints:

1 <= n <= 50
1 <= m <= 100
0 <= k <= n
''')

