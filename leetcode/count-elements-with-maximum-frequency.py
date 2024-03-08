from lc import *

# https://leetcode.com/problems/count-elements-with-maximum-frequency/

class Solution:
    def maxFrequencyElements(self, n: List[int]) -> int:
        c=Counter(n);m=max(c.values());return sum(1 for x in n if c[x]==m)

# https://leetcode.com/problems/count-elements-with-maximum-frequency/discuss/4562058/one-line-easy-python/2211162

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        return prod(max(Counter(Counter(nums).values()).items()))

class Solution:
    def maxFrequencyElements(self, n: List[int]) -> int:
        c=Counter;return prod(max(c(c(n).values()).items()))

# https://leetcode.com/problems/count-elements-with-maximum-frequency/discuss/4840186/3-Line-Python-Solution-using-Built-In-Functions

class Solution:
    def maxFrequencyElements(self, n: List[int]) -> int:
        return(m:=max(v:=[*Counter(n).values()]))*v.count(m)

test('''
3005. Count Elements With Maximum Frequency
Easy

15

1

Add to List

Share
You are given an array nums consisting of positive integers.

Return the total frequencies of elements in nums such that those elements all have the maximum frequency.

The frequency of an element is the number of occurrences of that element in the array.

 

Example 1:

Input: nums = [1,2,2,3,1,4]
Output: 4
Explanation: The elements 1 and 2 have a frequency of 2 which is the maximum frequency in the array.
So the number of elements in the array with maximum frequency is 4.
Example 2:

Input: nums = [1,2,3,4,5]
Output: 5
Explanation: All elements of the array have a frequency of 1 which is the maximum.
So the number of elements in the array with maximum frequency is 5.
 

Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100
Accepted
17,615
Submissions
24,649
''')


