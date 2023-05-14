from lc import *

# https://leetcode.com/problems/maximize-score-after-n-operations/discuss/1118747/Python-Short-dp-on-subsets-explained.

class Solution:
    def maxScore(self, a: List[int]) -> int:
        n=len(a);return(f:=cache(lambda m,k:max([k*gcd(a[i],a[j])+f(m^1<<i^1<<j,k+1) for i,j in combinations(range(n),2) if (m&1<<i)*(m&1<<j)]+[0])))((1<<n)-1,1)

# https://leetcode.com/problems/maximize-score-after-n-operations/discuss/3521613/Python-or-(NO-BIT-MANIPULATION)-DFS-or-Beats-90-or-11-Lines

class Solution:
    def maxScore(self, a: List[int]) -> int:
        return(f:=cache(lambda a,k:max([k*gcd(a[i],a[j])+f(a[:i]+a[i+1:j]+a[j+1:],k+1)for i,j in combinations(range(len(a)),2)]+[0])))(tuple(a),1)

test('''
1799. Maximize Score After N Operations
Hard

1098

82

Add to List

Share
You are given nums, an array of positive integers of size 2 * n. You must perform n operations on this array.

In the ith operation (1-indexed), you will:

Choose two elements, x and y.
Receive a score of i * gcd(x, y).
Remove x and y from nums.
Return the maximum score you can receive after performing n operations.

The function gcd(x, y) is the greatest common divisor of x and y.

 

Example 1:

Input: nums = [1,2]
Output: 1
Explanation: The optimal choice of operations is:
(1 * gcd(1, 2)) = 1
Example 2:

Input: nums = [3,4,6,8]
Output: 11
Explanation: The optimal choice of operations is:
(1 * gcd(3, 6)) + (2 * gcd(4, 8)) = 3 + 8 = 11
Example 3:

Input: nums = [1,2,3,4,5,6]
Output: 14
Explanation: The optimal choice of operations is:
(1 * gcd(1, 5)) + (2 * gcd(2, 4)) + (3 * gcd(3, 6)) = 1 + 4 + 9 = 14
 

Constraints:

1 <= n <= 7
nums.length == 2 * n
1 <= nums[i] <= 10^6
Accepted
34,169
Submissions
62,785
Seen this question in a real interview before?

Yes

No
Find every way to split the array until n groups of 2. Brute force recursion is acceptable.
Calculate the gcd of every pair and greedily multiply the largest gcds
''')


