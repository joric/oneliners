from lc import *

# https://leetcode.com/problems/replace-non-coprime-numbers-in-array/description/?envType=daily-question&envId=2025-09-16

class Solution():
    def replaceNonCoprimes(self, a: List[int]) -> List[int]:
        s = []
        for x in a:
            s.append(x)
            while len(s) > 1 and gcd(s[-1],s[-2]) > 1:
                s.append(lcm(s.pop(),s.pop()))
        return s

class Solution():
    def replaceNonCoprimes(self, a: List[int]) -> List[int]:
        s=[];[s.append(x)or all(len(s)>1<gcd(*s[-2:])!=s.append(lcm(s.pop(),s.pop()))for _ in a)for x in a];return s

test('''
2197. Replace Non-Coprime Numbers in Array
Hard
Topics
premium lock icon
Companies
Hint
You are given an array of integers nums. Perform the following steps:

Find any two adjacent numbers in nums that are non-coprime.
If no such numbers are found, stop the process.
Otherwise, delete the two numbers and replace them with their LCM (Least Common Multiple).
Repeat this process as long as you keep finding two adjacent non-coprime numbers.
Return the final modified array. It can be shown that replacing adjacent non-coprime numbers in any arbitrary order will lead to the same result.

The test cases are generated such that the values in the final array are less than or equal to 108.

Two values x and y are non-coprime if GCD(x, y) > 1 where GCD(x, y) is the Greatest Common Divisor of x and y.

 

Example 1:

Input: nums = [6,4,3,2,7,6,2]
Output: [12,7,6]
Explanation: 
- (6, 4) are non-coprime with LCM(6, 4) = 12. Now, nums = [12,3,2,7,6,2].
- (12, 3) are non-coprime with LCM(12, 3) = 12. Now, nums = [12,2,7,6,2].
- (12, 2) are non-coprime with LCM(12, 2) = 12. Now, nums = [12,7,6,2].
- (6, 2) are non-coprime with LCM(6, 2) = 6. Now, nums = [12,7,6].
There are no more adjacent non-coprime numbers in nums.
Thus, the final modified array is [12,7,6].
Note that there are other ways to obtain the same resultant array.
Example 2:

Input: nums = [2,2,1,1,3,3,3]
Output: [2,1,1,3]
Explanation: 
- (3, 3) are non-coprime with LCM(3, 3) = 3. Now, nums = [2,2,1,1,3,3].
- (3, 3) are non-coprime with LCM(3, 3) = 3. Now, nums = [2,2,1,1,3].
- (2, 2) are non-coprime with LCM(2, 2) = 2. Now, nums = [2,1,1,3].
There are no more adjacent non-coprime numbers in nums.
Thus, the final modified array is [2,1,1,3].
Note that there are other ways to obtain the same resultant array.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 105
The test cases are generated such that the values in the final array are less than or equal to 108.
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
26,894/57.5K
Acceptance Rate
46.8%
Topics
Array
Math
Stack
Number Theory
Weekly Contest 283
icon
Companies
Hint 1
Notice that the order of merging two numbers into their LCM does not matter so we can greedily merge elements to its left if possible.
Hint 2
If a new value is formed, we should recursively check if it can be merged with the value to its left.
Hint 3
To simulate the merge efficiently, we can maintain a stack that stores processed elements. When we iterate through the array, we only compare with the top of the stack (which is the value to its left).
Similar Questions
Remove All Adjacent Duplicates in String II
Medium
Number of Pairs of Interchangeable Rectangles
Medium
Split the Array to Make Coprime Products
Hard
''')
