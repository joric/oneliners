from lc import *

# https://leetcode.com/problems/tuple-with-same-product

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        ans = 0
        freq = {}
        for i in range(len(nums)):
            for j in range(i+1, len(nums)): 
                key = nums[i] * nums[j]
                ans += freq.get(key, 0)
                freq[key] = 1 + freq.get(key, 0)
        return 8*ans

# https://leetcode.com/problems/tuple-with-same-product/solutions/3878713/python-one-line/?envType=daily-question&envId=2025-02-06

class Solution:
    def tupleSameProduct(self, A):
        return sum(4*v*(v-1) for v in Counter(A[i]*A[j] for i in range(len(A)) for j in range(i)).values() if v>1)

# https://leetcode.com/problems/tuple-with-same-product/solutions/1334867/one-multi-line-100-speed/?envType=daily-question&envId=2025-02-06

class Solution:
    def tupleSameProduct(self, nums) -> int:
        return sum(4*n*(n-1)for n in Counter(a*b for a,b in combinations(nums,2)).values()if n>1)

class Solution:
    def tupleSameProduct(self, a) -> int:
        return sum(8*comb(n,2)for n in Counter(starmap(mul,combinations(a,2))).values()if n>1)

class Solution:
    def tupleSameProduct(self, a) -> int:
        return sum(4*n*~-n*(n>1)for n in Counter(starmap(mul,combinations(a,2))).values())

class Solution:
    def tupleSameProduct(self, a) -> int:
        return sum(8*comb(n,2)for n in Counter(starmap(mul,combinations(a,2))).values())

class Solution:
    def tupleSameProduct(self, a) -> int:
        return sum(n*~-n*4for n in Counter(starmap(mul,combinations(a,2))).values())

test('''
1726. Tuple with Same Product
Solved
Medium
Topics
Companies
Hint
Given an array nums of distinct positive integers, return the number of tuples (a, b, c, d) such that a * b = c * d where a, b, c, and d are elements of nums, and a != b != c != d.

 

Example 1:

Input: nums = [2,3,4,6]
Output: 8
Explanation: There are 8 valid tuples:
(2,6,3,4) , (2,6,4,3) , (6,2,3,4) , (6,2,4,3)
(3,4,2,6) , (4,3,2,6) , (3,4,6,2) , (4,3,6,2)
Example 2:

Input: nums = [1,2,4,5,10]
Output: 16
Explanation: There are 16 valid tuples:
(1,10,2,5) , (1,10,5,2) , (10,1,2,5) , (10,1,5,2)
(2,5,1,10) , (2,5,10,1) , (5,2,1,10) , (5,2,10,1)
(2,10,4,5) , (2,10,5,4) , (10,2,4,5) , (10,2,5,4)
(4,5,2,10) , (4,5,10,2) , (5,4,2,10) , (5,4,10,2)
 

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 104
All elements in nums are distinct.
Seen this question in a real interview before?
1/5
Yes
No
Accepted
32K
Submissions
51.6K
Acceptance Rate
62.0%
Topics
Array
Hash Table
Counting
Companies
Hint 1
Note that all of the integers are distinct. This means that each time a product is formed it must be formed by two unique integers.
Hint 2
Count the frequency of each product of 2 distinct numbers. Then calculate the permutations formed.
''')
