from lc import *

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0): return False
        y = 0        
        while x > y:
            y = y * 10 + x % 10
            x //= 10
        return x == y or x == y//10

class Solution:
    def isPalindrome(self, x):
        return 0 if x<0 else(f:=lambda n,p=0:p if n==0 else f(n//10,p*10+n%10))(x)==x

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return(s:=str(x))[::-1]==s

test('''
9. Palindrome Number
Easy

9580

2505

Add to List

Share
Given an integer x, return true if x is a palindrome, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
 

Follow up: Could you solve it without converting the integer to a string?
Accepted
3,188,953
Submissions
5,936,050
Seen this question in a real interview before?

Yes

No
Palindrome Linked List
Easy
Find Palindrome With Fixed Length
Medium
Strictly Palindromic Number
Medium
Beware of overflow when you reverse the integer.
''')

