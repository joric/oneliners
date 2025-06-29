from lc import *

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        s = sorted(nums)
        l, r, t = 0, len(s) - 1,0
        while l <= r:
            if s[l]+s[r]>target:
                r -= 1
            else:
                t += pow(2,r-l)
                l += 1
        return t%(10**9+7)

# https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/discuss/3266145/Python-Two-Liner-O(N-log-N)

class Solution:
    def numSubseq(self, a: List[int], t: int) -> int:
        a.sort();return sum(2**(j-i-1)for i,x in enumerate(a)for j in[bisect_right(a,t-x)]if i<j)%(10**9+7)

class Solution:
    def numSubseq(self, a: List[int], t: int) -> int:
        a.sort();return sum(1<<(j-i-1)for i,x in enumerate(a)if(i<(j:=bisect_right(a,t-x))))%(10**9+7)

class Solution:
    def numSubseq(self, a: List[int], t: int) -> int:
        a.sort();return sum(1<<~-j for i,x in enumerate(a)if(j:=bisect_right(a,t-x)-i)>0)%(10**9+7)

class Solution:
    def numSubseq(self, a: List[int], t: int) -> int:
        a.sort();return sum(1<<p for i,x in enumerate(a)if(p:=bisect_right(a,t-x)+~i)>=0)%(10**9+7)

# https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/solutions/6897201/1-line-by-joric-p2o1/

class Solution:
    def numSubseq(self, a: List[int], t: int) -> int:
        a.sort();return sum(1<<~i+bisect_right(a,t-x)for i,x in enumerate(a)if t-x>=x)%(10**9+7)

test('''
1498. Number of Subsequences That Satisfy the Given Sum Condition
Medium

2459

215

Add to List

Share
You are given an array of integers nums and an integer target.

Return the number of non-empty subsequences of nums such that the sum of the minimum and maximum element on it is less or equal to target. Since the answer may be too large, return it modulo 109 + 7.

 

Example 1:

Input: nums = [3,5,6,7], target = 9
Output: 4
Explanation: There are 4 subsequences that satisfy the condition.
[3] -> Min value + max value <= target (3 + 3 <= 9)
[3,5] -> (3 + 5 <= 9)
[3,5,6] -> (3 + 6 <= 9)
[3,6] -> (3 + 6 <= 9)
Example 2:

Input: nums = [3,3,6,8], target = 10
Output: 6
Explanation: There are 6 subsequences that satisfy the condition. (nums can have repeated numbers).
[3] , [3] , [3,3], [3,6] , [3,6] , [3,3,6]
Example 3:

Input: nums = [2,3,3,4,6,7], target = 12
Output: 61
Explanation: There are 63 non-empty subsequences, two of them do not satisfy the condition ([6,7], [7]).
Number of valid subsequences (63 - 2 = 61).
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 106
1 <= target <= 106
Accepted
57,146
Submissions
140,134
Seen this question in a real interview before?

Yes

No
Sort the array nums.
Use two pointers approach: Given an index i (choose it as the minimum in a subsequence) find the maximum j where j ≥ i and nums[i] +nums[j] ≤ target.
Count the number of subsequences.
''')

