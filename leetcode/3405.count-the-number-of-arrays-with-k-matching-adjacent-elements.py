from lc import *

# https://leetcode.com/problems/count-the-number-of-arrays-with-k-matching-adjacent-elements/solutions/6207891/ans-comb-n-1-n-k-1-m-m-1-n-k-1/?envType=daily-question&envId=2025-06-17

class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        return comb(n-1,n-k-1)*m*(m-1)**(n-k-1)%(10**9+7)

# https://leetcode.com/problems/count-the-number-of-arrays-with-k-matching-adjacent-elements/solutions/6212204/by-formula/?envType=daily-question&envId=2025-06-17

class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        return(m-1)**(n-1-k)*m*comb(n-1,k)%(10**9+7)

class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        return(m-1)**(n+~k)*m*comb(n-1,k)%(10**9+7)

test('''
3405. Count the Number of Arrays with K Matching Adjacent Elements
Solved
Hard
Topics
premium lock icon
Companies
Hint
You are given three integers n, m, k. A good array arr of size n is defined as follows:

Each element in arr is in the inclusive range [1, m].
Exactly k indices i (where 1 <= i < n) satisfy the condition arr[i - 1] == arr[i].
Return the number of good arrays that can be formed.

Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:

Input: n = 3, m = 2, k = 1

Output: 4

Explanation:

There are 4 good arrays. They are [1, 1, 2], [1, 2, 2], [2, 1, 1] and [2, 2, 1].
Hence, the answer is 4.
Example 2:

Input: n = 4, m = 2, k = 2

Output: 6

Explanation:

The good arrays are [1, 1, 1, 2], [1, 1, 2, 2], [1, 2, 2, 2], [2, 1, 1, 1], [2, 2, 1, 1] and [2, 2, 2, 1].
Hence, the answer is 6.
Example 3:

Input: n = 5, m = 2, k = 0

Output: 2

Other solutions:

Input: n = 1, m = 1, k = 0
Output: 1

Input: n = 10, m = 9, k = 0
Output: 207959545

Explanation:

The good arrays are [1, 2, 1, 2, 1] and [2, 1, 2, 1, 2]. Hence, the answer is 2.
 

Constraints:

1 <= n <= 105
1 <= m <= 105
0 <= k <= n - 1
Seen this question in a real interview before?
1/5
Yes
No
Accepted
5,272/16.6K
Acceptance Rate
31.7%
Topics
Math
Combinatorics
icon
Companies
Hint 1
The first position arr[0] has m choices.
Hint 2
For each of the remaining n - 1 indices, 0 < i < n, select k positions from left to right and set arr[i] = arr[i - 1].
Hint 3
For all other indices, set arr[i] != arr[i - 1] with (m - 1) choices for each of the n - 1 - k positions.
Similar Questions
Count Good Numbers
Medium
''')
