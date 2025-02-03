from lc import *

# Q1. https://leetcode.com/contest/weekly-contest-392
# https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/

class Solution:
    def longestMonotonicSubarray(self, a: List[int]) -> int:
        n=len(a);return max(j-i+1 for i in range(n)for j in range(i,n)if(c:=a[i:j+1])and len(set(c))==len(c)and(c==sorted(c)or c[::-1]==sorted(c)))

class Solution:
    def longestMonotonicSubarray(self, a: List[int]) -> int:
        i=d=1;return max([max(i:=i*(a[j]<a[j+1])+1,d:=d*(a[j]>a[j+1])+1)for j in range(len(a)-1)]+[1])

# https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/solutions/5137205/one-line-solution/?envType=daily-question&envId=2025-02-03

class Solution:
    def longestMonotonicSubarray(self, a: List[int]) -> int:
        return max([u:=(d:=1)]+[max(u:=u*lt(*q)+1,d:=d*gt(*q)+1)for q in pairwise(a)])

class Solution:
    def longestMonotonicSubarray(self, a: List[int]) -> int:
        u=d=1;return max([1]+[max(u:=u*lt(*q)+1,d:=d*gt(*q)+1)for q in pairwise(a)])

class Solution:
    def longestMonotonicSubarray(self, a: List[int]) -> int:
        return max(max((sum(g)for _,g in groupby(starmap(f,pairwise(a)))),default=0) for f in (lt,gt))+1

class Solution:
    def longestMonotonicSubarray(self, a: List[int]) -> int:
        return 1+max([0]+[sum(g)for f in(lt,gt)for _,g in groupby(map(f,a,a[1:]))])

test('''
3105. Longest Strictly Increasing or Strictly Decreasing Subarray
Easy

2

0

Add to List

Share
You are given an array of integers nums. Return the length of the longest subarray of nums which is either strictly increasing or strictly decreasing.

 

Example 1:

Input: nums = [1,4,3,3,2]

Output: 2

Explanation:

The strictly increasing subarrays of nums are [1], [2], [3], [3], [4], and [1,4].

The strictly decreasing subarrays of nums are [1], [2], [3], [3], [4], [3,2], and [4,3].

Hence, we return 2.

Example 2:

Input: nums = [3,3,3,3]

Output: 1

Explanation:

The strictly increasing subarrays of nums are [3], [3], [3], and [3].

The strictly decreasing subarrays of nums are [3], [3], [3], and [3].

Hence, we return 1.

Example 3:

Input: nums = [3,2,1]

Output: 3

Explanation:

The strictly increasing subarrays of nums are [3], [2], and [1].

The strictly decreasing subarrays of nums are [3], [2], [1], [3,2], [2,1], and [3,2,1].

Hence, we return 3.

More examples:

Input: nums = [1]
Output: 1

Constraints:

1 <= nums.length <= 50
1 <= nums[i] <= 50
Accepted
20,249
Submissions
37,317
''')