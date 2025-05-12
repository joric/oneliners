from lc import *

# https://leetcode.com/problems/finding-3-digit-even-numbers/solutions/6730564/one-line-solution/?envType=daily-question&envId=2025-05-12

class Solution:
    def findEvenNumbers(self, a: List[int]) -> List[int]:
        return sorted({100*v+10*u+w for v,u,w in permutations(a,3) if v>0==w&1})

class Solution:
    def findEvenNumbers(self, a: List[int]) -> List[int]:
        return sorted(100*v+10*u+w for v,u,w in {*permutations(a,3)} if v>0==w&1)

class Solution:
    def findEvenNumbers(self, a: List[int]) -> List[int]:
        z=Counter(a);return [v for v in range(100,1000,2) if Counter(map(int,str(v)))<=z]

class Solution:
    def findEvenNumbers(self, a: List[int]) -> List[int]:
        c=Counter;z=c(a);return[v for v in range(100,1000,2)if c(map(int,str(v)))<=z]

class Solution:
    def findEvenNumbers(self, a: List[int]) -> List[int]:
        return sorted({100*v+10*u+w for v,u,w in permutations(a,3)if v>0==w&1})

test('''
2094. Finding 3-Digit Even Numbers
Easy
Topics
Companies
Hint
You are given an integer array digits, where each element is a digit. The array may contain duplicates.

You need to find all the unique integers that follow the given requirements:

The integer consists of the concatenation of three elements from digits in any arbitrary order.
The integer does not have leading zeros.
The integer is even.
For example, if the given digits were [1, 2, 3], integers 132 and 312 follow the requirements.

Return a sorted array of the unique integers.

 

Example 1:

Input: digits = [2,1,3,0]
Output: [102,120,130,132,210,230,302,310,312,320]
Explanation: All the possible integers that follow the requirements are in the output array. 
Notice that there are no odd integers or integers with leading zeros.
Example 2:

Input: digits = [2,2,8,8,2]
Output: [222,228,282,288,822,828,882]
Explanation: The same digit can be used as many times as it appears in digits. 
In this example, the digit 8 is used twice each time in 288, 828, and 882. 
Example 3:

Input: digits = [3,7,5]
Output: []
Explanation: No even integers can be formed using the given digits.
 

Constraints:

3 <= digits.length <= 100
0 <= digits[i] <= 9
Seen this question in a real interview before?
1/5
Yes
No
Accepted
44.9K
Submissions
69.5K
Acceptance Rate
64.6%
Topics
Array
Hash Table
Sorting
Enumeration
Companies
Hint 1
The range of possible answers includes all even numbers between 100 and 999 inclusive. Could you check each possible answer to see if it could be formed from the digits in the array?
Similar Questions
Find Numbers with Even Number of Digits
Easy
''')
