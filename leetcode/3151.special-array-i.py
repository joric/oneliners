from lc import *

# https://leetcode.com/problems/special-array-i/solutions/6249305/python-1-line/?envType=daily-question&envId=2025-02-01

class Solution:
    def isArraySpecial(self, n: List[int]) -> bool:
        return all(map((1).__and__,map(abs,starmap(sub,pairwise(n)))))

class Solution:
    def isArraySpecial(self, n: List[int]) -> bool:
        return all(1&abs(a-b)for a,b in pairwise(n))

class Solution:
    def isArraySpecial(self, n: List[int]) -> bool:
        return all(1&(a^b)for a,b in pairwise(n))

class Solution:
    def isArraySpecial(self, n: List[int]) -> bool:
        return all(a+b&1 for a,b in pairwise(n))

test('''
3151. Special Array I
Solved
Easy
Topics
Companies
Hint
An array is considered special if every pair of its adjacent elements contains two numbers with different parity.

You are given an array of integers nums. Return true if nums is a special array, otherwise, return false.

 

Example 1:

Input: nums = [1]

Output: true

Explanation:

There is only one element. So the answer is true.

Example 2:

Input: nums = [2,1,4]

Output: true

Explanation:

There is only two pairs: (2,1) and (1,4), and both of them contain numbers with different parity. So the answer is true.

Example 3:

Input: nums = [4,3,1,6]

Output: false

Explanation:

nums[1] and nums[2] are both odd. So the answer is false.

 

Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100
Seen this question in a real interview before?
1/5
Yes
No
Accepted
69K
Submissions
91.3K
Acceptance Rate
75.6%
Topics
Array
Companies
Hint 1
Try to check the parity of each element and its previous element.
''')
