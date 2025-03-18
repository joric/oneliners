from lc import *

# https://leetcode.com/problems/longest-nice-subarray/solutions/3168576/5-lines-scala-recursion/?envType=daily-question&envId=2025-03-18

class Solution:
    def longestNiceSubarray(self, a: list[int]) -> int:
        return(f:=lambda i,j,m,k:j<len(a)and(k&a[j]and f(i+1,j,m,k^a[i])or f(i,j+1,max(m,j+1-i),k|a[j]))or m)(*[0]*4)


# https://leetcode.com/problems/longest-nice-subarray/solutions/2603282/python3-8-lines-two-pointer-dict-w-explanation-t-s-95-81/?envType=daily-question&envId=2025-03-18

class Solution:
    def longestNiceSubarray(self, a: List[int]) -> int:
        i=k=m=0
        for j in range(len(a)):
            while a[j]&k:
                k ^= a[i]
                i += 1
            k ^= a[j]
            m = max(m, j-i+1)
        return m

class Solution:
    def longestNiceSubarray(self, a: List[int]) -> int:
        i=k=0;return max((all(k&x and(k:=k^a[i],i:=i+1)for _ in a),k:=k^x,j-i+1)[2]for j,x in enumerate(a))

test('''
2401. Longest Nice Subarray
Medium
Topics
Companies
Hint
You are given an array nums consisting of positive integers.

We call a subarray of nums nice if the bitwise AND of every pair of elements that are in different positions in the subarray is equal to 0.

Return the length of the longest nice subarray.

A subarray is a contiguous part of an array.

Note that subarrays of length 1 are always considered nice.

 

Example 1:

Input: nums = [1,3,8,48,10]
Output: 3
Explanation: The longest nice subarray is [3,8,48]. This subarray satisfies the conditions:
- 3 AND 8 = 0.
- 3 AND 48 = 0.
- 8 AND 48 = 0.
It can be proven that no longer nice subarray can be obtained, so we return 3.
Example 2:

Input: nums = [3,1,5,11,13]
Output: 1
Explanation: The length of the longest nice subarray is 1. Any subarray of length 1 can be chosen.


Other examples:

Input: nums = [178830999,19325904,844110858,806734874,280746028,64,256,33554432,882197187,104359873,453049214,820924081,624788281,710612132,839991691]
Output: 4

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
Seen this question in a real interview before?
1/5
Yes
No
Accepted
69.2K
Submissions
118.6K
Acceptance Rate
58.3%
Topics
Array
Bit Manipulation
Sliding Window
Companies
Hint 1
What is the maximum possible length of a nice subarray?
Hint 2
If two numbers have bitwise AND equal to zero, they do not have any common set bit. A number x <= 109 only has 30 bits, hence the length of the longest nice subarray cannot exceed 30.
Similar Questions
Longest Substring Without Repeating Characters
Medium
Bitwise AND of Numbers Range
Medium
Bitwise ORs of Subarrays
Medium
Fruit Into Baskets
Medium
Max Consecutive Ones III
Medium
Get Equal Substrings Within Budget
Medium
Frequency of the Most Frequent Element
Medium
Longest Substring Of All Vowels in Order
Medium
Maximize the Confusion of an Exam
Medium
Maximum Sum of Distinct Subarrays With Length K
Medium
''')
