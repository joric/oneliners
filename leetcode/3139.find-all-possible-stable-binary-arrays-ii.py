from lc import *

# https://leetcode.com/problems/find-all-possible-stable-binary-arrays-ii/solutions/5162587/simple-solution-less-than-15-lines-beats-0fnx/

class Solution:
    def numberOfStableArrays(self, z: int, o: int, l: int) -> int:
        a,b=[[[0]*(max(o,l)+2)for _ in range(max(z,l)+2)]for _ in range(2)]
        for i in range(l+1):
            a[i][0] = 1
            b[0][i] = 1
        for i in range(1,z+1):
            for j in range(1, o + 1):
                b[i][j] += b[i][j - 1] - a[i][j - 1 - l] + a[i][j - 1]
                a[i][j] += a[i - 1][j] - b[i - 1 - l][j] + b[i - 1][j]
        return(a[z][o]+b[z][o])%(10**9+7)

class Solution:
    def numberOfStableArrays(self, z: int, o: int, l: int) -> int:
        f=cache(lambda i,j,k:0 if i<0 or j<0 else int(0<i<=l) if k==0 and j==0 else int(0<j<=l) if k==1 and i==0 else f(i-1,j,0)+f(i-1,j,1)-f(i-1-l,j,1) if k==0 else f(i,j-1,1)+f(i,j-1,0)-f(i,j-1-l,0));return(f(z,o,0)+f(z,o,1))%(10**9+7)

class Solution:
    def numberOfStableArrays(self, z: int, o: int, l: int) -> int:
        f=cache(lambda i,j,k:0 if i<0 or j<0 else(0<j<=l if i==0 else f(i,j-1,1)+f(i,j-1,0)-f(i,j-1-l,0))if k else(0<i<=l if j==0 else f(i-1,j,0)+f(i-1,j,1)-f(i-1-l,j,1)));return(f(z,o,0)+f(z,o,1))%(10**9+7)

class Solution:
    def numberOfStableArrays(self, z: int, o: int, l: int) -> int:
        f=cache(lambda i,j,k:0 if i<0 or j<0 else(0<(i,j)[k]<=l if (j,i)[k]==0 else f(i-1+k,j-k,0)+f(i-1+k,j-k,1)-f(i-(1-k)*(l+1),j-k*(l+1),1-k)));return(f(z,o,0)+f(z,o,1))%(10**9+7)

class Solution:
    def numberOfStableArrays(self, z: int, o: int, l: int) -> int:
        f=cache(lambda i,j:0 if i<0 or j<0 else 0<i<=l if j==0 else f(i-1,j)+f(j,i-1)-f(j,i-1-l));return(f(z,o)+f(o,z))%(10**9+7)

class Solution:
    def numberOfStableArrays(self, z: int, o: int, l: int) -> int:
        f=cache(lambda i,j:i>=0<=j and(0<i<=l if j<1 else f(i-1,j)+f(j,i-1)-f(j,i+~l)));return(f(z,o)+f(o,z))%(10**9+7)

class Solution:
    def numberOfStableArrays(self, z: int, o: int, l: int) -> int:
        f=cache(lambda i,j:i>-1<j and(f(i-1,j)+f(j,i-1)-f(j,i+~l)if j else 0<i<=l));return(f(z,o)+f(o,z))%(10**9+7)

class Solution:
    def numberOfStableArrays(self, z: int, o: int, l: int) -> int:
        f=cache(lambda i,j:i|j>0 and(f(i-1,j)+f(j,i-1)-f(j,i+~l)if j else 0<i<=l));return(f(z,o)+f(o,z))%(10**9+7)

class Solution:
    def numberOfStableArrays(self, z: int, o: int, l: int) -> int:
        f=cache(lambda i,j:i|j>0 and(f(i-1,j)+f(j,i-1)-f(j,i+~l)if j else i<=l));return(f(z,o)+f(o,z))%(10**9+7)

# POTD 2026-03-10

class Solution: # MLE
    def numberOfStableArrays(self, z: int, o: int, l: int) -> int:
        f=cache(lambda i,j:i|j>0 and(i<=l,f(i-1,j)+f(j,i-1)-f(j,i+~l))[j>0]);return(f(z,o)+f(o,z))%(10**9+7)

class Solution:
    def numberOfStableArrays(self, z: int, o: int, l: int) -> int:
        f=cache(lambda i,j:i|j>0 and(i<=l,f(i-1,j)+f(j,i-1)-f(j,i+~l))[j>0]);return(f(z,o)+f(o,z),f.cache_clear())[0]%(10**9+7)

test('''
3130. Find All Possible Stable Binary Arrays II
Hard
Topics
premium lock icon
Companies
Hint
You are given 3 positive integers zero, one, and limit.

A binary array arr is called stable if:

The number of occurrences of 0 in arr is exactly zero.
The number of occurrences of 1 in arr is exactly one.
Each subarray of arr with a size greater than limit must contain both 0 and 1.
Return the total number of stable binary arrays.

Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:

Input: zero = 1, one = 1, limit = 2

Output: 2

Explanation:

The two possible stable binary arrays are [1,0] and [0,1].

Example 2:

Input: zero = 1, one = 2, limit = 1

Output: 1

Explanation:

The only possible stable binary array is [1,0,1].

Example 3:

Input: zero = 3, one = 3, limit = 2

Output: 14

Explanation:

All the possible stable binary arrays are [0,0,1,0,1,1], [0,0,1,1,0,1], [0,1,0,0,1,1], [0,1,0,1,0,1], [0,1,0,1,1,0], [0,1,1,0,0,1], [0,1,1,0,1,0], [1,0,0,1,0,1], [1,0,0,1,1,0], [1,0,1,0,0,1], [1,0,1,0,1,0], [1,0,1,1,0,0], [1,1,0,0,1,0], and [1,1,0,1,0,0].

 

Constraints:

1 <= zero, one, limit <= 1000
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
4,560/16.2K
Acceptance Rate
28.2%
Topics
Principal
Dynamic Programming
Prefix Sum
Biweekly Contest 129
icon
Companies
Hint 1
Let dp[x][y][z = 0/1] be the number of stable arrays with exactly x zeros, y ones, and the last element is z. (0 or 1). dp[x][y][0] + dp[x][y][1] is the answer for given (x, y).
Hint 2
If we have already placed x 1 and y 0, if we place a group of k 0, the number of ways is dp[x-k][y][1]. We can place a group with size i, where i varies from 1 to min(limit, zero - x). Similarly, we can solve by placing a group of ones.
Hint 3
Speed up the calculation using prefix arrays to store the sum of dp states.
Similar Questions
Contiguous Array
Medium
Binary Subarrays With Sum
Medium
''')
