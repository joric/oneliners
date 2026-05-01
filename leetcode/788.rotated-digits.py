from lc import *

# https://leetcode.com/problems/rotated-digits/solutions/203985/one-line-in-python3-on-though-by-alexcho-7hp7/?envType=daily-question&envId=2026-05-02

class Solution:
    def rotatedDigits(self, n: int) -> int:
        return sum([1 for x in range(n+1)if set('2569')&set(str(x))and not set('347')&set(str(x))])

class Solution:
    def maxRotateFunction(self,n:int)->int:
        return sum({*'2569'}&(s:={*str(x)})>s&{*'347'}for x in range(n+1))

'''kotlin
class Solution {
    fun rotatedDigits(n: Int): Int {
        return(1..n).count{val s =it.toString();s.any{it in "2569"}&&!s.any{it in "743"}}
    }
}

class Solution {
    fun rotatedDigits(n: Int): Int {
        return(1..n).count{"$it".any{it in "2569"}&&"$it".none{it in "347"}}
    }
}
'''

test('''
788. Rotated Digits
Medium
Topics
premium lock icon
Companies
An integer x is a good if after rotating each digit individually by 180 degrees, we get a valid number that is different from x. Each digit must be rotated - we cannot choose to leave it alone.

A number is valid if each digit remains a digit after rotation. For example:

0, 1, and 8 rotate to themselves,
2 and 5 rotate to each other (in this case they are rotated in a different direction, in other words, 2 or 5 gets mirrored),
6 and 9 rotate to each other, and
the rest of the numbers do not rotate to any other number and become invalid.
Given an integer n, return the number of good integers in the range [1, n].

 

Example 1:

Input: n = 10
Output: 4
Explanation: There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.
Example 2:

Input: n = 1
Output: 0
Example 3:

Input: n = 2
Output: 1
 

Constraints:

1 <= n <= 104
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
130,697/229.8K
Acceptance Rate
56.9%
Topics
Senior
Math
Dynamic Programming
Weekly Contest 73
icon
''')
