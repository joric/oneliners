from lc import *

# https://leetcode.com/problems/k-radius-subarray-averages/discuss/2818000/One-liner-in-Python

class Solution:
    def getAverages(self, n: List[int], k: int) -> List[int]:
        return [-1]*k+[r//(2*k+1) for r in accumulate(zip(n,n[2*k+1:]),lambda a,x:a-x[0]+x[1],initial=sum(n[:2*k+1]))]+[-1]*k if len(n)>=2*k+1 else[-1 for x in n]

# https://leetcode.com/problems/k-radius-subarray-averages/discuss/1599853/Python3-prefix-sum

class Solution:
    def getAverages(self, n: List[int], k: int) -> List[int]:
        p = [0,*accumulate(n)]
        r = [-1]*len(n)
        for i, x in enumerate(n):
            if k <= i < len(n)-k:
                r[i] = (p[i+k+1]-p[i-k])//(2*k+1)
        return r

class Solution:
    def getAverages(self, n: List[int], k: int) -> List[int]:
        p=[0,*accumulate(n)];return[(p[i+k+1]-p[i-k])//(2*k+1) if k<=i<len(n)-k else -1 for i,x in enumerate(n)]

class Solution:
    def getAverages(self, n: List[int], k: int) -> List[int]:
        p=[0,*accumulate(n)];return[(k<=i<len(n)-k and(p[i+k+1]-p[i-k])//(2*k+1)+1)-1for i,x in enumerate(n)]

class Solution:
    def getAverages(self, n: List[int], k: int) -> List[int]:
        t=len(n);p=[0,*accumulate(n)];return[(k<=i<t-k and(p[i+k+1]-p[i-k])//(2*k+1)+1)-1for i in range(t)]

test('''
2090. K Radius Subarray Averages
Medium

541

28

Add to List

Share
You are given a 0-indexed array nums of n integers, and an integer k.

The k-radius average for a subarray of nums centered at some index i with the radius k is the average of all elements in nums between the indices i - k and i + k (inclusive). If there are less than k elements before or after the index i, then the k-radius average is -1.

Build and return an array avgs of length n where avgs[i] is the k-radius average for the subarray centered at index i.

The average of x elements is the sum of the x elements divided by x, using integer division. The integer division truncates toward zero, which means losing its fractional part.

For example, the average of four elements 2, 3, 1, and 5 is (2 + 3 + 1 + 5) / 4 = 11 / 4 = 2.75, which truncates to 2.
 

Example 1:


Input: nums = [7,4,3,9,1,8,5,2,6], k = 3
Output: [-1,-1,-1,5,4,4,-1,-1,-1]
Explanation:
- avg[0], avg[1], and avg[2] are -1 because there are less than k elements before each index.
- The sum of the subarray centered at index 3 with radius 3 is: 7 + 4 + 3 + 9 + 1 + 8 + 5 = 37.
  Using integer division, avg[3] = 37 / 7 = 5.
- For the subarray centered at index 4, avg[4] = (4 + 3 + 9 + 1 + 8 + 5 + 2) / 7 = 4.
- For the subarray centered at index 5, avg[5] = (3 + 9 + 1 + 8 + 5 + 2 + 6) / 7 = 4.
- avg[6], avg[7], and avg[8] are -1 because there are less than k elements after each index.
Example 2:

Input: nums = [100000], k = 0
Output: [100000]
Explanation:
- The sum of the subarray centered at index 0 with radius 0 is: 100000.
  avg[0] = 100000 / 1 = 100000.
Example 3:

Input: nums = [8], k = 100000
Output: [-1]
Explanation: 
- avg[0] is -1 because there are less than k elements before and after index 0.
 

Constraints:

n == nums.length
1 <= n <= 10^5
0 <= nums[i], k <= 10^5
Accepted
25,787
Submissions
60,644
Seen this question in a real interview before?

Yes

No
To calculate the average of a subarray, you need the sum and the K. K is already given. How could you quickly calculate the sum of a subarray?
Use the Prefix Sums method to calculate the subarray sums.
It is possible that the sum of all the elements does not fit in a 32-bit integer type. Be sure to use a 64-bit integer type for the prefix sum array.
''')
