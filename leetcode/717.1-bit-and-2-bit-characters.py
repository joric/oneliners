from lc import *

# https://leetcode.com/problems/1-bit-and-2-bit-characters/description/?envType=daily-question&envId=2025-11-18

class Solution:
    def isOneBitCharacter(self, b: List[int]) -> bool:
        return not([*b[::-1],0][1:].index(0)%2)

# https://leetcode.com/problems/1-bit-and-2-bit-characters/solutions/782768/one-line-pythonic-solution-by-jrbt-laa8/?envType=daily-question&envId=2025-11-18

class Solution:
    def isOneBitCharacter(self, b: List[int]) -> bool:
        return not(len(''.join(map(str,b)).split('0')[-2])%2)

# https://leetcode.com/problems/1-bit-and-2-bit-characters/solutions/556711/one-line-python-code-by-akandeha-gmmh/?envType=daily-question&envId=2025-11-18

class Solution:
    def isOneBitCharacter(self, b: List[int]) -> bool:
        return not(b[-2::-1]+[0]).index(0)%2

class Solution:
    def isOneBitCharacter(self, b: List[int]) -> bool:
        return(b[-2::-1]+[0]).index(0)%2<1

test('''
717. 1-bit and 2-bit Characters
Easy
Topics
premium lock icon
Companies
Hint
We have two special characters:

The first character can be represented by one bit 0.
The second character can be represented by two bits (10 or 11).
Given a binary array bits that ends with 0, return true if the last character must be a one-bit character.

 

Example 1:

Input: bits = [1,0,0]
Output: true
Explanation: The only way to decode it is two-bit character and one-bit character.
So the last character is one-bit character.
Example 2:

Input: bits = [1,1,1,0]
Output: false
Explanation: The only way to decode it is two-bit character and two-bit character.
So the last character is not one-bit character.
 

Constraints:

1 <= bits.length <= 1000
bits[i] is either 0 or 1.
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
162,543/358.1K
Acceptance Rate
45.4%
Topics
Array
icon
Companies
Hint 1
Keep track of where the next character starts. At the end, you want to know if you started on the last bit.
Similar Questions
Gray Code
Medium
''')
