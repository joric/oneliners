from lc import *

# https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/solutions/6526047/beat-100-python-one-line-solution/?envType=daily-question&envId=2025-03-12

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        return max(bisect_left(nums, 0), len(nums)-bisect_right(nums, 0))

# https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/solutions/3016922/python3-one-line/?envType=daily-question&envId=2025-03-12

class Solution:
    def maximumCount(self, a: List[int]) -> int:
        return max(sum(x>0 for x in a),sum(x<0 for x in a))

class Solution:
    def maximumCount(self, a: List[int]) -> int:
        return max(sum(map(f,a,repeat(0)))for f in(lt,gt))

class Solution:
    def maximumCount(self, a: List[int]) -> int:
        return max(sum(f(x,0)for x in a)for f in(lt,gt))

test('''
2529. Maximum Count of Positive Integer and Negative Integer
Easy
Topics
Companies
Hint
Given an array nums sorted in non-decreasing order, return the maximum between the number of positive integers and the number of negative integers.

In other words, if the number of positive integers in nums is pos and the number of negative integers is neg, then return the maximum of pos and neg.
Note that 0 is neither positive nor negative.

 

Example 1:

Input: nums = [-2,-1,-1,1,2,3]
Output: 3
Explanation: There are 3 positive integers and 3 negative integers. The maximum count among them is 3.
Example 2:

Input: nums = [-3,-2,-1,0,0,1,2]
Output: 3
Explanation: There are 2 positive integers and 3 negative integers. The maximum count among them is 3.
Example 3:

Input: nums = [5,20,66,1314]
Output: 4
Explanation: There are 4 positive integers and 0 negative integers. The maximum count among them is 4.
 

Constraints:

1 <= nums.length <= 2000
-2000 <= nums[i] <= 2000
nums is sorted in a non-decreasing order.
 

Follow up: Can you solve the problem in O(log(n)) time complexity?

Seen this question in a real interview before?
1/5
Yes
No
Accepted
155.6K
Submissions
217.9K
Acceptance Rate
71.4%
Topics
Array
Binary Search
Counting
Companies
Hint 1
Count how many positive integers and negative integers are in the array.
Hint 2
Since the array is sorted, can we use the binary search?
Similar Questions
Binary Search
Easy
Count Negative Numbers in a Sorted Matrix
Easy
''')
