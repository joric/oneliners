from lc import *

# https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/solutions/4104468/one-line-solution/?envType=daily-question&envId=2025-06-14

class Solution:
    def minMaxDifference(self, a: int) -> int:
        return int(s.replace(s[i.start()],'9')if(i:=re.search(r'[0-8]',(s:=str(a))))else s)-int(s.replace(s[0],'0'))

# https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/solutions/3201944/python3-one-line/?envType=daily-question&envId=2025-06-14

class Solution:
    def minMaxDifference(self, num: int) -> int:
        a=str(num)
        amax=max(int(''.join(ch if ch!=d else '9' for ch in a)) for d in a)
        amin=min(int(''.join(ch if ch!=d else '0' for ch in a)) for d in a)
        return amax-amin

class Solution:
    def minMaxDifference(self, a: int) -> int:
        f=lambda t,s=str(a):[int(''.join((t,c)[c!=d]for c in s))for d in s];return max(f('9'))-min(f('0'))

class Solution:
    def minMaxDifference(self, a: int) -> int:
        f=lambda t,s=str(a):[int(s.translate({ord(d):ord(t)})) for d in s];return max(f('9'))-min(f('0'))

class Solution:
    def minMaxDifference(self, a: int) -> int:
        f=lambda t,s=str(a):[int(s.replace(d,t))for d in s];return max(f('9'))-min(f('0'))

class Solution:
    def minMaxDifference(self, a: int) -> int:
        f=lambda t,s=str(a):[int(re.sub(d,t,s))for d in s];return max(f('9'))-min(f('0'))

test('''
2566. Maximum Difference by Remapping a Digit
Easy
Topics
premium lock icon
Companies
Hint
You are given an integer num. You know that Bob will sneakily remap one of the 10 possible digits (0 to 9) to another digit.

Return the difference between the maximum and minimum values Bob can make by remapping exactly one digit in num.

Notes:

When Bob remaps a digit d1 to another digit d2, Bob replaces all occurrences of d1 in num with d2.
Bob can remap a digit to itself, in which case num does not change.
Bob can remap different digits for obtaining minimum and maximum values respectively.
The resulting number after remapping can contain leading zeroes.
 

Example 1:

Input: num = 11891
Output: 99009
Explanation: 
To achieve the maximum value, Bob can remap the digit 1 to the digit 9 to yield 99899.
To achieve the minimum value, Bob can remap the digit 1 to the digit 0, yielding 890.
The difference between these two numbers is 99009.
Example 2:

Input: num = 90
Output: 99
Explanation:
The maximum value that can be returned by the function is 99 (if 0 is replaced by 9) and the minimum value that can be returned by the function is 0 (if 9 is replaced by 0).
Thus, we return 99.
 

Constraints:

1 <= num <= 108
Seen this question in a real interview before?
1/5
Yes
No
Accepted
29,690/48.7K
Acceptance Rate
60.9%
Topics
Math
Greedy
icon
Companies
Hint 1
Try to remap the first non-nine digit to 9 to obtain the maximum number.
Hint 2
Try to remap the first non-zero digit to 0 to obtain the minimum number.
''')
