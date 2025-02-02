from lc import *

# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/solutions/4394976/count-breakpoints-1-line-solution-beat-92/?envType=daily-question&envId=2025-02-02

class Solution:
    def check(self, nums: List[int]) -> bool:
        return sum(nums[i] > nums[(i + 1) % len(nums)] for i in range(len(nums))) <= 1

class Solution:
    def check(self, n: List[int]) -> bool:
        return sum(x>n[(i+1)%len(n)]for i,x in enumerate(n))<2

class Solution:
    def check(self, a: List[int]) -> bool:
        n=len(a);return sum(a[i]>a[-~i%n]for i in range(n))<2

class Solution:
    def check(self, n: List[int]) -> bool:
        return sum(x>n[-~i%len(n)]for i,x in enumerate(n))<2

# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/solutions/1053508/java-c-python-easy-and-concise/

class Solution:
    def check(self, n: List[int]) -> bool:
        return sum(a>b for a,b in zip(n,n[1:]+n[:1]))<2

class Solution:
    def check(self, n: List[int]) -> bool:
        return sum(map(gt,n,n[1:]+n))<2

test('''
1752. Check if Array Is Sorted and Rotated
Solved
Easy
Topics
Companies
Hint
Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.

There may be duplicates in the original array.

Note: An array A rotated by x positions results in an array B of the same length such that A[i] == B[(i+x) % A.length], where % is the modulo operation.

 

Example 1:

Input: nums = [3,4,5,1,2]
Output: true
Explanation: [1,2,3,4,5] is the original sorted array.
You can rotate the array by x = 3 positions to begin on the the element of value 3: [3,4,5,1,2].
Example 2:

Input: nums = [2,1,3,4]
Output: false
Explanation: There is no sorted array once rotated that can make nums.
Example 3:

Input: nums = [1,2,3]
Output: true
Explanation: [1,2,3] is the original sorted array.
You can rotate the array by x = 0 positions (i.e. no rotation) to make nums.
 

Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100
Seen this question in a real interview before?
1/5
Yes
No
Accepted
395.6K
Submissions
759K
Acceptance Rate
52.1%
Topics
Array
Companies
Hint 1
Brute force and check if it is possible for a sorted array to start from each position.
''')
