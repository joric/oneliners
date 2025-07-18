from lc import *

# https://leetcode.com/problems/minimum-difference-in-sums-after-removal-of-elements/solutions/4878821/python-9-lines-solutions-heapq/?envType=daily-question&envId=2025-07-18

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3
        A, B = sorted([-v for v in nums[:n]]), sorted(nums[-n:]), 
        possible_A, possible_B = [-sum(A)], [sum(B)]
        for i in range(n, 2*n):
            heappush(A, -nums[i])
            possible_A.append(possible_A[-1] + nums[i] + heappop(A))
            heappush(B, nums[-i-1])
            possible_B.append(possible_B[-1] + nums[-i-1] - heappop(B))
        return min(a - b for a, b in zip(possible_A, possible_B[::-1]))

class Solution:
    def minimumDifference(self, t: List[int]) -> int:
        n=len(t)//3;a,b=sorted(map(neg,t[:n])),sorted(t[-n:]);p,q=[-sum(a)],[sum(b)];[(heappush(a,-t[i]),p.append(p[-1]+t[i]+heappop(a)),heappush(b,t[~i]),q.append(q[-1]+t[~i]-heappop(b)))for i in range(n,2*n)];return min(map(sub,p,q[::-1]))

test('''
2163. Minimum Difference in Sums After Removal of Elements
Hard
Topics
premium lock icon
Companies
Hint
You are given a 0-indexed integer array nums consisting of 3 * n elements.

You are allowed to remove any subsequence of elements of size exactly n from nums. The remaining 2 * n elements will be divided into two equal parts:

The first n elements belonging to the first part and their sum is sumfirst.
The next n elements belonging to the second part and their sum is sumsecond.
The difference in sums of the two parts is denoted as sumfirst - sumsecond.

For example, if sumfirst = 3 and sumsecond = 2, their difference is 1.
Similarly, if sumfirst = 2 and sumsecond = 3, their difference is -1.
Return the minimum difference possible between the sums of the two parts after the removal of n elements.

 

Example 1:

Input: nums = [3,1,2]
Output: -1
Explanation: Here, nums has 3 elements, so n = 1. 
Thus we have to remove 1 element from nums and divide the array into two equal parts.
- If we remove nums[0] = 3, the array will be [1,2]. The difference in sums of the two parts will be 1 - 2 = -1.
- If we remove nums[1] = 1, the array will be [3,2]. The difference in sums of the two parts will be 3 - 2 = 1.
- If we remove nums[2] = 2, the array will be [3,1]. The difference in sums of the two parts will be 3 - 1 = 2.
The minimum difference between sums of the two parts is min(-1,1,2) = -1. 
Example 2:

Input: nums = [7,9,5,8,1,3]
Output: 1
Explanation: Here n = 2. So we must remove 2 elements and divide the remaining array into two parts containing two elements each.
If we remove nums[2] = 5 and nums[3] = 8, the resultant array will be [7,9,1,3]. The difference in sums will be (7+9) - (1+3) = 12.
To obtain the minimum difference, we should remove nums[1] = 9 and nums[4] = 1. The resultant array becomes [7,5,8,3]. The difference in sums of the two parts is (7+5) - (8+3) = 1.
It can be shown that it is not possible to obtain a difference smaller than 1.
 

Constraints:

nums.length == 3 * n
1 <= n <= 105
1 <= nums[i] <= 105
Seen this question in a real interview before?
1/5
Yes
No
Accepted
14,420/28.9K
Acceptance Rate
49.9%
Topics
Array
Dynamic Programming
Heap (Priority Queue)
icon
Companies
Hint 1
The lowest possible difference can be obtained when the sum of the first n elements in the resultant array is minimum, and the sum of the next n elements is maximum.
Hint 2
For every index i, think about how you can find the minimum possible sum of n elements with indices lesser or equal to i, if possible.
Hint 3
Similarly, for every index i, try to find the maximum possible sum of n elements with indices greater or equal to i, if possible.
Hint 4
Now for all indices, check if we can consider it as the partitioning index and hence find the answer.
Similar Questions
Product of Array Except Self
Medium
Find Subsequence of Length K With the Largest Sum
Easy
Find Minimum Cost to Remove Array Elements
Medium
''')
