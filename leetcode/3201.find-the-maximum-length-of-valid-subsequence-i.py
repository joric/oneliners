from lc import *

# https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-i/solutions/5389361/java-c-python-dp/?envType=daily-question&envId=2025-07-16

class Solution:
    def maximumLength(self, a: List[int]) -> int:
        a=[x&1 for x in a];return max(a.count(0),a.count(1),len([*groupby(a)]))

class Solution:
    def maximumLength(self, a: List[int]) -> int:
        return max(t:=sum(a:=[x&1 for x in a]),len(a)-t,1+sum(map(ne,a,a[1:])))

class Solution:
    def maximumLength(self, a: List[int]) -> int:
        return max(t:=sum(a:=[x&1 for x in a]),len(a)-t,len([*groupby(a)]))

class Solution:
    def maximumLength(self, a: List[int]) -> int:
        return max(sum(a:=[x&1 for x in a]),a.count(1),len([*groupby(a)]))

test('''
3201. Find the Maximum Length of Valid Subsequence I
Solved
Medium
Topics
premium lock icon
Companies
Hint
You are given an integer array nums.
A subsequence sub of nums with length x is called valid if it satisfies:

(sub[0] + sub[1]) % 2 == (sub[1] + sub[2]) % 2 == ... == (sub[x - 2] + sub[x - 1]) % 2.
Return the length of the longest valid subsequence of nums.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: nums = [1,2,3,4]

Output: 4

Explanation:

The longest valid subsequence is [1, 2, 3, 4].

Example 2:

Input: nums = [1,2,1,1,2,1,2]

Output: 6

Explanation:

The longest valid subsequence is [1, 2, 1, 2, 1, 2].

Example 3:

Input: nums = [1,3]

Output: 2

Explanation:

The longest valid subsequence is [1, 3].

 

Constraints:

2 <= nums.length <= 2 * 105
1 <= nums[i] <= 107
Seen this question in a real interview before?
1/5
Yes
No
Accepted
61,034/126.6K
Acceptance Rate
48.2%
Topics
Array
Dynamic Programming
icon
Companies
Hint 1
The possible sequence either contains all even elements, all odd elements, alternate even odd, or alternate odd even elements.
Hint 2
Considering only the parity of elements, there are only 4 possibilities and we can try all of them.
Hint 3
When selecting an element with any parity, try to select the earliest one.
Similar Questions
Longest Increasing Subsequence
Medium
Length of the Longest Subsequence That Sums to Target
Medium
''')
