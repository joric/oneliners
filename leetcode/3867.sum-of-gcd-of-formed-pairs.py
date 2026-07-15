from lc import *

# https://leetcode.com/problems/sum-of-gcd-of-formed-pairs/solutions/7648117/python-one-line-by-ante-umft/?envType=daily-question&envId=2026-07-16

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        return (lambda pg: sum(gcd(pg[i], pg[len(nums) - i - 1]) for i in range(len(nums)//2)))(sorted([gcd(a,b) for a, b in zip(nums,list(accumulate(nums, max)))]))

class Solution:
    def gcdSum(self, n: list[int]) -> int:
        p=sorted(map(gcd,n,accumulate(n,max)));return sum(map(gcd,p[:len(n)>>1],p[::-1]))

test('''
3867. Sum of GCD of Formed Pairs
Medium
Topics
premium lock icon
Companies
Hint
You are given an integer array nums of length n.

Construct an array prefixGcd where for each index i:

Let mxi = max(nums[0], nums[1], ..., nums[i]).
prefixGcd[i] = gcd(nums[i], mxi).
After constructing prefixGcd:

Sort prefixGcd in non-decreasing order.
Form pairs by taking the smallest unpaired element and the largest unpaired element.
Repeat this process until no more pairs can be formed.
For each formed pair, compute the gcd of the two elements.
If n is odd, the middle element in the prefixGcd array remains unpaired and should be ignored.
Return an integer denoting the sum of the GCD values of all formed pairs.

The term gcd(a, b) denotes the greatest common divisor of a and b.
 

Example 1:

Input: nums = [2,6,4]

Output: 2

Explanation:

Construct prefixGcd:

i   nums[i] mxi prefixGcd[i]
0   2   2   2
1   6   6   6
2   4   6   2
prefixGcd = [2, 6, 2]. After sorting, it forms [2, 2, 6].

Pair the smallest and largest elements: gcd(2, 6) = 2. The remaining middle element 2 is ignored. Thus, the sum is 2.

Example 2:

Input: nums = [3,6,2,8]

Output: 5

Explanation:

Construct prefixGcd:

i   nums[i] mxi prefixGcd[i]
0   3   3   3
1   6   6   6
2   2   6   2
3   8   8   8
prefixGcd = [3, 6, 2, 8]. After sorting, it forms [2, 3, 6, 8].

Form pairs: gcd(2, 8) = 2 and gcd(3, 6) = 3. Thus, the sum is 2 + 3 = 5.

 

Constraints:

1 <= n == nums.length <= 105
1 <= nums[i] <= 10​​​​​​​9
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
32,270/49K
Acceptance Rate
65.9%
Topics
Senior
Array
Math
Two Pointers
Sorting
Simulation
Number Theory
Biweekly Contest 178
icon
Companies
Hint 1
Maintain a running prefix maximum mxi while iterating nums to compute prefixGcd[i] = gcd(nums[i], mxi).
Hint 2
Sort prefixGcd in non-decreasing order.
Hint 3
Form pairs by combining smallest unpaired and largest unpaired elements.
Hint 4
Compute gcd for each pair and sum them; ignore middle element if n is odd.
''')
