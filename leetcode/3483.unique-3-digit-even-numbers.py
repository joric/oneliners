from lc import *

# https://leetcode.com/problems/unique-3-digit-even-numbers/solutions/8507372/one-line-solution-by-mikposp-vc8f/?envType=daily-question&envId=2026-09-11

class Solution:
    def totalNumbers(self, a: List[int]) -> int:
        return sum(map(Counter(str(a)).__ge__,map(Counter,map(str,range(100,999,2)))))

class Solution:
    def totalNumbers(self, a: List[int]) -> int:
        z=Counter(str(a));return sum(z>=Counter(str(v))for v in range(100,999,2))

class Solution:
    def totalNumbers(self, a: List[int]) -> int:
        return len({p for p in permutations(a,3)if p[0]>0==p[2]&1})

# POTD 2026-09-11

class Solution:
    def totalNumbers(self, a: List[int]) -> int:
        return len({p for p in permutations(a,3)if~p[2]%2*p[0]})

test('''
3483. Unique 3-Digit Even Numbers
Easy
Topics
premium lock icon
Companies
Hint
You are given an array of digits called digits. Your task is to determine the number of distinct three-digit even numbers that can be formed using these digits.

Note: Each copy of a digit can only be used once per number, and there may not be leading zeros.

 

Example 1:

Input: digits = [1,2,3,4]

Output: 12

Explanation: The 12 distinct 3-digit even numbers that can be formed are 124, 132, 134, 142, 214, 234, 312, 314, 324, 342, 412, and 432. Note that 222 cannot be formed because there is only 1 copy of the digit 2.

Example 2:

Input: digits = [0,2,2]

Output: 2

Explanation: The only 3-digit even numbers that can be formed are 202 and 220. Note that the digit 2 can be used twice because it appears twice in the array.

Example 3:

Input: digits = [6,6,6]

Output: 1

Explanation: Only 666 can be formed.

Example 4:

Input: digits = [1,3,5]

Output: 0

Explanation: No even 3-digit numbers can be formed.

 

Constraints:

3 <= digits.length <= 10
0 <= digits[i] <= 9
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
51,283/73.6K
Acceptance Rate
69.7%
Topics
Mid Level
Array
Hash Table
Recursion
Enumeration
Biweekly Contest 152
icon
Companies
Hint 1
Use brute force to try all possibilities
Similar Questions
Finding 3-Digit Even Numbers
Easy
''')
