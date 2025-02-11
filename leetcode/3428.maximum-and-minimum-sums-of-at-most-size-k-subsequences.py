from lc import *

# https://leetcode.com/problems/maximum-and-minimum-sums-of-at-most-size-k-subsequences/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days

class Solution:
    def minMaxSums(self, nums: List[int], k: int) -> int:
        nums.sort()
        total_sums = 0
        quantity = 1
        for i in range(len(nums)):
            total_sums += quantity * (nums[i] + nums[-i - 1])
            quantity = 2 * quantity - comb(i, k - 1)
        return total_sums % (10 ** 9 + 7)

class Solution:
    def minMaxSums(self, a: List[int], k: int) -> int:
        s,c,a=0,1,sorted(a)
        for i in range(len(a)):
            s += c * (a[i]+a[-i-1])
            c = 2 * c - comb(i,k-1)
        return s % (10 ** 9 + 7)

class Solution:
    def minMaxSums(self, a: List[int], k: int) -> int:
        a.sort();s,c=0,1;return sum(c*(a[i]+a[~i])+0*(c:=2*c-comb(i,k-1))for i in range(len(a)))%(10**9+7)

class Solution:
    def minMaxSums(self, a: List[int], k: int) -> int:
        c=1;return sum(c*(x+a[~i])+0*(c:=2*c-comb(i,k-1))for i,x in enumerate(sorted(a)))%(10**9+7)

test('''
3428. Maximum and Minimum Sums of at Most Size K Subsequences
Medium
Topics
Companies
Hint
You are given an integer array nums and a positive integer k. Return the sum of the maximum and minimum elements of all 
subsequences
 of nums with at most k elements.

Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:

Input: nums = [1,2,3], k = 2

Output: 24

Explanation:

The subsequences of nums with at most 2 elements are:

Subsequence Minimum Maximum Sum
[1] 1   1   2
[2] 2   2   4
[3] 3   3   6
[1, 2]  1   2   3
[1, 3]  1   3   4
[2, 3]  2   3   5
Final Total         24
The output would be 24.

Example 2:

Input: nums = [5,0,6], k = 1

Output: 22

Explanation:

For subsequences with exactly 1 element, the minimum and maximum values are the element itself. Therefore, the total is 5 + 5 + 0 + 0 + 6 + 6 = 22.

Example 3:

Input: nums = [1,1,1], k = 2

Output: 12

Explanation:

The subsequences [1, 1] and [1] each appear 3 times. For all of them, the minimum and maximum are both 1. Thus, the total is 12.

 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 109
1 <= k <= min(70, nums.length)
Seen this question in a real interview before?
1/5
Yes
No
Accepted
9.7K
Submissions
47.3K
Acceptance Rate
20.4%
Topics
Array
Math
Dynamic Programming
Sorting
Combinatorics
Companies
Hint 1
Sort the array.
''')
