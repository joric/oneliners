from lc import *

# https://leetcode.com/problems/separate-the-digits-in-an-array/solutions/4529485/one-line-solution-by-ashishbaipalli369-ibl1/?envType=daily-question&envId=2026-05-11

class Solution:
    def separateDigits(self, n: List[int]) -> List[int]:
        return[*map(int,re.sub('\D','',str(n)))]

class Solution:
    def separateDigits(self, n: List[int]) -> List[int]:
        return[*map(int,''.join(map(str,n)))]

test('''
2553. Separate the Digits in an Array
Easy
Topics
premium lock icon
Companies
Hint
Given an array of positive integers nums, return an array answer that consists of the digits of each integer in nums after separating them in the same order they appear in nums.

To separate the digits of an integer is to get all the digits it has in the same order.

For example, for the integer 10921, the separation of its digits is [1,0,9,2,1].
 

Example 1:

Input: nums = [13,25,83,77]
Output: [1,3,2,5,8,3,7,7]
Explanation: 
- The separation of 13 is [1,3].
- The separation of 25 is [2,5].
- The separation of 83 is [8,3].
- The separation of 77 is [7,7].
answer = [1,3,2,5,8,3,7,7]. Note that answer contains the separations in the same order.
Example 2:

Input: nums = [7,1,3,9]
Output: [7,1,3,9]
Explanation: The separation of each integer in nums is itself.
answer = [7,1,3,9].
 

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 105
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
104,553/129.3K
Acceptance Rate
80.9%
Topics
Mid Level
Array
Simulation
Biweekly Contest 97
icon
Companies
Hint 1
Convert each number into a list and append that list to the answer.
Hint 2
You can convert the integer into a string to do that easily.
Similar Questions
Count Integers With Even Digit Sum
Easy
Alternating Digit Sum
Easy
''')
