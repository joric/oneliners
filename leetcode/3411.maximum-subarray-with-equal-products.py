from lc import *

# https://leetcode.com/problems/maximum-subarray-with-equal-products/solutions/8619381/two-simple-lines-of-code-by-mikposp-15yt/?envType=daily-question&envId=2026-11-24

class Solution:
    def maxLength(self, a: List[int]) -> int:
        return max(j-i for i,j in combinations(range(len(a)+1),2)if prod(q:=a[i:j])==lcm(*q)*gcd(*q))

class Solution:
    def maxLength(self, a: List[int]) -> int:
        return max(2,*(j-i for i,j in combinations(range(len(a)+1),2)if prod(q:=a[i:j])==lcm(*q)))

class Solution:
    def maxLength(self, a: List[int]) -> int:
        r=range(101);return max(2,*(len(q)for i,j in product(r,r)if prod(q:=a[j:i])==lcm(*q)))

class Solution:
    def maxLength(self, a: List[int]) -> int:
        return max(2,*(len(q)for i in range(101)for j in range(i)if prod(q:=a[j:i])==lcm(*q)))

class Solution:
    def maxLength(self, a: List[int]) -> int:
        return max(2,*(len(q)for i in range(1<<14)if prod(q:=a[i>>7:i&127])==lcm(*q)))

class Solution:
    def maxLength(self, a: List[int]) -> int:
        return max(2,*(len(q)for i in range(5**6)if prod(q:=a[i>>7:i&127])==lcm(*q)))

class Solution:
    def maxLength(self, a: List[int]) -> int:
        q=a[:2];[q:=(q:=q+[x])[lcm(*q)<prod(q):]for x in a[2:]];return len(q)

class Solution:
    def maxLength(self, a: List[int]) -> int:
        q=1,-1;[q:=(q:=(*q,x))[prod(q)!=lcm(*q):]for x in a];return len(q)

class Solution:
    def maxLength(self, a: List[int]) -> int:
        q=1,-1;[q:=(*q,x)[prod(q)*x!=lcm(x,*q):]for x in a];return len(q)

test('''
3411. Maximum Subarray With Equal Products
Easy
Topics
premium lock icon
Companies
Hint
You are given an array of positive integers nums.

An array arr is called product equivalent if prod(arr) == lcm(arr) * gcd(arr), where:

prod(arr) is the product of all elements of arr.
gcd(arr) is the GCD of all elements of arr.
lcm(arr) is the LCM of all elements of arr.
Return the length of the longest product equivalent subarray of nums.

 

Example 1:

Input: nums = [1,2,1,2,1,1,1]

Output: 5

Explanation: 

The longest product equivalent subarray is [1, 2, 1, 1, 1], where prod([1, 2, 1, 1, 1]) = 2, gcd([1, 2, 1, 1, 1]) = 1, and lcm([1, 2, 1, 1, 1]) = 2.

Example 2:

Input: nums = [2,3,4,5,6]

Output: 3

Explanation: 

The longest product equivalent subarray is [3, 4, 5].

Example 3:

Input: nums = [1,2,3,1,4,5,1]

Output: 5

 

Constraints:

2 <= nums.length <= 100
1 <= nums[i] <= 10
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
32,555/69.1K
Acceptance Rate
47.1%
Topics
Mid Level
Array
Math
Sliding Window
Enumeration
Number Theory
Weekly Contest 431
icon
Companies
Hint 1
What is the maximum possible lcm?
Similar Questions
Find Greatest Common Divisor of Array
Easy
''')
