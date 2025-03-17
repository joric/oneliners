from lc import *

# https://leetcode.com/problems/divide-array-into-equal-pairs/solutions/6544733/one-line-solution/?envType=daily-question&envId=2025-03-17

class Solution:
    def divideArray(self, a: List[int]) -> bool:
        return all(not c%2 for c in Counter(a).values())

class Solution:
    def divideArray(self, a: List[int]) -> bool:
        return all(1>c&1 for c in Counter(a).values())

class Solution:
    def divideArray(self, a: List[int]) -> bool:
        return not reduce(lambda s,x:s^{x},a,set())

class Solution:
    def divideArray(self, a: List[int]) -> bool:
        s=set();[s:=s^{x}for x in a];return not s

# https://leetcode.com/problems/divide-array-into-equal-pairs/solutions/3102577/best-solution-ever-only-using-xor/?envType=daily-question&envId=2025-03-17

class Solution:
    def divideArray(self, a: List[int]) -> bool:
        p=q=0;[(p:=p^x,q:=q^~-x)for x in a];return p==q==0

# https://leetcode.com/problems/divide-array-into-equal-pairs/solutions/2105016/why-xoring-does-not-work/?envType=daily-question&envId=2025-03-17

class Solution:
    def divideArray(self, a: List[int]) -> bool:
        return reduce(xor,map(pow,a,repeat(2)))<1

class Solution:
    def divideArray(self, a: List[int]) -> bool:
        return reduce(xor,(1<<x for x in a))<1

class Solution:
    def divideArray(self, a: List[int]) -> bool:
        s=0;[s:=s^1<<x for x in a];return s<1

test('''
2206. Divide Array Into Equal Pairs
Easy
Topics
Companies
Hint
You are given an integer array nums consisting of 2 * n integers.

You need to divide nums into n pairs such that:

Each element belongs to exactly one pair.
The elements present in a pair are equal.
Return true if nums can be divided into n pairs, otherwise return false.

 

Example 1:

Input: nums = [3,2,3,2,2,2]
Output: true
Explanation: 
There are 6 elements in nums, so they should be divided into 6 / 2 = 3 pairs.
If nums is divided into the pairs (2, 2), (3, 3), and (2, 2), it will satisfy all the conditions.
Example 2:

Input: nums = [1,2,3,4]
Output: false
Explanation: 
There is no way to divide nums into 4 / 2 = 2 pairs such that the pairs satisfy every condition.


Other examples:

Input: nums = [18,19,5,5,18,19,5,6,12,19,13,4,16,11,4,16,10,8,12,8,2,1,8,17,4,18,3,5,16,2,16,12,17,16,7,16,2,17,19,9,1,20,17,17,4,6]
Output: false


Constraints:

nums.length == 2 * n
1 <= n <= 500
1 <= nums[i] <= 500
Seen this question in a real interview before?
1/5
Yes
No
Accepted
135.9K
Submissions
177.5K
Acceptance Rate
76.5%
Topics
Array
Hash Table
Bit Manipulation
Counting
Companies
Hint 1
For any number x in the range [1, 500], count the number of elements in nums whose values are equal to x.
Hint 2
The elements with equal value can be divided completely into pairs if and only if their count is even.
Similar Questions
Sort Array by Increasing Frequency
Easy
Distribute Elements Into Two Arrays I
Easy
Distribute Elements Into Two Arrays II
Hard
''')
