from lc import *

# https://leetcode.com/problems/minimum-moves-to-make-array-complementary/solutions/952989/python-easy-to-understand-binary-search-yzuru/?envType=daily-question&envId=2026-05-13

class Solution:
    def minMoves(self, a: List[int], k: int) -> int:
        b=bisect_left
        n=len(a)//2
        p=[*zip(a[:n],a[:n-1:-1])]
        l,h=map(sorted,(map(min,p),map(max,p)))
        c=Counter(map(sum,p))
        return min(n-c[t]+n-b(l,t)+b(h,t-k)for t in range(2,2*k+1))

class Solution:
    def minMoves(self, a: List[int], k: int) -> int:
        b,n=bisect_left,len(a)//2;p=[*zip(a[:n],a[:n-1:-1])];l,h=map(sorted,(map(min,p),map(max,p)));c=Counter(map(sum,p));return min(n-c[t]+n-b(l,t)+b(h,t-k)for t in range(2,2*k+1))

class Solution:
    def minMoves(self, a: List[int], k: int) -> int:
        b=bisect_right;p=[*map(sorted,zip(a,a[::-1]))];l,h=map(sorted,zip(*p));c=Counter(map(sum,p));return min(2*len(a)-c[t]-b(l,t-1)+b(h,t+~k)for t in range(k-~k))//2

test('''
1674. Minimum Moves to Make Array Complementary
Medium
Topics
premium lock icon
Companies
Hint
You are given an integer array nums of even length n and an integer limit. In one move, you can replace any integer from nums with another integer between 1 and limit, inclusive.

The array nums is complementary if for all indices i (0-indexed), nums[i] + nums[n - 1 - i] equals the same number. For example, the array [1,2,3,4] is complementary because for all indices i, nums[i] + nums[n - 1 - i] = 5.

Return the minimum number of moves required to make nums complementary.

 

Example 1:

Input: nums = [1,2,4,3], limit = 4
Output: 1
Explanation: In 1 move, you can change nums to [1,2,2,3] (underlined elements are changed).
nums[0] + nums[3] = 1 + 3 = 4.
nums[1] + nums[2] = 2 + 2 = 4.
nums[2] + nums[1] = 2 + 2 = 4.
nums[3] + nums[0] = 3 + 1 = 4.
Therefore, nums[i] + nums[n-1-i] = 4 for every i, so nums is complementary.
Example 2:

Input: nums = [1,2,2,1], limit = 2
Output: 2
Explanation: In 2 moves, you can change nums to [2,2,2,2]. You cannot change any number to 3 since 3 > limit.
Example 3:

Input: nums = [1,2,1,2], limit = 2
Output: 0
Explanation: nums is already complementary.
 

Constraints:

n == nums.length
2 <= n <= 105
1 <= nums[i] <= limit <= 105
n is even.
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
13,264/30.4K
Acceptance Rate
43.6%
Topics
Senior Staff
Array
Hash Table
Prefix Sum
Weekly Contest 217
icon
Companies
Hint 1
Given a target sum x, each pair of nums[i] and nums[n-1-i] would either need 0, 1, or 2 modifications.
Hint 2
Can you find the optimal target sum x value such that the sum of modifications is minimized?
Hint 3
Create a difference array to efficiently sum all the modifications.
Similar Questions
Zero Array Transformation II
Medium
Zero Array Transformation III
Medium
''')
