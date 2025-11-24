from lc import *

# https://leetcode.com/problems/binary-prefix-divisible-by-5/solutions/7363508/one-line-solution-by-mikposp-tp7a/?envType=daily-question&envId=2025-11-24

class Solution:
    def prefixesDivBy5(self, a: List[int]) -> List[bool]:
        return [*map(not_,accumulate(a,lambda q,v:(q*2+v)%5))]

class Solution:
    def prefixesDivBy5(self, n: List[int]) -> List[bool]:
        n=''.join(str(a)for a in n)
        return [ not(int(n[:i+1],2)%5) for i in range(len(n))]


# https://leetcode.com/problems/binary-prefix-divisible-by-5/solutions/411320/python-3-one-line-9945-by-ye15-0bgx/?envType=daily-question&envId=2025-11-24

class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        return [x == 0 for x in accumulate(A, lambda x, y: (2*x+y)%5)]


# https://leetcode.com/problems/binary-prefix-divisible-by-5/solutions/551755/python-one-liners-explained-by-rmoskalen-369y/?envType=daily-question&envId=2025-11-24

class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        return [x == 0 for x in accumulate(A, lambda x, y: (2*x+y)%5)]

class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        return (lambda n: [ (n:=2*n+i)%5==0 for i in A ])(0)

class Solution:
    def prefixesDivBy5(self, a: List[int]) -> List[bool]:
            return[x%5<1 for x in accumulate(a,lambda x,y:x*2+y)]

class Solution:
    def prefixesDivBy5(self, a: List[int]) -> List[bool]:
        n=0;return[(n:=2*n+i)%5<1 for i in a]

test('''
1018. Binary Prefix Divisible By 5
Solved
Easy
Topics
premium lock icon
Companies
Hint
You are given a binary array nums (0-indexed).

We define xi as the number whose binary representation is the subarray nums[0..i] (from most-significant-bit to least-significant-bit).

For example, if nums = [1,0,1], then x0 = 1, x1 = 2, and x2 = 5.
Return an array of booleans answer where answer[i] is true if xi is divisible by 5.

 

Example 1:

Input: nums = [0,1,1]
Output: [true,false,false]
Explanation: The input numbers in binary are 0, 01, 011; which are 0, 1, and 3 in base-10.
Only the first number is divisible by 5, so answer[0] is true.
Example 2:

Input: nums = [1,1,1]
Output: [false,false,false]
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
70,415/148.5K
Acceptance Rate
47.4%
Topics
Array
Bit Manipulation
Weekly Contest 130
icon
Companies
Hint 1
If X is the first i digits of the array as a binary number, then 2X + A[i] is the first i+1 digits.
Similar Questions
Average Value of Even Numbers That Are Divisible by Three
Easy
Find the Maximum Divisibility Score
Easy
''')
