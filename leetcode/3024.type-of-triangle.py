from lc import *

# biweekly-contest-123 Q1
# https://leetcode.com/problems/type-of-triangle-ii
# https://leetcode.com/problems/type-of-triangle/?envType=daily-question&envId=2025-05-19

class Solution:
    def triangleType(self, n: List[int]) -> str:
        a,b,c=sorted(n);s=len({*n});return('none',(('scalene','isosceles')[s<3],'equilateral')[s<2])[c<a+b]

class Solution:
    def triangleType(self, n: List[int]) -> str:
        t=[0,4,15,24,31];return'noneequilateralisoscelesscalene'[t[i:=2*max(n)<sum(n)and len({*n})]:t[i+1]]

class Solution:
    def triangleType(self, n: List[int]) -> str:
        a,b,c=sorted(n);return('none',('equilateral','isosceles','scalene')[len({*n})-1])[c<a+b]

class Solution:
    def triangleType(self, n: List[int]) -> str:
        a,b,c=sorted(n);('none','equilateral','isosceles','scalene')[c<a+b and len({*n})]

class Solution:
    def triangleType(self, n: List[int]) -> str:
        return('none','equilateral','isosceles','scalene')[2*max(n)<sum(n)and len({*n})]

class Solution:
    def triangleType(self, n: List[int]) -> str:
        return('none','equilateral','isosceles','scalene')[len({*n})*(sum(n)>2*max(n))]

test('''
3024. Type of Triangle II
Easy

5

0

Add to List

Share
You are given a 0-indexed integer array nums of size 3 which can form the sides of a triangle.

A triangle is called equilateral if it has all sides of equal length.
A triangle is called isosceles if it has exactly two sides of equal length.
A triangle is called scalene if all its sides are of different lengths.
Return a string representing the type of triangle that can be formed or "none" if it cannot form a triangle.

 

Example 1:

Input: nums = [3,3,3]
Output: "equilateral"
Explanation: Since all the sides are of equal length, therefore, it will form an equilateral triangle.
Example 2:

Input: nums = [3,4,5]
Output: "scalene"
Explanation: 
nums[0] + nums[1] = 3 + 4 = 7, which is greater than nums[2] = 5.
nums[0] + nums[2] = 3 + 5 = 8, which is greater than nums[1] = 4.
nums[1] + nums[2] = 4 + 5 = 9, which is greater than nums[0] = 3. 
Since the sum of the two sides is greater than the third side for all three cases, therefore, it can form a triangle.
As all the sides are of different lengths, it will form a scalene triangle.
 

Example 3:

Input: nums = [9,4,9]
Output: "isosceles"

Example 4:
Input: nums = [8,4,2]
Output: "none"

Constraints:

nums.length == 3
1 <= nums[i] <= 100
Accepted
20,070
Submissions
53,037
''')